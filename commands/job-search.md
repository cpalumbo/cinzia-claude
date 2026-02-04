---
name: job-search
description: Run daily job search across three tracks (Tech Giants Partnerships, Ex-Founder roles, GTM Leadership)
---

Use the web-scraper agent to research job opportunities. Reference @.claude/agents/docs/job-search.md for the full specification.

Search across all THREE tracks:
1. Startup Partnerships at Tech Giants (Anthropic, OpenAI, Google, AWS, Microsoft, Meta, NVIDIA)
2. Ex-Founder / Former Founder Roles (YC, Wellfound, LinkedIn)
3. GTM Leadership at Startups (robotics, AI, deep tech - Seed to Series C)

**Location filter:** Barcelona, London, Remote EU, or EU-based
**Time window:** Last 30 days

**Output:** CSV file to `projects/job-search/outputs/jobs_<today's date>.csv`

**Columns:** type, company_name, company_description, industry_vertical, job_title, job_url, location, date_posted, fit_score, company_stage, GTM_maturity_signal, outreach_angle

Aim for 15-25 quality results. Deduplicate against recent outputs if possible.
