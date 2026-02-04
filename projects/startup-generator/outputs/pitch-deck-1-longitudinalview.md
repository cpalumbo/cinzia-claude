# LongitudinalView
## AI-Powered Longitudinal Imaging Comparison for Preventive Care

---

## The Problem

**Preventive imaging is interpreted in isolation, not longitudinally.**

Every year, millions of Europeans undergo routine preventive screenings:
- Mammographies
- Abdominal ultrasounds
- Skin lesion imaging
- Eye exams
- Chest X-rays

**The critical issue:** When you get your results, the radiologist compares them to... nothing. Or to a vague reference in a paper report from 3 years ago at a different clinic.

### Real Patient Journey Today

```
2018: Mammography at Clinic A → Paper report filed
2020: Mammography at Clinic B → No access to 2018 images
2022: Mammography at Clinic C → "Cannot compare, no priors available"
2024: Suspicious finding → "We need your prior images"
      Patient: "I don't have them"
```

**Subtle but important changes across years are often missed because:**
- Prior exams are fragmented across clinics
- Too time-consuming to manually compare
- Different formats, different systems
- Patients don't maintain their own imaging records

### The Cost

- **Delayed detection** of slowly progressing conditions
- **Unnecessary repeat imaging** when priors unavailable
- **Cognitive overload** for radiologists doing manual comparisons
- **Liability risk** when changes are missed

---

## The Solution

**LongitudinalView** is a B2B software layer for diagnostic imaging clinics that:

1. **Ingests** prior reports and images from any source (DICOM, PDFs, photos of reports)
2. **Structures** them into a unified patient timeline
3. **Automatically produces** a longitudinal comparison brief for each new exam

### What We Do

```
New mammography scan arrives
         ↓
LongitudinalView automatically:
├── Finds patient's prior imaging (any clinic, any format)
├── Aligns and compares the images
├── Generates comparison brief:
│   ├── "3mm nodule in right breast - UNCHANGED from 2022"
│   ├── "Calcification pattern - NEW since last exam"
│   └── "Breast density - DECREASED (previously heterogeneous)"
└── Presents to radiologist in their existing PACS workflow
```

### What We Don't Do

- We don't diagnose
- We don't advise patients
- We don't replace radiologists

**We augment the radiologist's workflow** by eliminating the manual work of finding, aligning, and comparing prior studies.

---

## Why Now

### 1. AI Image Analysis is Mature
- GE HealthCare acquired icometrix for brain MRI comparison
- Oxipit's ChestEye has CE certification for longitudinal X-ray comparison
- Google's MedGemma provides foundation for medical image understanding

### 2. Reimbursement Pathways Exist
- CPT-III codes 0865T/0866T active for volumetric brain analysis
- 30+ US insurers processing claims
- European value-based care moving same direction

### 3. icometrix Validates the Category, But Leaves a Gap
- icometrix = **brain only** (MS, dementia, Parkinson's)
- Oxipit = **chest X-ray only**
- **Nobody does multi-modality, multi-organ longitudinal comparison**

### 4. Patient Records Remain Fragmented
- FHIR improving EHR interoperability
- But imaging records still siloed
- Patients switch clinics, lose continuity

---

## Market Size

### Total Addressable Market (TAM)
- European radiology services: **€72B** (2024)
- Growing to **€193B** by 2032 (CAGR 13.1%)

### Serviceable Addressable Market (SAM)
- Radiology workflow software in Europe: **€5B**
- Longitudinal/comparative analysis segment: **€500M**

### Serviceable Obtainable Market (SOM)
- Year 5 target: 2,000 clinics × €20K/year = **€41M ARR**

### Bottom-Up Sizing

| Year | Clinics | Avg Monthly Reports | MRR | ARR |
|------|---------|---------------------|-----|-----|
| Y1 | 50 | 100 | €60K | €720K |
| Y2 | 200 | 150 | €200K | €2.4M |
| Y3 | 500 | 200 | €600K | €7.2M |
| Y5 | 2,000 | 300 | €3.4M | €41M |

**Pricing Model:**
- Base: €200/month platform fee
- Usage: €5 per longitudinal comparison report generated
- Average clinic: 200 reports/month = €1,200/month = €14.4K/year

---

## Business Model

### Revenue Streams

1. **Platform Subscription** (€200-500/month)
   - PACS integration
   - Patient timeline management
   - Basic comparison dashboards

2. **Per-Report Fee** (€5-10/report)
   - AI-generated longitudinal comparison briefs
   - Aligned prior/current image pairs
   - Change detection and quantification

3. **Premium Features** (€500+/month)
   - Multi-clinic network access
   - Patient-facing reports
   - API access for EMR integration

### Unit Economics (Target)

| Metric | Target |
|--------|--------|
| Monthly ARPU | €1,500 |
| CAC | €3,000 |
| Payback Period | 2 months |
| Gross Margin | 80%+ |
| Net Revenue Retention | 120%+ |

---

## Competition

### Competitive Landscape

| Company | Focus | Funding | Gap |
|---------|-------|---------|-----|
| **icometrix** (GE) | Brain MRI only | Acquired | No multi-organ |
| **Oxipit** | Chest X-ray only | €3M | No multi-organ |
| **Tempus Radiology** | Oncology | $1.1B+ total | US-focused, cancer-only |
| **Qure.ai** | X-ray triage | $90M | Acute care, not longitudinal |
| **Harrison.ai** | Radiology LLM | $129M | General AI, not comparison |

### Our Differentiation

1. **Multi-modality** - Mammography, ultrasound, X-ray, MRI in one platform
2. **Cross-clinic** - Patient-controlled record aggregation
3. **European focus** - GDPR-native, CE marking priority
4. **Workflow integration** - Works with existing PACS, not replacing it

---

## Traction / Validation

### Problem Validation
- Cinzia's personal experience: "All my imaging and diagnostics are left on paper. Rarely stored in one place throughout the years."
- icometrix's success proves radiologists pay for longitudinal comparison
- CPT code adoption proves payers reimburse for it

### Technical Validation
- Yerezhan built Impress's multi-clinic imaging and EMR system
- DICOM handling, cross-system integration = solved problems for this team
- 200+ clinics, 9 countries at Impress = relevant scale experience

### Next Validation Steps
1. LOIs from 5 diagnostic imaging clinics in Barcelona
2. Technical PoC with one partner clinic
3. CE marking pathway assessment

---

## Team

### Yerezhan Tashbenbetov - Co-founder, CPTO
**Built exactly this problem space at scale.**

- CTO & CPO at Impress for 5+ years
- Built full-stack clinic and patient platform from scratch
- Scaled to 200+ clinics across 9 countries
- Custom EMRs, intelligent scheduling, AI-driven treatment planning
- Navigated seed through Series B (>€300M raised)

**Why this matters:** Yerezhan has built healthcare workflow software that radiologists and clinicians actually use, at multi-country scale, with compliance across jurisdictions.

### Cinzia Palumbo - Co-founder, CRO/COO
**GTM leader who has scaled complex B2B deals.**

- Co-founder of Genie (raised $1.2M, 24 paying enterprise customers)
- Former Global Key Accounts Director at DJI (scaled Apple partnership to $46M/year)
- Experience with regulated industries and complex sales cycles
- Network in European VC ecosystem (Speedinvest, Expa backers)

**Why this matters:** Cinzia has sold complex technology to enterprises and knows how to navigate healthcare procurement.

### Why Us

| Dimension | Evidence |
|-----------|----------|
| Technical capability | Built clinic EMR + imaging workflows for 200+ clinics |
| Domain expertise | 5+ years in healthcare technology at Impress |
| Customer access | Network of European clinic operators |
| Relevant experience | DICOM, PACS integration, multi-country compliance |
| Passion for problem | Both in 40s with personal preventive health concerns |

---

## Financial Projections

### Revenue Forecast

| Year | Clinics | ARR | Revenue Growth |
|------|---------|-----|----------------|
| Y1 | 50 | €720K | - |
| Y2 | 200 | €2.4M | 233% |
| Y3 | 500 | €7.2M | 200% |
| Y4 | 1,200 | €20M | 178% |
| Y5 | 2,000 | €41M | 105% |

### Cost Structure (Y3)

| Category | Amount | % of Revenue |
|----------|--------|--------------|
| Engineering (10 FTE) | €1.5M | 21% |
| Sales & Marketing | €1.8M | 25% |
| Cloud Infrastructure | €360K | 5% |
| G&A | €720K | 10% |
| **Total OpEx** | €4.4M | 61% |
| **Gross Profit** | €5.76M | 80% |
| **EBITDA** | €2.8M | 39% |

### Path to Profitability
- Break-even at ~€3M ARR (Y2-Y3)
- Target 30%+ EBITDA margins at scale

---

## The Ask

### Seed Round: €1.5M

**Use of Funds:**

| Category | Amount | Purpose |
|----------|--------|---------|
| Product Development | €800K | MVP, PACS integrations, AI models |
| Regulatory (CE Mark) | €200K | Certification, clinical validation |
| Sales & Marketing | €300K | 50 pilot clinics |
| Operations | €200K | 18-month runway buffer |

**Milestones:**
- MVP with 3 PACS integrations
- CE Mark Class IIa submission
- 50 paying pilot clinics
- €500K ARR

### Why Now
- GE/icometrix acquisition proves strategic value
- Category timing is perfect
- Team is ready and available

---

## Exit Potential

### Acquisition Targets
- **GE HealthCare** - Already bought icometrix, would want multi-organ
- **Siemens Healthineers** - Major PACS player, missing AI comparison
- **Philips** - Healthcare imaging leader
- **Agfa** / **Sectra** - Top PACS vendors per KLAS rankings

### Comparable Transactions
- icometrix → GE HealthCare (undisclosed, est. €100-200M)
- Tempus radiology platform (part of $8.1B company)

### Strategic Value
- **Network effects** - Patient data becomes more valuable with scale
- **Regulatory moat** - CE marking creates barrier to entry
- **Workflow integration** - Switching costs once embedded in PACS

---

## Appendix: Research Summary

### Funded Competitors Analysis

| Company | Focus | Funding | Business Model |
|---------|-------|---------|----------------|
| icometrix | Brain MRI comparison | Acquired by GE | B2B per-scan + subscription |
| Oxipit | Chest X-ray AI | €3M | B2B subscription |
| Harrison.ai | Radiology AI | $129M | B2B enterprise |
| Qure.ai | X-ray triage | $90M | B2B per-scan |
| RapidAI | Stroke/vascular | $135M | B2B subscription |

### Technology Signals
- Google MedGemma 1.5 for medical image interpretation (open source)
- FDA cleared 22-minute full-body MRI (Ezra Flash AI)
- Vision language models achieving radiologist-level performance

### Market Trends
- 62% of digital health funding going to AI-enabled companies (H1 2025)
- 22% of healthcare orgs have implemented domain-specific AI (7x increase over 2024)
- Diagnostic imaging centers = fastest growing segment in Europe

### Regulatory Landscape
- CE Mark Class IIa for clinical decision support tools
- MDR compliance required for EU market
- CPT codes active for volumetric brain analysis (pathway for expansion)
