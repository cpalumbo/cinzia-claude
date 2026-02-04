#!/bin/bash
# Daily job search automation - runs at 9 AM CET
# Searches across 3 tracks and outputs to CSV

set -e

PROJECT_DIR="/Users/cinziapalumbo/cinzia-claude"
OUTPUT_DIR="$PROJECT_DIR/projects/job-search/outputs"
DATE=$(date +%Y-%m-%d)
LOG_FILE="$OUTPUT_DIR/launchd.log"

# Ensure output directory exists
mkdir -p "$OUTPUT_DIR"

echo "$(date): Starting daily job search..." >> "$LOG_FILE"

cd "$PROJECT_DIR"

# Run claude with the job search agent
claude -p "Use the web-scraper agent to research job opportunities. Reference @.claude/agents/docs/job-search.md for the full specification.

Search across all THREE tracks:
1. Startup Partnerships at Tech Giants (Anthropic, OpenAI, Google, AWS, Microsoft, Meta, NVIDIA)
2. Ex-Founder / Former Founder Roles (YC, Wellfound, LinkedIn)
3. GTM Leadership at Startups (robotics, AI, deep tech - Seed to Series C)

Location filter: Barcelona, London, Remote EU, or EU-based
Time window: Last 30 days

Output ONLY a CSV file (no summary.md) to: $OUTPUT_DIR/jobs_${DATE}.csv

Columns: type, company_name, company_description, industry_vertical, job_title, job_url, location, date_posted, fit_score, company_stage, GTM_maturity_signal, outreach_angle

Aim for 15-25 quality results. Deduplicate against recent outputs if possible." 2>&1 >> "$LOG_FILE"

echo "$(date): Job search complete. Output: $OUTPUT_DIR/jobs_${DATE}.csv" >> "$LOG_FILE"
