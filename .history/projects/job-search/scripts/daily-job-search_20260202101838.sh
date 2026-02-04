#!/bin/bash

# Daily Job Search Script
# Runs the web-scraper agent to find relevant job postings across three tracks:
# 1. Startup Partnerships at AI/Tech Giants
# 2. Ex-Founder / Former Founder roles
# 3. GTM Leadership at startups

# Create output folder if it doesn't exist
mkdir -p output-job-search

# Run the agent
claude -p "Use the web-scraper agent. \
Reference @.claude/agents/docs/job-research.md. \

Search across THREE tracks: \

**TRACK 1: Startup Partnerships at Tech Giants** \
Search Anthropic, OpenAI, Google, AWS, Microsoft, Meta, NVIDIA careers for: \
Head of Startup Partnerships, Startup Partnerships Lead, Director Startup Partnerships, \
Head of Startup Programs, Startup Ecosystem Lead, Developer Partnerships, Strategic Partnerships (startups). \

**TRACK 2: Ex-Founder / Former Founder Roles** \
Search YC Work at a Startup (workatastartup.com), Wellfound, LinkedIn, Greenhouse job boards for: \
'ex-founder', 'former founder', 'ex founder', 'founding experience', \
'Technical Ex-Founder', 'Ex-Founder GTM', 'Ex-Founder Sales', 'Ex-Founder Ops'. \
Focus on AI, SaaS, deep tech, robotics, developer tools companies. \

**TRACK 3: GTM Leadership at Startups** \
Search for: Head of GTM, Head of Go to Market, GTM Lead, VP GTM, Head of Growth, \
Head of Strategic Partnerships, Head of Business Development, VP Partnerships, \
COO, CCO, CRO, General Manager roles \
in robotics, AI, and deep tech startups (Series A to C). \
Also capture company-level GTM transition signals (hiring sales/marketing teams, expansion announcements). \

**Location filter:** Barcelona, London, Remote (with international scope), or EU-based. \
**Time window:** roles posted in last 30 days; company signals in last 90 days. \

For each result capture: \
company_name, company_description, industry_vertical, job_title, job_url, location, \
date_posted, fit_score (1-5), company_stage, track (partnerships|ex-founder|gtm). \

For companies without a relevant role posted, still include them if GTM transition signals are detected. \

Save to output-job-search/jobs_and_signals_$(date +%Y-%m-%d).csv"
