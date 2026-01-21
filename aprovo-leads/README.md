# Aprovo Lead Generation - Barcelona Dental Clinics

## Overview

This project scrapes and qualifies dental clinics in Barcelona, Spain for Aprovo's conversion optimization platform. The goal is to identify 100-200 qualified leads that match Aprovo's Ideal Customer Profile (ICP).

## Methodology

### 1. Data Sources

- **Seed List**: 220+ verified Barcelona dental clinic URLs
- **Sources**: Dental directories, Google Maps, Invisalign provider directory
- **Focus**: Independent clinics and small DSOs in Barcelona area

### 2. ICP Scoring Model

Each clinic is scored based on two main categories:

#### Digital Savviness (adoption readiness)
- Modern website (+10 points)
- Online booking system (+15 points)
- Instagram presence (+5-10 points based on followers)
- WhatsApp Business (+5 points)
- Google My Business 50+ reviews (+5 points)

#### High-Ticket Focus (deal size indicators)
- Mentions implants (+10 points)
- Mentions Invisalign/orthodontics (+15 points)
- Mentions carillas/estética (+10 points)
- Before/after gallery (+5 points)
- Financing options (+10 points)

#### Bonus & Penalties
- Multiple locations (+10 points)
- No website (-50 points)
- Dated website (-20 points)
- Only general dentistry (-20 points)

**Qualification Threshold**: 60+ points

### 3. Data Collection

For each clinic, we collect:

- **Basic Info**: Name, website, city, phone, email
- **Digital Presence**: Instagram handle, Google ratings/reviews
- **ICP Signals**: All scoring criteria (booking, WhatsApp, treatments, etc.)
- **Score**: Calculated ICP score (0-100)

### 4. Quality Standards

- UTF-8 encoded CSV
- Deduplicated by website domain and phone number
- Empty values = empty string (not "N/A")
- All boolean fields as True/False
- Spanish phone format: +34 XXX XXX XXX

## Files

### Output Files

1. **aprovo_leads_barcelona_YYYY-MM-DD.csv**
   - Qualified leads only (score >= 60)
   - Sorted by ICP score (highest first)
   - Ready for outreach

2. **aprovo_leads_barcelona_full_YYYY-MM-DD.csv**
   - All scraped clinics (including non-qualified)
   - For reference and future re-scoring

### Scripts

1. **barcelona_scraper.py** - Initial scraper (39 clinics)
2. **expanded_scraper.py** - Expanded version (67 clinics)
3. **comprehensive_scraper.py** - Final version (220+ clinics)

## CSV Columns

```
clinic_name              Official clinic name
website_url              Main website domain
city                     Barcelona
phone                    Primary contact number
email                    Contact email if available
google_rating            1-5 stars (0 if unknown)
google_review_count      Number of Google reviews
instagram_handle         @username if found
instagram_followers      Follower count (0 if unknown)
has_online_booking       True/False
has_whatsapp             True/False
has_financing            True/False
mentions_implants        True/False
mentions_invisalign      True/False
mentions_carillas        True/False
has_gallery              True/False (before/after photos)
website_quality          modern/dated/none
multi_location           True/False
icp_score                0-100 (qualification score)
notes                    Scraping metadata
```

## Usage

### Running the Scraper

```bash
cd aprovo-leads
source venv/bin/activate
python3 comprehensive_scraper.py
```

### Filtering Results

The scraper automatically filters to qualified leads (score >= 60), but you can adjust the threshold by modifying `min_score` parameter.

## Red Flags (Auto-Excluded)

- Large DSO chains (Sanitas, Vitaldent, etc.)
- Impress clinics (competitor)
- Broken/non-existent websites
- Only general dentistry focus

## Results Summary

Target: 100-200 qualified leads
Processed: 220+ Barcelona dental clinic URLs
Qualified: [To be updated after scraping completes]

### Score Distribution
- 90+ points: Premium leads (strong ICP fit)
- 80-89 points: High-quality leads
- 70-79 points: Good leads
- 60-69 points: Qualified leads

## Next Steps

1. Review top-scoring leads manually
2. Enrich with Doctoralia data (optional)
3. Verify phone numbers and emails
4. Prioritize outreach by ICP score
5. Customize messaging based on signals (e.g., Invisalign mention)

## Notes

- Scraping respects rate limits (0.5-2 sec delays)
- Some clinic URLs may fail (domain issues, SSL errors, timeouts)
- Instagram follower counts require manual verification
- Google review counts would need Maps API for accuracy
