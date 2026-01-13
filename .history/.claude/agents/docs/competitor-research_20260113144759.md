# Competitor Research

Reference guide for researching competitors and building competitive analysis datasets.

## What to Capture

### Market Information and Context
- Market and product category to research
- Ask users for definitions and examples of competitors
- Context: ask the user why they're interested in researching this market and product category

### Company Basics
- company_name
- website_url
- linkedin-url
- founding_year
- headquarters_location
- employee_count (or range: 1-10, 11-50, 51-200, etc.)
- no. of open jobs

### Product & Positioning
- Homepage tagline (one-liner from their homepage metadescrition, hero section)
- LinkedIn tagline (as per LinkedIn company page)
- product_description (2-3 sentences max)
- target_audience
- target_use_cases
- key_features (top 3-5, comma-separated)
- pricing_model (freemium, subscription, one-time, usage-based, contact-sales)
- starting_price (lowest tier, or "Contact sales")

### Business Signals
- funding_stage (bootstrapped, seed, series-a, series-b, etc.)
- total_funding (if public)
- last_funding_date
- notable_investors
- growth signals (recent funding news, high number of job vacancies, high-profile hires, M&A activity)

### Tech Stack (if relevant)
- built_with (languages, frameworks if detectable)
- integrations (what tools they connect with)

## Best Sources

| Source | Best for |
|--------|----------|
| Company website | Tagline, features, pricing |
| LinkedIn | Employee count, headquarters, company description |
| Crunchbase | Funding, founding year, investors |
| G2/Capterra | User reviews, feature lists, pricing |
| BuiltWith/Wappalyzer | Tech stack |
| Twitter/blog | Recent news, positioning changes |

## Research Workflow

1. Start with direct competitor websites
2. Cross-reference with Crunchbase/LinkedIn for business data
3. Check G2/Capterra for market perception
4. Note pricing page structure (transparent vs. contact sales)
5. Capture screenshots of pricing pages (they change often)

## Output Formats

### Quick Comparison (5-10 competitors)
```
company_name, website, tagline, starting_price, pricing_model
```

### Full Analysis (3-5 competitors)
```
company_name, website, tagline, target_audience, key_features, starting_price, pricing_model, employee_count, funding_stage, total_funding
```

### Feature Matrix
```
feature_name, our_product, competitor_1, competitor_2, competitor_3
```
Values: yes, no, partial, unknown

## Quality Checks

- Verify pricing is current (check page date or wayback machine)
- Employee counts vary by source—note where you got it
- "Contact sales" is valid pricing data—don't leave blank
- Flag anything over 6 months old as potentially stale
