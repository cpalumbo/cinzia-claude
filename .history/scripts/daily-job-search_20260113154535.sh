#!/bin/bash

# Daily Job Search Script
# Runs the web-scraper agent to find relevant job postings

# Create output folder if it doesn't exist
mkdir -p output-job-search

# Run the agent
claude -p "Use the web-scraper agent. \
Reference @.claude/agents/docs/job-research.md. \
Find Head of GTM, VP Business Development, COO, CCO roles \
in robotics, AI, and deep tech startups (Series A to C). \
Location: Barcelona, London, or Remote with international scope. \
Posted in the last 24 hours. \
Save to output-job-search/jobs_$(date +%Y-%m-%d).csv"