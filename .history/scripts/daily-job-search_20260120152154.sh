#!/bin/bash

# Daily Job Search Script
# Runs the web-scraper agent to find relevant job postings

# Create output folder if it doesn't exist
mkdir -p output-job-search

# Run the agent
claude -p "Use the web-scraper agent. \
Reference @.claude/agents/docs/job-research.md. \
Find BOTH: \
(A) Head of GTM, Head of Go to Market, GTM Lead, Global Expansion, Head of Strategic Partnerships, Head of Business Development, COO, CCO roles AND \
(B) company-level growth and GTM transition signals \
in robotics, AI, and deep tech startups (Series A to C). \
Location: Barcelona, London, or Remote with international scope. \
Time window: roles posted in last 30 days; company signals in last 90 days. \
For companies without a relevant role posted, still include them if GTM transition signals are detected. \
Save to output-job-search/jobs_and_signals_$(date +%Y-%m-%d).csv"
