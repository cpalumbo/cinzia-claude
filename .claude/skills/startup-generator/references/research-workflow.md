# Research Workflow

Detailed protocols for conducting startup market research.

## Research Stream 1: Recently Funded Startups

### Search Queries Template

Replace `[VERTICAL]` with the target vertical:

```
Primary queries:
- "[VERTICAL] startup seed funding 2024"
- "[VERTICAL] startup series A 2025"
- "[VERTICAL] YC batch"
- "[VERTICAL] startup raised"
- "emerging [VERTICAL] startups to watch"

Secondary queries:
- "[VERTICAL] startup acquisition"
- "[VERTICAL] unicorn startup"
- "top [VERTICAL] startups investors"
- "[VERTICAL] startup landscape"
```

### Data Extraction Template

For each relevant startup found, capture:

```markdown
### [Startup Name]
- **One-liner:** [What they do in one sentence]
- **Founded:** [Year]
- **Funding:** [Total raised, last round amount, round type]
- **Investors:** [Notable investors]
- **Problem:** [What problem they solve]
- **Solution:** [How they solve it]
- **Business Model:** [How they make money]
- **Traction:** [Users, revenue, growth if available]
- **Why interesting:** [What makes this notable for our research]
- **Source:** [URL]
```

### Key Sources

| Source | What to Find | Tool to Use |
|--------|--------------|-------------|
| YC Directory | YC companies by vertical | **web-scraper** → CSV of companies |
| Crunchbase | Funding data, rounds | **web-scraper** → CSV of funding |
| TechCrunch | Funding announcements | `web_search` + `web_fetch` for articles |
| Product Hunt | New launches | **web-scraper** → CSV of products |
| CB Insights | Market maps | `web_search` + `web_fetch` |
| PitchBook (limited) | Funding data | `web_search` for reported deals |

### Web-Scraper Tasks for This Stream

**Task 1: YC Company Directory**
```
Use web-scraper to:
- Target: YC company directory filtered by [vertical]
- Columns: company_name, one_liner, website, batch, status
- Rows: Up to 50 relevant companies
- Objective: Identify funded startups in this space
```

**Task 2: Recent Funding Rounds**
```
Use web-scraper to:
- Target: Search for "[vertical] startup funding 2024 2025"
- Columns: company, funding_amount, round_type, date, lead_investor, source_url
- Rows: 20-30 recent deals
- Objective: Map funding activity and investor interest
```

**Task 3: Product Hunt Launches**
```
Use web-scraper to:
- Target: Product Hunt search for [vertical]
- Columns: product_name, tagline, url, upvotes, launch_date
- Rows: 20 most recent/popular
- Objective: Identify new entrants and positioning
```

### Analysis Questions

After collecting 10-15 funded startups:

1. **Pattern Recognition**
   - What problems are multiple startups attacking?
   - What business models are most common?
   - What customer segments are targeted?

2. **Gap Analysis**
   - What adjacent problems aren't being addressed?
   - What customer segments are underserved?
   - Where are existing solutions weak?

3. **Signal Extraction**
   - What are investors betting on?
   - What's the average funding size? (indicates capital intensity)
   - What's the typical go-to-market?

---

## Research Stream 2: Technology Signals

### Search Queries Template

```
Research/Academic:
- "[VERTICAL] AI machine learning applications"
- "[VERTICAL] arxiv paper 2024"
- "[VERTICAL] research breakthrough"
- "[VERTICAL] new algorithm"

Infrastructure/Platforms:
- "[VERTICAL] API launch"
- "[VERTICAL] platform developer"
- "[VERTICAL] open source github"
- "new [VERTICAL] tools developers"

Cost/Capability Changes:
- "[VERTICAL] cost reduction technology"
- "[VERTICAL] automation"
- "LLM [VERTICAL] applications"
- "what's newly possible [VERTICAL]"
```

### Technology Signal Categories

#### 1. AI/ML Enablement
- New models applicable to the vertical
- Fine-tuned models for specific tasks
- Cost reductions in inference
- New capabilities (multimodal, reasoning, etc.)

#### 2. Infrastructure Changes
- New APIs making things easier
- Cloud services reducing build complexity
- Open source projects lowering barriers
- Platforms enabling new applications

#### 3. Cost Curves
- What was expensive that's now cheap?
- What required specialists that's now accessible?
- What took months that now takes days?

#### 4. Data Availability
- New datasets becoming available
- Data sharing regulations changing
- Synthetic data capabilities
- Real-time data access

### Signal Evaluation

For each technology signal, assess:

| Question | Answer |
|----------|--------|
| What's newly possible? | |
| Who benefits most? | |
| What startups could be built on this? | |
| How durable is this advantage? | |
| What's the timing? (ready now vs. 2-3 years) | |

### Web-Scraper Tasks for This Stream

**Task: GitHub Trending in Vertical**
```
Use web-scraper to:
- Target: GitHub trending repos related to [vertical]
- Columns: repo_name, description, stars, language, url
- Rows: 20 trending repos
- Objective: Identify emerging open-source tools and technologies
```

**Task: Recent Papers/Research**
```
Use web-scraper to:
- Target: arXiv or Google Scholar search for [vertical] + [technology]
- Columns: title, authors, date, abstract_snippet, url
- Rows: 15-20 recent papers
- Objective: Spot research breakthroughs with commercial potential
```

---

## Research Stream 3: Market Trends

### Search Queries Template

```
Market Size/Growth:
- "[VERTICAL] market size 2025"
- "[VERTICAL] industry growth rate"
- "[VERTICAL] TAM SAM SOM"
- "[VERTICAL] market forecast"

Trends/Shifts:
- "[VERTICAL] industry trends 2025"
- "[VERTICAL] consumer behavior change"
- "[VERTICAL] digital transformation"
- "future of [VERTICAL]"

Regulatory/External:
- "[VERTICAL] regulation changes"
- "[VERTICAL] policy impact"
- "[VERTICAL] compliance requirements"
- "[VERTICAL] government initiative"
```

### Trend Categories

#### 1. Demand Trends
- Growing customer segments
- Changing buyer behavior
- New use cases emerging
- Price sensitivity shifts

#### 2. Supply Trends
- New competitors entering
- Incumbents struggling/adapting
- Consolidation happening
- New business models emerging

#### 3. Regulatory Trends
- New regulations creating opportunity
- Compliance burdens creating software needs
- Deregulation opening markets
- Government incentives/funding

#### 4. Social/Behavioral Trends
- Generational shifts
- Work pattern changes
- Privacy/security concerns
- Sustainability demands

### "Why Now" Framework

For each trend, articulate:

```markdown
**Trend:** [Description]

**What changed:**
- [Specific change or event]

**Why this creates opportunity:**
- [How this enables new startups]

**Timing evidence:**
- [Data showing this is happening now]

**Who wins:**
- [Customer segments that benefit]
- [Startup types that can capitalize]
```

---

## Research Synthesis

### Opportunity Matrix

After completing all research streams, create synthesis:

| Opportunity | Funded Startup Signal | Tech Signal | Market Trend | Team Fit |
|-------------|----------------------|-------------|--------------|----------|
| [Opp 1] | [Related startups] | [Enabling tech] | [Supporting trend] | [Fit score] |
| [Opp 2] | ... | ... | ... | ... |

### Prioritization Criteria

Rank opportunities by:

1. **Signal Strength** (multiple data points supporting)
2. **Timing** (why now is the right time)
3. **Team Fit** (matches team strengths)
4. **Defensibility** (potential for moat)
5. **Market Size** (big enough to matter)

### Research Quality Checklist

- [ ] 10+ funded startups analyzed
- [ ] 5+ technology signals identified
- [ ] 3+ market trends documented
- [ ] "Why now" articulated for top opportunities
- [ ] Gaps and underserved areas identified
- [ ] All sources documented with URLs

---

## Tool Selection Guide

Choose the right tool for each research task:

```
┌─────────────────────────────────────────────────────────────────┐
│  Need structured data (tables, lists, directories)?            │
│  YES → Use web-scraper → Outputs CSV                           │
│  NO  ↓                                                         │
├─────────────────────────────────────────────────────────────────┤
│  Need to read a specific article/page in depth?                │
│  YES → Use web_fetch → Returns full content                    │
│  NO  ↓                                                         │
├─────────────────────────────────────────────────────────────────┤
│  Need quick facts or to find URLs?                             │
│  YES → Use web_search → Returns snippets + links               │
│  NO  ↓                                                         │
├─────────────────────────────────────────────────────────────────┤
│  Need to interact with a page (click, scroll, login)?          │
│  YES → Use browser tools → Full page control                   │
└─────────────────────────────────────────────────────────────────┘
```

### Combining Tools Effectively

**Pattern: Discovery → Scrape → Deep-dive**

1. `web_search` to find relevant sources/URLs
2. `web-scraper` to extract structured data into CSV
3. `web_fetch` to read detailed pages for top results

**Example workflow for funding research:**
```
1. web_search: "[vertical] startup funding 2024" → find sources
2. web-scraper: Scrape YC directory → companies.csv
3. web-scraper: Scrape funding news → funding_rounds.csv  
4. web_fetch: Read top 5 company "About" pages for deeper context
5. Synthesize findings into opportunity analysis
```
