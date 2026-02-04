#!/bin/bash
#
# Startup Generator CLI
# Automates startup idea research and pitch deck generation
#
# Usage:
#   ./startup-generator.sh --vertical "clinical trials" --team ./team.md
#   ./startup-generator.sh -v "fintech" -t B2B --team ./team.md --output ./output
#
# Requirements:
#   - Claude Code installed (npm install -g @anthropic-ai/claude-code)
#   - ANTHROPIC_API_KEY set
#   - Firecrawl MCP configured (for web scraping)

set -e

# Default values
VERTICAL=""
PRODUCT_TYPE="any"
TEAM_FILE=""
OUTPUT_DIR="./output"
MODEL="sonnet"
VERBOSE=false

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Print usage
usage() {
    cat << EOF
Usage: $(basename "$0") [OPTIONS]

Startup Generator - Research and evaluate startup opportunities

OPTIONS:
    -v, --vertical TEXT     Industry/vertical to explore (required)
                            Examples: "clinical trials", "fintech", "logistics"
    
    -t, --type TYPE         Product type preference (default: any)
                            Options: B2B, B2C, SaaS, marketplace, API, any
    
    --team FILE             Path to team.md profile (recommended)
    
    -o, --output DIR        Output directory (default: ./output)
    
    -m, --model MODEL       Claude model to use (default: sonnet)
                            Options: sonnet, opus, haiku
    
    --verbose               Show detailed progress
    
    -h, --help              Show this help message

EXAMPLES:
    # Basic usage
    ./startup-generator.sh -v "healthcare AI"

    # With team profile and B2B focus
    ./startup-generator.sh -v "clinical trials" -t B2B --team ./team.md

    # Full options
    ./startup-generator.sh \\
        --vertical "developer tools" \\
        --type SaaS \\
        --team ./team.md \\
        --output ./research \\
        --model opus \\
        --verbose

EOF
    exit 0
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -v|--vertical)
            VERTICAL="$2"
            shift 2
            ;;
        -t|--type)
            PRODUCT_TYPE="$2"
            shift 2
            ;;
        --team)
            TEAM_FILE="$2"
            shift 2
            ;;
        -o|--output)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        -m|--model)
            MODEL="$2"
            shift 2
            ;;
        --verbose)
            VERBOSE=true
            shift
            ;;
        -h|--help)
            usage
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            usage
            ;;
    esac
done

# Validate required arguments
if [[ -z "$VERTICAL" ]]; then
    echo -e "${RED}Error: --vertical is required${NC}"
    echo ""
    usage
fi

# Check Claude Code is installed
if ! command -v claude &> /dev/null; then
    echo -e "${RED}Error: Claude Code is not installed${NC}"
    echo "Install with: npm install -g @anthropic-ai/claude-code"
    exit 1
fi

# Check API key
if [[ -z "$ANTHROPIC_API_KEY" ]]; then
    echo -e "${RED}Error: ANTHROPIC_API_KEY is not set${NC}"
    exit 1
fi

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Generate timestamp for filenames
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
SAFE_VERTICAL=$(echo "$VERTICAL" | tr ' ' '-' | tr '[:upper:]' '[:lower:]')
OUTPUT_FILE="${OUTPUT_DIR}/${SAFE_VERTICAL}-pitch-deck-${TIMESTAMP}.md"
RESEARCH_FILE="${OUTPUT_DIR}/${SAFE_VERTICAL}-research-${TIMESTAMP}.md"

# Build team context
TEAM_CONTEXT=""
if [[ -n "$TEAM_FILE" && -f "$TEAM_FILE" ]]; then
    TEAM_CONTEXT="

## Team Profile

$(cat "$TEAM_FILE")
"
    echo -e "${GREEN}✓ Loaded team profile from ${TEAM_FILE}${NC}"
else
    echo -e "${YELLOW}⚠ No team profile provided. Results won't be personalized to your strengths.${NC}"
fi

# Print configuration
echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}  Startup Generator${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "  Vertical:     ${GREEN}${VERTICAL}${NC}"
echo -e "  Product Type: ${GREEN}${PRODUCT_TYPE}${NC}"
echo -e "  Model:        ${GREEN}${MODEL}${NC}"
echo -e "  Output:       ${GREEN}${OUTPUT_FILE}${NC}"
echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Build the prompt
read -r -d '' PROMPT << EOF || true
You are a startup research agent. Your task is to discover and evaluate startup opportunities in the "${VERTICAL}" vertical.

## Your Mission

1. **Research Phase** - Gather comprehensive market intelligence:
   - Search for recently funded startups in ${VERTICAL} (use web search)
   - Find technology signals and breakthroughs enabling new solutions
   - Identify market trends and momentum indicators
   - Use the web-scraper/firecrawl tools to extract structured data when useful (e.g., YC company directory, funding databases)

2. **Ideation Phase** - Generate 3-5 opportunity hypotheses:
   - Apply startup ideation best practices (problems > solutions, deep demand > broad)
   - Filter through the "three criteria": founders want it, can build it, few realize it's worth doing
   - Consider schlep blindness - what tedious problems are being avoided?

3. **Analysis Phase** - For the top 2-3 opportunities:
   - Bottom-up market sizing (Year 1, 3, 5, 10 projections)
   - Team fit scoring (if team profile provided)
   - Multi-factor evaluation: market size, MVP buildability, customer acquisition, momentum, moat potential

4. **Output Phase** - Generate a YC-style pitch deck in Markdown

## Constraints

- Product type preference: ${PRODUCT_TYPE}
- Focus on opportunities that are actionable in the next 6-12 months
- Prioritize ideas where technology is ready NOW, not speculative
${TEAM_CONTEXT}

## Output Format

Create a comprehensive Markdown document with:

1. **Executive Summary** - Top 1-2 recommended opportunities
2. **Research Findings**
   - Funded startups in space (table format)
   - Technology signals
   - Market trends
3. **Opportunity Analysis** (for each of top 2-3 ideas)
   - Problem & Solution
   - Why Now
   - Market Size (bottom-up)
   - Team Fit Score (if team provided)
   - Multi-factor score
4. **Recommended Pitch Deck** - Full YC-style deck for #1 opportunity
5. **Appendix** - Sources and additional research

Begin your research now. Be thorough but focused.
EOF

# Verbose output
if [[ "$VERBOSE" == true ]]; then
    echo -e "${YELLOW}Prompt:${NC}"
    echo "$PROMPT"
    echo ""
fi

echo -e "${YELLOW}Starting research... This may take 5-15 minutes.${NC}"
echo ""

# Run Claude Code
if [[ "$VERBOSE" == true ]]; then
    claude -p "$PROMPT" \
        --model "claude-${MODEL}-4-20250514" \
        --allowedTools "Bash(curl:*),Read,Write,mcp__firecrawl__firecrawl_scrape,mcp__firecrawl__firecrawl_search" \
        --output-format text \
        | tee "$OUTPUT_FILE"
else
    claude -p "$PROMPT" \
        --model "claude-${MODEL}-4-20250514" \
        --allowedTools "Bash(curl:*),Read,Write,mcp__firecrawl__firecrawl_scrape,mcp__firecrawl__firecrawl_search" \
        --output-format text \
        > "$OUTPUT_FILE" 2>&1
fi

# Check if output was generated
if [[ -s "$OUTPUT_FILE" ]]; then
    echo ""
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}  ✓ Research complete!${NC}"
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo -e "  Output: ${BLUE}${OUTPUT_FILE}${NC}"
    echo ""
    echo -e "  Preview:"
    echo -e "${YELLOW}  ─────────────────────────────────────────────────${NC}"
    head -30 "$OUTPUT_FILE" | sed 's/^/  /'
    echo -e "${YELLOW}  ─────────────────────────────────────────────────${NC}"
    echo ""
    echo -e "  View full report: ${BLUE}cat ${OUTPUT_FILE}${NC}"
    echo ""
else
    echo -e "${RED}Error: No output generated. Check your API key and try with --verbose${NC}"
    exit 1
fi