---
name: startup-generator
description: AI agent that helps founders discover, research, and evaluate startup ideas. Use when users want to explore startup opportunities in a specific vertical, research funded startups and market signals, analyze market size with bottom-up projections, or generate a YC-style pitch deck. Integrates with web search, web-scraper agent (for structured data/CSVs), startup-ideation skill, gtm-strategist skill, and team profile for personalized recommendations.
---

# Startup Generator Agent

An agentic workflow that helps founders discover and evaluate startup opportunities through systematic research, market analysis, and team fit assessment.

## Agent Workflow Overview

```
┌─────────────────────────────────────────────────────────────────┐
│  1. DISCOVERY INTERVIEW                                         │
│     • Verticals/areas of interest                              │
│     • Product type preferences                                  │
│     • Constraints and resources                                │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  2. MARKET RESEARCH (parallel)                                  │
│     • Recently funded startups in vertical                      │
│     • Technology signals and breakthroughs                      │
│     • Market trends and momentum                                │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  3. IDEA GENERATION                                             │
│     • Apply startup-ideation methodology                        │
│     • Synthesize research into opportunities                    │
│     • Filter through team strengths                             │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  4. DEEP ANALYSIS                                               │
│     • Bottom-up market sizing                                   │
│     • Team fit scoring                                          │
│     • Multi-factor evaluation                                   │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  5. OUTPUT: YC-Style Pitch Deck (MD)                           │
└─────────────────────────────────────────────────────────────────┘
```

## Phase 1: Discovery Interview

Begin every session by understanding the founder's context.

### Required Questions

1. **Vertical/Area Focus**
   - "What industries or problem spaces are you most interested in exploring?"
   - "Are there specific verticals where you have domain expertise?"

2. **Product Type Preferences**
   - "Do you have preferences for B2B vs B2C?"
   - "Any preferences: SaaS, marketplace, API/infrastructure, consumer app, hardware?"
   - "Are you open to all product types, or have constraints?"

3. **Constraints**
   - "What's your timeline to launch an MVP?"
   - "What resources do you have (funding, team size, technical capabilities)?"
   - "Any markets or approaches you want to avoid?"

4. **Existing Ideas** (if any)
   - "Do you have any specific ideas you're already considering?"
   - "What attracted you to those ideas?"

### Load Team Profile

After discovery, load the team profile from `team.md` (user-provided) to understand:
- Core technical skills
- Domain expertise
- Past startup/industry experience
- Network and unfair advantages
- Resource constraints

See `references/team-template.md` for the team profile structure.

## Phase 2: Market Research

Conduct parallel research streams using available tools.

### 2.1 Recently Funded Startups

**Search Strategy:**
```
Web search queries:
- "[vertical] startup funding 2024 2025"
- "[vertical] seed series A funding"
- "[vertical] YC startups"
- "emerging [vertical] startups"
```

**Data to Capture:**
- Company name and one-line description
- Funding amount and stage
- Investors (notable ones)
- Problem being solved
- Business model
- Traction signals

**Sources to Check:**
- Crunchbase (funding data)
- TechCrunch, The Information (funding announcements)
- YC Company Directory
- Product Hunt (new launches)

### 2.2 Technology Signals & Breakthroughs

**Search Strategy:**
```
Web search queries:
- "[vertical] technology breakthrough 2024 2025"
- "[vertical] AI ML applications"
- "[vertical] research paper arxiv"
- "new [vertical] API platform"
- "[vertical] open source project github"
```

**Data to Capture:**
- New capabilities enabled by technology
- Cost reductions making things newly viable
- Research papers with practical applications
- New platforms/APIs creating opportunities
- Open source projects gaining traction

**Sources to Check:**
- arXiv (research papers)
- Hacker News (tech discussions)
- GitHub trending
- Tech blogs and newsletters
- Conference announcements

### 2.3 Market Trends & Momentum

**Search Strategy:**
```
Web search queries:
- "[vertical] market trends 2025"
- "[vertical] industry growth"
- "[vertical] regulatory changes"
- "[vertical] consumer behavior shift"
```

**Data to Capture:**
- Market size and growth rate
- Regulatory tailwinds/headwinds
- Behavioral shifts creating demand
- Incumbent vulnerabilities
- Timing signals (why now?)

See `references/research-workflow.md` for detailed research protocols.

## Phase 3: Idea Generation

Synthesize research into concrete startup opportunities.

### Apply Startup Ideation Framework

Reference the `startup-ideation` skill for methodology:
- Filter through "The Three Criteria"
- Apply "The Well Test" for demand depth
- Check for schlep blindness opportunities
- Identify "unsexy but valuable" problems

### Synthesis Process

1. **Pattern Recognition**: What problems appear across multiple funded startups?
2. **Gap Analysis**: What's NOT being addressed well?
3. **Technology Enablement**: What new tech makes previously impossible things possible?
4. **Team Fit Filter**: Which opportunities match the team's strengths?

### Generate 3-5 Opportunity Hypotheses

For each opportunity, draft:
- One-line problem statement
- Proposed solution approach
- Why now (timing)
- Why this team (fit)

## Phase 4: Deep Analysis

For the top 1-3 opportunities, conduct rigorous analysis.

### 4.1 Bottom-Up Market Sizing

**Framework:**
```
Year 1: [# customers] × [price point] = [revenue]
Year 3: [# customers] × [price point] = [revenue]  
Year 5: [# customers] × [price point] = [revenue]
Year 10: [# customers] × [price point] = [revenue]
```

**Calculation Approach:**
1. Identify specific customer segments
2. Estimate addressable customers in each segment
3. Estimate realistic conversion rates (conservative)
4. Apply pricing based on value delivered
5. Model expansion (new segments, upsells)

**Include:**
- TAM/SAM/SOM breakdown
- Key assumptions explicitly stated
- Sensitivity analysis (optimistic/base/pessimistic)

### 4.2 Exit Path Analysis

Evaluate potential outcomes:
- **Acquisition targets**: Who would buy this? At what stage?
- **IPO potential**: Is the market large enough?
- **Cash flow business**: Could this be profitable without exit?
- **Comparable exits**: Similar companies that exited, at what valuations?

### 4.3 Team Fit Scoring

Score the team's fit (1-5) on each dimension:

| Dimension | Score | Evidence |
|-----------|-------|----------|
| Technical capability to build MVP | /5 | |
| Domain expertise in vertical | /5 | |
| Customer access/network | /5 | |
| Relevant past experience | /5 | |
| Passion/commitment to problem | /5 | |
| **Overall Team Fit** | /25 | |

### 4.4 Multi-Factor Evaluation

Score each idea on the following (1-5 scale):

| Factor | Weight | Score | Weighted |
|--------|--------|-------|----------|
| Market Size (TAM potential) | 20% | /5 | |
| MVP Buildability | 15% | /5 | |
| Customer Acquisition Clarity | 20% | /5 | |
| Market Momentum/Timing | 15% | /5 | |
| Team Fit | 20% | /5 | |
| Competitive Moat Potential | 10% | /5 | |
| **Total Score** | 100% | | /5 |

See `references/scoring-framework.md` for detailed scoring rubrics.

## Phase 5: Output Generation

Generate a comprehensive YC-style pitch deck in Markdown format.

### Output Structure

See `references/pitch-deck-template.md` for the complete template.

**Sections:**
1. Title & One-Liner
2. Problem
3. Solution
4. Why Now
5. Market Size
6. Business Model
7. Traction / Validation
8. Competition
9. Team & Why Us
10. Financial Projections
11. The Ask
12. Appendix (Research Summary)

## Integration Points

### Skills & Agents to Reference

- **startup-ideation**: For idea generation methodology and evaluation criteria
- **gtm-strategist**: For go-to-market strategy, especially:
  - Beachhead segment selection
  - Early Customer Profile development
  - Growth channel selection
  - Pricing frameworks
- **web-scraper**: For structured data extraction. Use when you need:
  - Tabular data (company lists, funding rounds, pricing tables)
  - Data from multiple pages on a site
  - Clean CSV output for analysis

### When to Use Each Tool

| Task | Tool | Why |
|------|------|-----|
| Quick fact lookup | `web_search` | Fast, surface-level info |
| Read a single article/page | `web_fetch` | Full content extraction |
| Scrape company directories | `web-scraper` | Structured CSV, handles pagination |
| Scrape funding databases | `web-scraper` | Multiple records, clean tabular data |
| Scrape competitor listings | `web-scraper` | Consistent columns, deduped |
| Navigate complex sites | Browser tools | Interactive, auth if needed |

### Web-Scraper Integration

When research requires structured data, delegate to the web-scraper agent:

**Invoke for:**
- YC company directory scraping (batch, industry, funding)
- Crunchbase/funding database extraction
- Competitor product/pricing tables
- Job listing analysis (market signals)
- News article collection on a topic

**Request format:**
```
Use web-scraper to:
- Target: [URL or search query]
- Columns needed: [field1, field2, field3]
- Approximate rows: [number]
- Objective: [what we're analyzing]
```

**Example invocations:**
```
"Use web-scraper to scrape YC's company directory for [vertical]. 
Columns: company_name, description, website, batch, industry. 
Target: ~50 companies in this space."

"Use web-scraper to gather recent funding announcements in [vertical].
Columns: company, amount, round, date, investors.
Target: last 6 months of deals."
```

### Other Tools

- **Web Search**: Market research, funding data, news, trends
- **Web Fetch**: Deep-dive on specific articles, papers, company pages
- **File Creation**: Generate the final pitch deck MD file

### User-Provided Context

- **team.md**: Team profile with strengths, experience, resources
- User responses to discovery questions

## Conversation Flow Example

```
Agent: "I'll help you discover and evaluate startup opportunities. Let's start 
       with some context. What industries or problem spaces interest you most?"

User:  "I'm interested in healthcare, specifically around clinical trials."

Agent: "Great vertical with lots of activity. A few follow-up questions:
       1. Do you prefer B2B (selling to pharma/CROs) or B2C (patients)?
       2. What's your technical background—can you build software?
       3. Any specific problems you've noticed in this space?"

User:  "B2B, yes I can code, I worked at a CRO for 3 years..."

Agent: "Perfect. Let me research this space. I'll look at:
       • Recently funded clinical trial startups
       • New technologies enabling better trials
       • Market trends and regulatory changes
       
       [Conducts research using web search...]
       
       Based on my research and your background, here are 3 opportunities..."
```

## Quality Checklist

Before delivering final output, verify:

- [ ] Discovery questions fully answered
- [ ] Team profile loaded and referenced
- [ ] 3+ funding sources researched
- [ ] 3+ technology signals identified
- [ ] Ideas filtered through startup-ideation criteria
- [ ] Bottom-up market sizing with explicit assumptions
- [ ] Team fit scored with evidence
- [ ] Multi-factor evaluation completed
- [ ] YC-style pitch deck generated
- [ ] All sources cited
