#!/usr/bin/env python3
"""
2025 Unicorn Startups - GTM & Partnerships Roles Search
Searches for GTM, Partnerships, and Leadership roles at unicorns that crossed $1B in 2025
Focus on EU-based opportunities (Barcelona, London, Remote EU)
"""

import os
import csv
import time
from datetime import datetime
from typing import List, Dict, Optional
from firecrawl import FirecrawlApp

# Initialize Firecrawl
FIRECRAWL_API_KEY = os.getenv('FIRECRAWL_API_KEY')
if not FIRECRAWL_API_KEY:
    raise ValueError("FIRECRAWL_API_KEY not found in environment variables")

app = FirecrawlApp(api_key=FIRECRAWL_API_KEY)

# Output file
OUTPUT_FILE = '/Users/cinziapalumbo/cinzia-claude/projects/job-search/outputs/jobs_2026-02-04_unicorns.csv'

# CSV Headers
HEADERS = [
    'company_name',
    'company_description',
    'hq_country',
    'job_title',
    'job_url',
    'location',
    'remote_policy',
    'role_type',
    'fit_score',
    'notes'
]

# Target companies - EU-headquartered first
UNICORN_COMPANIES = [
    # Priority 1: EU Headquarters
    {'name': 'Lovable', 'hq': 'Sweden', 'flag': '🇸🇪', 'description': 'AI front-end code generation', 'url': 'https://lovable.dev'},
    {'name': 'Tines', 'hq': 'Ireland', 'flag': '🇮🇪', 'description': 'Security automation workflows', 'url': 'https://www.tines.com'},
    {'name': 'Framer', 'hq': 'Netherlands', 'flag': '🇳🇱', 'description': 'AI-native website builder', 'url': 'https://www.framer.com'},
    {'name': 'Fuse Energy', 'hq': 'UK', 'flag': '🇬🇧', 'description': 'Building energy abundance', 'url': 'https://www.fuseenergy.com'},
    {'name': 'n8n', 'hq': 'Germany', 'flag': '🇩🇪', 'description': 'AI workflow automation tool', 'url': 'https://n8n.io'},
    {'name': 'Quantum Systems', 'hq': 'Germany', 'flag': '🇩🇪', 'description': 'Defence drones using AI', 'url': 'https://quantum-systems.com'},
    {'name': 'Legora', 'hq': 'Sweden', 'flag': '🇸🇪', 'description': 'AI legal tech platform', 'url': 'https://legora.com'},
    {'name': 'Sana', 'hq': 'Sweden', 'flag': '🇸🇪', 'description': 'AI tools for human knowledge', 'url': 'https://www.sanalabs.com'},
    {'name': 'Parloa', 'hq': 'Germany', 'flag': '🇩🇪', 'description': 'AI voice automation for support', 'url': 'https://www.parloa.com'},
    {'name': 'Nothing', 'hq': 'UK', 'flag': '🇬🇧', 'description': 'Consumer devices with AI layer', 'url': 'https://nothing.tech'},
    {'name': 'Poolside', 'hq': 'France', 'flag': '🇫🇷', 'description': 'Foundation model for coding', 'url': 'https://poolside.ai'},
    {'name': 'Coralogix', 'hq': 'Israel', 'flag': '🇮🇱', 'description': 'AI observability and logging', 'url': 'https://coralogix.com'},
    {'name': 'Lighthouse', 'hq': 'UK', 'flag': '🇬🇧', 'description': 'AI property intelligence', 'url': 'https://lighthouse.re'},
    {'name': 'Neko Health', 'hq': 'Sweden', 'flag': '🇸🇪', 'description': 'Preventative healthcare', 'url': 'https://www.nekohealth.com'},
    {'name': 'Isar Aerospace', 'hq': 'Germany', 'flag': '🇩🇪', 'description': 'Launch vehicles using AI', 'url': 'https://www.isaraerospace.com'},
    {'name': 'Tide', 'hq': 'UK', 'flag': '🇬🇧', 'description': 'SME banking with embedded AI', 'url': 'https://www.tide.co'},
    {'name': 'Dream', 'hq': 'Israel', 'flag': '🇮🇱', 'description': 'Critical infrastructure cybersecurity', 'url': 'https://www.dream.security'},
    {'name': 'Isomorphic Labs', 'hq': 'UK', 'flag': '🇬🇧', 'description': 'AI drug design platform', 'url': 'https://www.isomorphiclabs.com'},
    {'name': 'TEKEVER', 'hq': 'Portugal', 'flag': '🇵🇹', 'description': 'Maritime surveillance drones', 'url': 'https://www.tekever.com'},

    # Priority 2: US HQ with EU presence/remote-friendly
    {'name': 'Abridge', 'hq': 'US', 'flag': '🇺🇸', 'description': 'Clinical transcription AI', 'url': 'https://www.abridge.com'},
    {'name': 'Clay', 'hq': 'US', 'flag': '🇺🇸', 'description': 'AI prospecting and outreach', 'url': 'https://www.clay.com'},
    {'name': 'Hippocratic AI', 'hq': 'US', 'flag': '🇺🇸', 'description': 'Safe medical LLMs', 'url': 'https://www.hippocratic.ai'},
    {'name': 'Modal', 'hq': 'US', 'flag': '🇺🇸', 'description': 'Serverless compute for AI apps', 'url': 'https://modal.com'},
    {'name': 'CHAOS Industries', 'hq': 'US', 'flag': '🇺🇸', 'description': 'Counter-drone radar', 'url': 'https://chaos.industries'},
    {'name': 'Filevine', 'hq': 'US', 'flag': '🇺🇸', 'description': 'Legal case management AI', 'url': 'https://www.filevine.com'},
    {'name': 'Eon.io', 'hq': 'US', 'flag': '🇺🇸', 'description': 'Cloud backup platform', 'url': 'https://eon.io'},
    {'name': 'Eve', 'hq': 'US', 'flag': '🇺🇸', 'description': 'AI legal tech platform', 'url': 'https://www.eve.law'},
    {'name': 'Function Health', 'hq': 'US', 'flag': '🇺🇸', 'description': 'Healthcare platform', 'url': 'https://www.functionhealth.com'},
    {'name': 'Mercor', 'hq': 'US', 'flag': '🇺🇸', 'description': 'AI talent matching marketplace', 'url': 'https://mercor.com'},
    {'name': 'Peregrine', 'hq': 'US', 'flag': '🇺🇸', 'description': 'Data integration platform', 'url': 'https://www.peregrine.ai'},
    {'name': 'Periodic Labs', 'hq': 'US', 'flag': '🇺🇸', 'description': 'Computational drug discovery', 'url': 'https://periodic.com'},
    {'name': 'ShopMy', 'hq': 'US', 'flag': '🇺🇸', 'description': 'Creator commerce storefronts', 'url': 'https://shopmy.us'},
    {'name': 'Supabase', 'hq': 'US', 'flag': '🇺🇸', 'description': 'Open-source backend + AI tools', 'url': 'https://supabase.com'},
    {'name': 'Kalshi', 'hq': 'US', 'flag': '🇺🇸', 'description': 'Regulated prediction markets', 'url': 'https://kalshi.com'},
    {'name': 'Tandem', 'hq': 'US', 'flag': '🇺🇸', 'description': 'AI for pharmacy coordination', 'url': 'https://www.tandemdiabetes.com'},
    {'name': 'Base Power Company', 'hq': 'US', 'flag': '🇺🇸', 'description': 'Energy infrastructure', 'url': 'https://basepower.com'},
    {'name': 'Cursor', 'hq': 'US', 'flag': '🇺🇸', 'description': 'AI coding environment', 'url': 'https://cursor.sh'},
    {'name': 'fal', 'hq': 'US', 'flag': '🇺🇸', 'description': 'Real-time AI inference engine', 'url': 'https://fal.ai'},
    {'name': 'Nourish', 'hq': 'US', 'flag': '🇺🇸', 'description': 'Nutrition telehealth with AI', 'url': 'https://www.nourishcare.com'},
    {'name': 'Decagon', 'hq': 'US', 'flag': '🇺🇸', 'description': 'Automated customer resolution', 'url': 'https://decagon.ai'},
    {'name': 'Fireworks', 'hq': 'US', 'flag': '🇺🇸', 'description': 'High-speed model inference', 'url': 'https://fireworks.ai'},
    {'name': 'LangChain', 'hq': 'US', 'flag': '🇺🇸', 'description': 'Agentic application framework', 'url': 'https://www.langchain.com'},
    {'name': 'Linear', 'hq': 'US', 'flag': '🇺🇸', 'description': 'Product issue tracking with AI', 'url': 'https://linear.app'},
    {'name': 'Onebrief', 'hq': 'US', 'flag': '🇺🇸', 'description': 'Defense planning using AI', 'url': 'https://www.onebrief.com'},
    {'name': 'Gamma', 'hq': 'US', 'flag': '🇺🇸', 'description': 'AI-native presentations and decks', 'url': 'https://gamma.app'},
    {'name': 'Posthog', 'hq': 'US', 'flag': '🇺🇸', 'description': 'Product analytics with AI', 'url': 'https://posthog.com'},
    {'name': 'Thinking Machines', 'hq': 'US', 'flag': '🇺🇸', 'description': 'AI research lab', 'url': 'https://thinkingmachines.com'},
]

# Role keywords for classification
ROLE_KEYWORDS = {
    'Partnerships': ['partnership', 'partner manager', 'ecosystem', 'alliances', 'channel', 'strategic partnerships'],
    'GTM Leadership': ['head of sales', 'vp sales', 'head of marketing', 'vp marketing', 'head of growth', 'vp growth', 'cro', 'cmo', 'head of gtm', 'vp gtm', 'go-to-market'],
    'BD': ['business development', 'enterprise sales', 'strategic accounts', 'account executive', 'sales director'],
    'RevOps': ['revenue operations', 'gtm operations', 'sales operations', 'revops'],
    'Regional': ['country manager', 'regional manager', 'emea', 'europe manager', 'eu lead']
}

LOCATION_KEYWORDS = ['barcelona', 'london', 'remote', 'europe', 'eu', 'emea', 'uk', 'spain', 'germany', 'france', 'netherlands', 'sweden', 'ireland', 'portugal', 'israel']


def classify_role_type(title: str) -> str:
    """Classify role into one of the target role types"""
    title_lower = title.lower()

    for role_type, keywords in ROLE_KEYWORDS.items():
        if any(kw in title_lower for kw in keywords):
            return role_type

    return 'Other'


def determine_remote_policy(location: str, description: str = '') -> str:
    """Determine remote work policy from location string"""
    location_lower = location.lower()
    desc_lower = description.lower()

    if 'remote' in location_lower or 'remote' in desc_lower:
        if 'hybrid' in location_lower or 'hybrid' in desc_lower:
            return 'Hybrid'
        return 'Remote'
    elif 'hybrid' in location_lower or 'hybrid' in desc_lower:
        return 'Hybrid'
    else:
        return 'On-site'


def calculate_fit_score(job: Dict) -> int:
    """
    Calculate fit score 1-10 based on seniority and GTM focus
    10 = Perfect fit (Head/VP Partnerships or GTM at relevant company)
    1 = Low relevance
    """
    score = 5  # Base score

    title_lower = job.get('job_title', '').lower()
    role_type = job.get('role_type', '')
    hq = job.get('hq_country', '')
    location = job.get('location', '').lower()

    # High value roles (+3-4)
    if any(x in title_lower for x in ['head of partnerships', 'vp partnerships', 'director partnerships']):
        score += 4
    elif any(x in title_lower for x in ['head of', 'vp ', 'director of']):
        if any(x in title_lower for x in ['gtm', 'sales', 'growth', 'marketing', 'business development']):
            score += 3
    elif 'strategic partnerships' in title_lower or 'partner manager' in title_lower:
        score += 2

    # EU HQ bonus (+1)
    if hq in ['Sweden', 'Ireland', 'Netherlands', 'UK', 'Germany', 'France', 'Portugal', 'Israel']:
        score += 1

    # Location preference (+1)
    if any(x in location for x in ['barcelona', 'london', 'remote']):
        score += 1

    # Role type relevance
    if role_type in ['Partnerships', 'GTM Leadership']:
        score += 1

    # Relevance penalty for non-GTM roles
    if role_type == 'Other':
        score -= 2

    return max(1, min(10, score))


def search_company_careers(company: Dict) -> List[Dict]:
    """Search a company's careers page and job boards"""
    results = []
    company_name = company['name']

    print(f"\n{company['flag']} Searching {company_name} ({company['hq']})...")

    try:
        # Build search query
        search_query = f"{company_name} careers partnerships OR GTM OR sales OR growth OR marketing Barcelona OR London OR Remote OR Europe"

        # Try Firecrawl search
        response = app.search(search_query, limit=5)

        if response and 'data' in response:
            for item in response['data']:
                title = item.get('title', '')
                url = item.get('url', '')

                # Skip if not a job posting
                if not title or not url:
                    continue

                # Check if role type matches
                role_type = classify_role_type(title)
                if role_type == 'Other':
                    continue

                # Check if location is relevant
                location = item.get('location', item.get('snippet', ''))
                if not any(kw in location.lower() for kw in LOCATION_KEYWORDS):
                    # Skip if location doesn't match EU criteria
                    continue

                job = {
                    'company_name': company_name,
                    'company_description': company['description'],
                    'hq_country': company['hq'],
                    'job_title': title,
                    'job_url': url,
                    'location': location,
                    'remote_policy': determine_remote_policy(location),
                    'role_type': role_type,
                    'fit_score': 0,
                    'notes': f"Found via search | {company['hq']} HQ"
                }

                job['fit_score'] = calculate_fit_score(job)

                if job['fit_score'] >= 5:
                    results.append(job)
                    print(f"  ✓ {job['job_title']} | Score: {job['fit_score']}")

        # Rate limiting
        time.sleep(2)

    except Exception as e:
        print(f"  ✗ Error: {str(e)}")

    return results


def search_linkedin_jobs(company_name: str) -> List[Dict]:
    """Search LinkedIn for company jobs"""
    try:
        query = f"site:linkedin.com/jobs {company_name} partnerships OR GTM OR sales Barcelona OR London OR Remote"
        response = app.search(query, limit=3)

        jobs = []
        if response and 'data' in response:
            for item in response['data']:
                title = item.get('title', '')
                if title and any(kw in title.lower() for kw in ['partnership', 'gtm', 'sales', 'growth']):
                    jobs.append(item)

        return jobs
    except:
        return []


def deduplicate_results(jobs: List[Dict]) -> List[Dict]:
    """Remove duplicate job postings"""
    seen = set()
    unique_jobs = []

    for job in jobs:
        key = (job['company_name'].lower(), job['job_title'].lower())
        if key not in seen:
            seen.add(key)
            unique_jobs.append(job)

    return unique_jobs


def save_to_csv(jobs: List[Dict], filename: str):
    """Save jobs to CSV file"""
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(jobs)

    print(f"\n✓ Saved {len(jobs)} jobs to {filename}")


def main():
    """Main execution"""
    print("=" * 80)
    print("2025 UNICORN STARTUPS - GTM & PARTNERSHIPS ROLES SEARCH")
    print("=" * 80)
    print(f"Searching {len(UNICORN_COMPANIES)} companies...")
    print("Focus: GTM, Partnerships, Leadership roles in EU or Remote")

    all_jobs = []
    companies_with_results = 0

    # Search each company
    for company in UNICORN_COMPANIES:
        jobs = search_company_careers(company)
        if jobs:
            all_jobs.extend(jobs)
            companies_with_results += 1

        # Stop if we have enough results
        if len(all_jobs) >= 50:
            print(f"\nReached 50 results, stopping search...")
            break

    # Deduplicate and sort by fit score
    unique_jobs = deduplicate_results(all_jobs)
    sorted_jobs = sorted(unique_jobs, key=lambda x: x['fit_score'], reverse=True)

    # Filter to top results if we have too many
    if len(sorted_jobs) > 40:
        sorted_jobs = sorted_jobs[:40]

    # Save to CSV
    save_to_csv(sorted_jobs, OUTPUT_FILE)

    # Summary
    print("\n" + "=" * 80)
    print("SEARCH SUMMARY")
    print("=" * 80)
    print(f"Companies searched: {len(UNICORN_COMPANIES)}")
    print(f"Companies with relevant roles: {companies_with_results}")
    print(f"Total unique jobs found: {len(sorted_jobs)}")

    print(f"\nRole Type Distribution:")
    for role_type in ['Partnerships', 'GTM Leadership', 'BD', 'RevOps', 'Regional']:
        count = sum(1 for j in sorted_jobs if j['role_type'] == role_type)
        if count > 0:
            print(f"  {role_type}: {count} jobs")

    print(f"\nHQ Distribution:")
    hq_counts = {}
    for job in sorted_jobs:
        hq = job['hq_country']
        hq_counts[hq] = hq_counts.get(hq, 0) + 1
    for hq, count in sorted(hq_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {hq}: {count} jobs")

    print(f"\nFit Score Distribution:")
    for score in range(10, 4, -1):
        count = sum(1 for j in sorted_jobs if j['fit_score'] == score)
        if count > 0:
            print(f"  Score {score}: {count} jobs")

    print(f"\nTop 10 Best Fits:")
    for i, job in enumerate(sorted_jobs[:10], 1):
        print(f"\n{i}. {job['job_title']} at {job['company_name']}")
        print(f"   Score: {job['fit_score']}/10 | {job['role_type']} | {job['location']}")
        print(f"   {job['job_url'][:80]}...")

    print(f"\n✓ Results saved to: {OUTPUT_FILE}")


if __name__ == '__main__':
    main()
