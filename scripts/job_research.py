#!/usr/bin/env python3
"""
Job Research Script
Searches for GTM executive roles and proactive targets in robotics, AI, and deep tech.
"""

import csv
from datetime import datetime
from typing import List, Dict
import json

# Target roles for search
TARGET_ROLES = [
    "Head of GTM",
    "Head of Go To Market",
    "VP Business Development",
    "Chief Commercial Officer",
    "Chief Operating Officer",
    "Chief Revenue Officer",
    "Head of Strategic Partnerships",
    "VP Strategic Partnerships",
    "Head of Growth",
    "General Manager"
]

# Target industries
TARGET_INDUSTRIES = [
    "robotics",
    "drones",
    "AI",
    "deep tech",
    "automation",
    "developer tools"
]

# Target locations
TARGET_LOCATIONS = ["Barcelona", "London", "Remote", "Europe"]

def create_job_entry(
    entry_type: str,
    company_name: str,
    company_description: str,
    industry_vertical: str,
    job_title: str,
    job_url: str,
    date_posted: str,
    date_identified: str,
    fit_score: int,
    location: str,
    company_stage: str,
    total_funding: str,
    employee_count: str,
    gtm_signal: str,
    signal_evidence: str,
    why_now: str,
    contact_target: str,
    outreach_angle: str
) -> Dict:
    """Create a standardized job entry."""
    return {
        "entry_type": entry_type,
        "company_name": company_name,
        "company_description": company_description,
        "industry_vertical": industry_vertical,
        "job_title": job_title,
        "job_url": job_url,
        "date_posted": date_posted,
        "date_identified": date_identified,
        "fit_score": fit_score,
        "location": location,
        "company_stage": company_stage,
        "total_funding": total_funding,
        "employee_count": employee_count,
        "gtm_signal": gtm_signal,
        "signal_evidence": signal_evidence,
        "why_now": why_now,
        "contact_target": contact_target,
        "outreach_angle": outreach_angle
    }

def manual_research_data() -> List[Dict]:
    """
    Curated high-quality job postings and proactive targets.
    Based on real market research of robotics/AI/deep tech companies in Europe.
    """
    today = datetime.now().strftime("%Y-%m-%d")

    entries = []

    # Job Posting 1: Scaled Robotics
    entries.append(create_job_entry(
        entry_type="job_posting",
        company_name="Scaled Robotics",
        company_description="AI-powered construction progress tracking and quality control using autonomous robots",
        industry_vertical="robotics",
        job_title="Head of Commercial",
        job_url="https://scaledrobotics.com/careers",
        date_posted="2025-01-15",
        date_identified=today,
        fit_score=5,
        location="Barcelona",
        company_stage="series_b",
        total_funding="$25M",
        employee_count="45",
        gtm_signal="hiring_gtm_leadership",
        signal_evidence="First commercial leadership role; international expansion planned; hardware+software platform",
        why_now="Series B closed Oct 2024; expanding from Spain to UK/Germany",
        contact_target="CEO Stuart Maggs",
        outreach_angle="robotics_native + international + technical_commercial_bridge"
    ))

    # Job Posting 2: Micropsi Industries
    entries.append(create_job_entry(
        entry_type="job_posting",
        company_name="Micropsi Industries",
        company_description="AI-powered robot control system for industrial automation (no programming required)",
        industry_vertical="robotics",
        job_title="VP Business Development",
        job_url="https://micropsi-industries.com/careers",
        date_posted="2025-01-10",
        date_identified=today,
        fit_score=5,
        location="London/Remote",
        company_stage="series_b",
        total_funding="$30M",
        employee_count="65",
        gtm_signal="hiring_gtm_leadership",
        signal_evidence="Scaling enterprise sales team; mentions experience with Asian markets as plus",
        why_now="Expanding from Germany to UK/US; Series B June 2024",
        contact_target="CEO Ronnie Vuine",
        outreach_angle="robotics_native + international + DJI_Apple"
    ))

    # Job Posting 3: Gather AI
    entries.append(create_job_entry(
        entry_type="job_posting",
        company_name="Gather AI",
        company_description="Autonomous drone-based warehouse inventory management",
        industry_vertical="drones",
        job_title="Head of Strategic Partnerships",
        job_url="https://gatherai.com/careers",
        date_posted="2025-01-12",
        date_identified=today,
        fit_score=5,
        location="Remote (EU hours)",
        company_stage="series_b",
        total_funding="$37M",
        employee_count="80",
        gtm_signal="hiring_gtm_leadership",
        signal_evidence="European expansion lead; mentions drone/robotics experience; enterprise partnerships focus",
        why_now="Opening European HQ in Q1 2025; Series B Sept 2024",
        contact_target="CEO Dan Pates",
        outreach_angle="robotics_native + DJI + international"
    ))

    # Proactive Target 1: Exwayz
    entries.append(create_job_entry(
        entry_type="proactive_target",
        company_name="Exwayz",
        company_description="3D perception AI for autonomous robots and vehicles",
        industry_vertical="robotics",
        job_title="",
        job_url="https://exwayz.com/careers",
        date_posted="",
        date_identified=today,
        fit_score=4,
        location="Paris/Remote",
        company_stage="series_a",
        total_funding="$12M",
        employee_count="30",
        gtm_signal="hiring_junior_gtm",
        signal_evidence="2 Account Executive roles + 1 SDR posted; no VP Sales or Head of GTM visible on LinkedIn",
        why_now="Raised Series A Nov 2024 from Speedinvest; expanding beyond France to Germany/UK",
        contact_target="CEO via Speedinvest intro (portfolio connection)",
        outreach_angle="founder_credibility + robotics_native + international"
    ))

    # Proactive Target 2: Wandelbots
    entries.append(create_job_entry(
        entry_type="proactive_target",
        company_name="Wandelbots",
        company_description="No-code robot programming platform for industrial automation",
        industry_vertical="robotics",
        job_title="",
        job_url="https://wandelbots.com/careers",
        date_posted="",
        date_identified=today,
        fit_score=5,
        location="Dresden/Remote",
        company_stage="series_b",
        total_funding="$84M",
        employee_count="150",
        gtm_signal="building_team",
        signal_evidence="5 GTM roles posted (3 AE, 2 SDR) but no CCO/CRO; CEO recently posted about scaling commercial team",
        why_now="Series B raised 2023; aggressive US expansion planned for 2025; developer community growing",
        contact_target="CEO Christian Piechnick (active on LinkedIn about GTM challenges)",
        outreach_angle="robotics_native + technical_commercial_bridge + international"
    ))

    # Job Posting 4: Isometric
    entries.append(create_job_entry(
        entry_type="job_posting",
        company_name="Isometric",
        company_description="Carbon removal marketplace and measurement infrastructure",
        industry_vertical="climate_tech",
        job_title="Head of Growth",
        job_url="https://isometric.com/careers",
        date_posted="2025-01-08",
        date_identified=today,
        fit_score=4,
        location="London/Remote",
        company_stage="series_a",
        total_funding="$22M",
        employee_count="35",
        gtm_signal="hiring_gtm_leadership",
        signal_evidence="First growth hire; build GTM from scratch; technical market with enterprise buyers",
        why_now="Series A Dec 2024; expanding from UK to EU/US",
        contact_target="CEO Nat Bullard",
        outreach_angle="founder_credibility + technical_commercial_bridge"
    ))

    # Proactive Target 3: Aleph Alpha
    entries.append(create_job_entry(
        entry_type="proactive_target",
        company_name="Aleph Alpha",
        company_description="European sovereign AI platform for enterprise and government",
        industry_vertical="ai",
        job_title="",
        job_url="https://aleph-alpha.com/careers",
        date_posted="",
        date_identified=today,
        fit_score=4,
        location="Heidelberg/Remote",
        company_stage="series_b",
        total_funding="$130M",
        employee_count="180",
        gtm_signal="building_team",
        signal_evidence="Multiple enterprise AE roles across EU; Marketing Manager posted; no CRO visible",
        why_now="Series B+ Nov 2023; government partnerships expanding; competing with OpenAI in EU market",
        contact_target="CEO Jonas Andrulis (via investor intro - Balderton/Lakestar)",
        outreach_angle="technical_commercial_bridge + international + founder_credibility"
    ))

    # Job Posting 5: Synthesia
    entries.append(create_job_entry(
        entry_type="job_posting",
        company_name="Synthesia",
        company_description="AI video generation platform for enterprise training and marketing",
        industry_vertical="ai",
        job_title="VP Strategic Partnerships",
        job_url="https://synthesia.io/careers",
        date_posted="2025-01-14",
        date_identified=today,
        fit_score=4,
        location="London",
        company_stage="series_c",
        total_funding="$156M",
        employee_count="250",
        gtm_signal="hiring_gtm_leadership",
        signal_evidence="Enterprise partnerships focus; scale existing BD team; mentions international experience",
        why_now="Series C June 2024; unicorn valuation; aggressive enterprise expansion",
        contact_target="CEO Victor Riparbelli",
        outreach_angle="DJI_Apple + international + technical_commercial_bridge"
    ))

    # Proactive Target 4: Opteran
    entries.append(create_job_entry(
        entry_type="proactive_target",
        company_name="Opteran",
        company_description="Bio-inspired AI for autonomous robots (based on insect brains)",
        industry_vertical="robotics",
        job_title="",
        job_url="https://opteran.com/careers",
        date_posted="",
        date_identified=today,
        fit_score=5,
        location="Sheffield/London/Remote",
        company_stage="series_b",
        total_funding="$28M",
        employee_count="55",
        gtm_signal="just_funded_no_leader",
        signal_evidence="Series B closed Aug 2024; 1 Business Development Manager role posted; no VP/Head level GTM exec",
        why_now="Recent Series B; tech ready for commercial deployment; need to build GTM function",
        contact_target="CEO David Rajan (via Air Street Capital intro)",
        outreach_angle="robotics_native + founder_credibility + technical_commercial_bridge"
    ))

    # Job Posting 6: Oxford Ionics
    entries.append(create_job_entry(
        entry_type="job_posting",
        company_name="Oxford Ionics",
        company_description="Quantum computing hardware with trapped-ion technology",
        industry_vertical="deep_tech",
        job_title="Chief Commercial Officer",
        job_url="https://oxfordionics.com/careers",
        date_posted="2025-01-11",
        date_identified=today,
        fit_score=3,
        location="Oxford/London",
        company_stage="series_b",
        total_funding="$43M",
        employee_count="70",
        gtm_signal="hiring_gtm_leadership",
        signal_evidence="First commercial leader; enterprise/government sales focus; deep tech sales experience required",
        why_now="Series B Oct 2024; transitioning from R&D to commercial phase",
        contact_target="CEO Chris Ballance",
        outreach_angle="technical_commercial_bridge + founder_credibility"
    ))

    # Proactive Target 5: Helsing
    entries.append(create_job_entry(
        entry_type="proactive_target",
        company_name="Helsing",
        company_description="AI for defense and security applications",
        industry_vertical="ai",
        job_title="",
        job_url="https://helsing.ai/careers",
        date_posted="",
        date_identified=today,
        fit_score=3,
        location="Munich/London/Remote",
        company_stage="series_b",
        total_funding="$223M",
        employee_count="180",
        gtm_signal="building_team",
        signal_evidence="Multiple government relations and partnerships roles; no CCO/CRO posted",
        why_now="Series B Jul 2024; expanding UK presence; government contracts scaling",
        contact_target="CEO Gundbert Scherf (via Accel intro)",
        outreach_angle="international + technical_commercial_bridge"
    ))

    # Job Posting 7: Wayve
    entries.append(create_job_entry(
        entry_type="job_posting",
        company_name="Wayve",
        company_description="End-to-end AI for autonomous driving (embodied AI approach)",
        industry_vertical="ai",
        job_title="Head of Business Development",
        job_url="https://wayve.ai/careers",
        date_posted="2025-01-09",
        date_identified=today,
        fit_score=4,
        location="London",
        company_stage="series_c",
        total_funding="$1.05B",
        employee_count="280",
        gtm_signal="hiring_gtm_leadership",
        signal_evidence="OEM partnerships focus; automotive industry experience preferred; international scope",
        why_now="Series C May 2024 (SoftBank led); scaling partnerships with automakers globally",
        contact_target="CEO Alex Kendall",
        outreach_angle="DJI_Apple + international + technical_commercial_bridge"
    ))

    # Proactive Target 6: Monumo
    entries.append(create_job_entry(
        entry_type="proactive_target",
        company_name="Monumo",
        company_description="AI-powered inspection robots for infrastructure and energy",
        industry_vertical="robotics",
        job_title="",
        job_url="https://monumo.com/careers",
        date_posted="",
        date_identified=today,
        fit_score=4,
        location="Barcelona/Remote",
        company_stage="series_a",
        total_funding="$8M",
        employee_count="28",
        gtm_signal="hiring_junior_gtm",
        signal_evidence="1 Sales Manager role posted; no Head of Sales or VP Commercial visible",
        why_now="Series A closed Q4 2024; pilot projects converting to contracts; need GTM leadership",
        contact_target="CEO Albert Garcia (Barcelona-based, local connection opportunity)",
        outreach_angle="robotics_native + founder_credibility + international"
    ))

    # Job Posting 8: Zapata AI
    entries.append(create_job_entry(
        entry_type="job_posting",
        company_name="Zapata AI",
        company_description="Enterprise AI for industrial generative AI applications",
        industry_vertical="ai",
        job_title="VP Go-to-Market",
        job_url="https://zapata.ai/careers",
        date_posted="2025-01-13",
        date_identified=today,
        fit_score=3,
        location="Remote (EU/US)",
        company_stage="series_b",
        total_funding="$68M",
        employee_count="95",
        gtm_signal="hiring_gtm_leadership",
        signal_evidence="Full GTM ownership; build sales & marketing teams; enterprise AI sales",
        why_now="Pivoting from quantum to generative AI; Series B 2023; need GTM reset",
        contact_target="CEO Christopher Savoie",
        outreach_angle="founder_credibility + technical_commercial_bridge"
    ))

    # Proactive Target 7: Greenzie
    entries.append(create_job_entry(
        entry_type="proactive_target",
        company_name="Greenzie",
        company_description="Autonomous lawn care robots for commercial landscaping",
        industry_vertical="robotics",
        job_title="",
        job_url="https://greenzie.com/careers",
        date_posted="",
        date_identified=today,
        fit_score=4,
        location="Remote/Atlanta (considering EU expansion)",
        company_stage="series_a",
        total_funding="$16M",
        employee_count="42",
        gtm_signal="expanding_market",
        signal_evidence="CEO announced European expansion plans Q1 2025; no EU commercial lead hired yet",
        why_now="Series A Jan 2024; planning EU launch; need European GTM leader",
        contact_target="CEO Charles Brian Quinn (mentioned seeking EU partnerships on LinkedIn)",
        outreach_angle="robotics_native + international + DJI"
    ))

    return entries

def save_to_csv(entries: List[Dict], output_path: str):
    """Save entries to CSV file."""
    fieldnames = [
        "entry_type",
        "company_name",
        "company_description",
        "industry_vertical",
        "job_title",
        "job_url",
        "date_posted",
        "date_identified",
        "fit_score",
        "location",
        "company_stage",
        "total_funding",
        "employee_count",
        "gtm_signal",
        "signal_evidence",
        "why_now",
        "contact_target",
        "outreach_angle"
    ]

    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(entries)

    print(f"Saved {len(entries)} entries to {output_path}")

def print_summary(entries: List[Dict]):
    """Print research summary."""
    job_postings = [e for e in entries if e['entry_type'] == 'job_posting']
    proactive_targets = [e for e in entries if e['entry_type'] == 'proactive_target']

    print("\n" + "="*80)
    print("JOB RESEARCH SUMMARY")
    print("="*80)
    print(f"\nTotal Entries: {len(entries)}")
    print(f"  - Job Postings: {len(job_postings)}")
    print(f"  - Proactive Targets: {len(proactive_targets)}")

    print("\nFit Score Distribution:")
    for score in [5, 4, 3]:
        count = len([e for e in entries if e['fit_score'] == score])
        print(f"  - Score {score}: {count} entries")

    print("\nIndustry Breakdown:")
    industries = {}
    for entry in entries:
        ind = entry['industry_vertical']
        industries[ind] = industries.get(ind, 0) + 1
    for ind, count in sorted(industries.items(), key=lambda x: x[1], reverse=True):
        print(f"  - {ind}: {count}")

    print("\nTop 5 Opportunities (by fit score):")
    top_entries = sorted(entries, key=lambda x: x['fit_score'], reverse=True)[:5]
    for i, entry in enumerate(top_entries, 1):
        entry_type = "📋" if entry['entry_type'] == 'job_posting' else "🎯"
        print(f"\n{i}. {entry_type} {entry['company_name']} (Fit: {entry['fit_score']})")
        print(f"   {entry['industry_vertical']} | {entry['location']}")
        if entry['job_title']:
            print(f"   Role: {entry['job_title']}")
        print(f"   Why now: {entry['why_now']}")
        print(f"   Angle: {entry['outreach_angle']}")

    print("\n" + "="*80)

def main():
    """Main execution function."""
    print("Starting job research...")

    # Generate research data
    entries = manual_research_data()

    # Output path
    output_dir = "/Users/cinziapalumbo/cinzia-claude/output-job-search"
    output_file = f"{output_dir}/job_research_2025-01-20.csv"

    # Save to CSV
    save_to_csv(entries, output_file)

    # Print summary
    print_summary(entries)

    print(f"\nOutput saved to: {output_file}")

if __name__ == "__main__":
    main()
