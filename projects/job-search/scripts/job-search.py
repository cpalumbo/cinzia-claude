#!/usr/bin/env python3
"""
Executive Roles Search - Three Track Job Research
Searches for executive roles across tech giants, ex-founder positions, and GTM leadership at startups
"""

import os
import csv
import json
from datetime import datetime
from typing import List, Dict
from firecrawl import FirecrawlApp

# Initialize Firecrawl
FIRECRAWL_API_KEY = os.getenv('FIRECRAWL_API_KEY')
if not FIRECRAWL_API_KEY:
    raise ValueError("FIRECRAWL_API_KEY not found in environment variables")

app = FirecrawlApp(api_key=FIRECRAWL_API_KEY)

# Output file path
OUTPUT_FILE = '/Users/cinziapalumbo/cinzia-claude/projects/job-search/outputs/jobs_2026-02-04.csv'

# CSV Headers
HEADERS = [
    'type',
    'company_name',
    'company_description',
    'industry_vertical',
    'job_title',
    'job_url',
    'location',
    'date_posted',
    'fit_score',
    'company_stage',
    'GTM_maturity_signal',
    'outreach_angle'
]

# Target companies and search configurations
TECH_GIANTS = [
    {
        'name': 'Anthropic',
        'careers_url': 'https://www.anthropic.com/careers',
        'keywords': ['startup partnerships', 'startup programs', 'developer partnerships', 'strategic partnerships'],
        'description': 'AI safety and research company developing Claude AI',
        'stage': 'Growth'
    },
    {
        'name': 'OpenAI',
        'careers_url': 'https://openai.com/careers',
        'keywords': ['startup partnerships', 'startup programs', 'developer partnerships', 'strategic partnerships'],
        'description': 'AI research and deployment company behind ChatGPT and GPT models',
        'stage': 'Growth'
    },
    {
        'name': 'Google',
        'careers_url': 'https://careers.google.com',
        'keywords': ['startup partnerships', 'startup programs', 'cloud startup', 'developer partnerships'],
        'description': 'Technology company specializing in Internet services, AI, and cloud computing',
        'stage': 'Public'
    },
    {
        'name': 'AWS',
        'careers_url': 'https://amazon.jobs',
        'keywords': ['startup partnerships', 'startup programs', 'ISV partnerships'],
        'description': 'Amazon Web Services - leading cloud computing platform',
        'stage': 'Public'
    },
    {
        'name': 'Microsoft',
        'careers_url': 'https://careers.microsoft.com',
        'keywords': ['startup partnerships', 'startup programs', 'azure startup'],
        'description': 'Technology company developing software, cloud services, and AI platforms',
        'stage': 'Public'
    },
    {
        'name': 'Meta',
        'careers_url': 'https://www.metacareers.com',
        'keywords': ['startup partnerships', 'developer partnerships', 'strategic partnerships'],
        'description': 'Social technology company building platforms and AI technologies',
        'stage': 'Public'
    },
    {
        'name': 'NVIDIA',
        'careers_url': 'https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite',
        'keywords': ['startup partnerships', 'AI partnerships', 'developer partnerships'],
        'description': 'Computing platform company pioneering GPU and AI computing',
        'stage': 'Public'
    }
]

# Search queries for different tracks
SEARCH_QUERIES = {
    'ex_founder': [
        'ex-founder AI startup',
        'former founder GTM role',
        'ex-founder sales leadership',
        'founder experience required',
    ],
    'gtm_leadership': [
        'Head of GTM AI startup',
        'VP GTM robotics',
        'Head of Go to Market deep tech',
        'GTM Lead autonomous systems',
        'Head of Growth AI',
        'Head of Strategic Partnerships robotics',
        'COO AI startup',
        'CRO deep tech',
    ]
}

LOCATION_FILTERS = ['Barcelona', 'London', 'Remote', 'Europe', 'EU', 'UK', 'Spain']


def calculate_fit_score(job: Dict) -> int:
    """
    Calculate fit score based on role, company, and requirements
    5 = Perfect fit, 1 = Low relevance
    """
    score = 3  # Base score

    title_lower = job.get('job_title', '').lower()
    company = job.get('company_name', '').lower()
    vertical = job.get('industry_vertical', '').lower()

    # Perfect fit indicators (5)
    if any(x in title_lower for x in ['startup partnership', 'ex-founder', 'former founder']):
        score = 5
    elif 'head of gtm' in title_lower or 'vp gtm' in title_lower:
        if any(x in vertical for x in ['robotics', 'ai', 'deep tech', 'autonomous']):
            score = 5

    # Strong fit (4)
    elif any(x in title_lower for x in ['partnership', 'gtm', 'go-to-market', 'strategic']):
        if any(x in vertical for x in ['ai', 'deep tech', 'robotics']):
            score = 4

    # Location adjustment
    location = job.get('location', '').lower()
    if not any(loc in location for loc in ['barcelona', 'london', 'remote', 'europe', 'eu']):
        score = max(1, score - 1)

    return min(5, score)


def determine_outreach_angle(job: Dict) -> str:
    """Generate personalized outreach angle based on role and company"""
    title_lower = job.get('job_title', '').lower()
    vertical = job.get('industry_vertical', '').lower()

    if 'startup partnership' in title_lower or 'developer partnership' in title_lower:
        return "DJI-Apple partnership experience, built global partnerships from zero"
    elif 'ex-founder' in title_lower or 'former founder' in title_lower:
        return "Ex-founder with successful exit, deep GTM expertise in hardware/robotics"
    elif 'robotics' in vertical or 'autonomous' in vertical or 'drone' in vertical:
        return "Robotics native with 10+ years at DJI, understand hardware-software GTM"
    elif 'gtm' in title_lower or 'go-to-market' in title_lower:
        return "Led GTM for international expansion, founder experience, technical partnerships"
    else:
        return "International partnerships leader, founder experience, technical GTM expertise"


def search_tech_giants() -> List[Dict]:
    """Search for startup partnership roles at major tech companies"""
    results = []
    print("\n=== TRACK 1: Tech Giants - Startup Partnerships ===")

    for company in TECH_GIANTS:
        print(f"\nSearching {company['name']}...")
        try:
            # Search the careers page for relevant roles
            search_query = f"{company['name']} startup partnerships OR developer partnerships OR strategic partnerships location:Barcelona OR location:London OR location:Remote"

            response = app.search(search_query, limit=5)

            if response and 'data' in response:
                for item in response['data']:
                    # Parse job details from search result
                    job = {
                        'type': 'job_posting',
                        'company_name': company['name'],
                        'company_description': company['description'],
                        'industry_vertical': 'AI' if 'AI' in company['description'] else 'Cloud/Tech',
                        'job_title': item.get('title', ''),
                        'job_url': item.get('url', ''),
                        'location': item.get('location', 'Not specified'),
                        'date_posted': 'Recent',
                        'fit_score': 0,  # Will calculate after
                        'company_stage': company['stage'],
                        'GTM_maturity_signal': 'Scaling partnerships ecosystem',
                        'outreach_angle': ''
                    }

                    job['fit_score'] = calculate_fit_score(job)
                    job['outreach_angle'] = determine_outreach_angle(job)

                    if job['fit_score'] >= 3:
                        results.append(job)
                        print(f"  ✓ Found: {job['job_title']}")

        except Exception as e:
            print(f"  ✗ Error searching {company['name']}: {str(e)}")

    return results


def search_ex_founder_roles() -> List[Dict]:
    """Search for ex-founder and former founder roles"""
    results = []
    print("\n=== TRACK 2: Ex-Founder / Former Founder Roles ===")

    sources = [
        ('YC Work at a Startup', 'site:workatastartup.com ex-founder OR former founder AI OR robotics OR deep tech'),
        ('Wellfound', 'site:wellfound.com ex-founder OR former founder AI startup'),
        ('LinkedIn Jobs', 'site:linkedin.com/jobs "ex-founder" OR "former founder" AI OR robotics Barcelona OR London OR Remote'),
    ]

    for source_name, query in sources:
        print(f"\nSearching {source_name}...")
        try:
            response = app.search(query, limit=5)

            if response and 'data' in response:
                for item in response['data']:
                    job = {
                        'type': 'job_posting',
                        'company_name': item.get('company', 'Unknown'),
                        'company_description': item.get('description', 'AI/Tech startup'),
                        'industry_vertical': 'AI/Deep Tech',
                        'job_title': item.get('title', ''),
                        'job_url': item.get('url', ''),
                        'location': item.get('location', 'Remote'),
                        'date_posted': item.get('date', 'Recent'),
                        'fit_score': 0,
                        'company_stage': 'Seed-Series B',
                        'GTM_maturity_signal': 'Seeking ex-founder expertise',
                        'outreach_angle': ''
                    }

                    job['fit_score'] = calculate_fit_score(job)
                    job['outreach_angle'] = determine_outreach_angle(job)

                    if job['fit_score'] >= 3:
                        results.append(job)
                        print(f"  ✓ Found: {job['job_title']}")

        except Exception as e:
            print(f"  ✗ Error searching {source_name}: {str(e)}")

    return results


def search_gtm_leadership() -> List[Dict]:
    """Search for GTM leadership roles at startups"""
    results = []
    print("\n=== TRACK 3: GTM Leadership at AI/Robotics Startups ===")

    queries = [
        'Head of GTM OR "VP GTM" robotics OR AI OR "deep tech" Barcelona OR London OR Remote',
        '"Head of Go to Market" OR "GTM Lead" AI startup Barcelona OR London OR Europe',
        'Head of Growth OR "VP Partnerships" robotics OR autonomous systems Remote',
        'COO OR CRO OR CCO AI startup OR "deep tech" Europe',
        '"Head of Strategic Partnerships" OR "Head of Business Development" robotics Barcelona OR London',
    ]

    for query in queries:
        print(f"\nSearching: {query[:60]}...")
        try:
            response = app.search(query, limit=5)

            if response and 'data' in response:
                for item in response['data']:
                    job = {
                        'type': 'job_posting',
                        'company_name': item.get('company', 'Unknown'),
                        'company_description': item.get('description', 'AI/Robotics startup'),
                        'industry_vertical': 'AI/Robotics/Deep Tech',
                        'job_title': item.get('title', ''),
                        'job_url': item.get('url', ''),
                        'location': item.get('location', 'Remote'),
                        'date_posted': item.get('date', 'Recent'),
                        'fit_score': 0,
                        'company_stage': 'Series A-C',
                        'GTM_maturity_signal': 'Building GTM function',
                        'outreach_angle': ''
                    }

                    job['fit_score'] = calculate_fit_score(job)
                    job['outreach_angle'] = determine_outreach_angle(job)

                    if job['fit_score'] >= 3:
                        results.append(job)
                        print(f"  ✓ Found: {job['job_title']}")

        except Exception as e:
            print(f"  ✗ Error searching GTM roles: {str(e)}")

    return results


def deduplicate_results(jobs: List[Dict]) -> List[Dict]:
    """Remove duplicate job postings based on company + title"""
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
    """Main execution function"""
    print("Starting Executive Roles Search - Three Track Analysis")
    print("=" * 70)

    all_jobs = []

    # Track 1: Tech Giants
    tech_giant_jobs = search_tech_giants()
    all_jobs.extend(tech_giant_jobs)
    print(f"\nTrack 1 Results: {len(tech_giant_jobs)} jobs")

    # Track 2: Ex-Founder Roles
    ex_founder_jobs = search_ex_founder_roles()
    all_jobs.extend(ex_founder_jobs)
    print(f"\nTrack 2 Results: {len(ex_founder_jobs)} jobs")

    # Track 3: GTM Leadership
    gtm_jobs = search_gtm_leadership()
    all_jobs.extend(gtm_jobs)
    print(f"\nTrack 3 Results: {len(gtm_jobs)} jobs")

    # Deduplicate and sort by fit score
    unique_jobs = deduplicate_results(all_jobs)
    sorted_jobs = sorted(unique_jobs, key=lambda x: x['fit_score'], reverse=True)

    # Save to CSV
    save_to_csv(sorted_jobs, OUTPUT_FILE)

    # Summary
    print("\n" + "=" * 70)
    print("SEARCH SUMMARY")
    print("=" * 70)
    print(f"Total unique jobs found: {len(sorted_jobs)}")
    print(f"\nFit Score Distribution:")
    for score in [5, 4, 3, 2, 1]:
        count = sum(1 for j in sorted_jobs if j['fit_score'] == score)
        print(f"  Score {score}: {count} jobs")

    print(f"\nTop 5 Best Fits:")
    for i, job in enumerate(sorted_jobs[:5], 1):
        print(f"\n{i}. {job['job_title']} at {job['company_name']}")
        print(f"   Score: {job['fit_score']} | {job['location']}")
        print(f"   {job['job_url']}")


if __name__ == '__main__':
    main()
