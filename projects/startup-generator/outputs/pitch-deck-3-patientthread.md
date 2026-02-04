# PatientThread
## Your Health History, Finally Connected

---

## The Problem

**Your preventive health records are scattered across a decade of different clinics.**

### The Fragmented Patient Journey

```
Age 32: Bloodwork at Lab A → Results in Lab A portal
Age 34: Mammography at Clinic B → PDF emailed, then lost
Age 35: Eye exam at Optometrist C → Paper printout filed somewhere
Age 37: Skin check at Dermatologist D → Notes in their EMR only
Age 39: Abdominal ultrasound at Clinic E → CD-ROM (really)
Age 41: New doctor asks for "complete history" → Patient: "Um..."
```

### The Real Consequences

1. **For Patients:**
   - No single view of health over time
   - Can't share history easily with new providers
   - Miss trends that matter (cholesterol creeping up, moles changing)

2. **For Clinics:**
   - Time wasted requesting prior records
   - Decisions made without full context
   - Duplicate tests ordered because priors unavailable

3. **For Healthcare Systems:**
   - Poor interoperability costs UK NHS **£1B+ annually**
   - 68% of clinics pay **€20K+/year** for third-party integration tools
   - Preventable conditions progress because early signals missed

### Why This Persists

- **EHRs don't talk to each other** (different vendors, formats, standards)
- **Patients don't own their data** (it's "held" by each provider)
- **No incentive for clinics** to share data outbound
- **Existing solutions are enterprise-only** (Particle, Datavant = big hospital systems)

---

## The Solution

**PatientThread** is a patient-controlled platform that aggregates your health records from any clinic, structures them into a unified timeline, and lets you share them with any provider.

### How It Works

```
Patient signs up for PatientThread
         ↓
Connects prior care locations
├── Manual upload (PDFs, images)
├── Patient portal integration (where available)
├── FHIR API connections (growing network)
└── OCR extraction from paper documents
         ↓
PatientThread creates unified timeline
├── Lab results over time (charts, trends)
├── Imaging history (linked to reports)
├── Medications and procedures
└── Preventive care schedule
         ↓
Patient shares with new provider
├── One-click sharing via secure link
├── Provider gets structured data
└── Automatically updated with new records
```

### The B2B Model

**We sell to clinics, not patients.**

```
Clinic subscribes to PatientThread
         ↓
Benefits for clinic:
├── New patient onboarding is instant
├── Full history available for first visit
├── Differentiated "connected care" offering
├── Patient retention (they don't want to lose their history)
         ↓
Benefits for patient:
├── Free access via clinic subscription
├── Portable record they control
├── Continuity across providers
```

---

## Why Now

### 1. Regulatory Tailwinds
- **CMS Interoperability Framework** mandating data sharing (2026)
- **60+ companies** pledged to comply, including major EHRs
- **FHIR** becoming universal standard (finally)
- **TEFCA** creating trusted exchange network

### 2. Patient Expectations Rising
- Patients used to having their data (finance, fitness)
- Why is health data the exception?
- Generational shift: younger patients demand portability

### 3. Infrastructure is Ready
- FHIR APIs now available at major health systems
- OCR and AI can extract data from legacy formats
- Cloud costs make storage economical

### 4. Competition is Enterprise-Focused
- Particle Health, Datavant, Redox = big health systems
- **Nobody serving the patient + clinic level**

---

## Market Size

### Total Addressable Market (TAM)
- Health data interoperability market: **$5B+** globally
- Patient engagement platforms: **$20B+**

### Serviceable Addressable Market (SAM)
- European multi-location clinic chains: ~5,000 chains
- At €6K/clinic/year = **€1.5B**

### Serviceable Obtainable Market (SOM)
- Year 5 target: 2,000 clinics × €7K/year = **€14M ARR**

### Bottom-Up Sizing

**Assumptions:**
- Target: Multi-location clinic chains (5-50 locations)
- Pricing: €500/clinic/month + €2/patient/year
- Average clinic chain: 10 locations, 5,000 patients

| Year | Clinic Chains | Total Clinics | Patients | ARR |
|------|---------------|---------------|----------|-----|
| Y1 | 5 | 50 | 10K | €320K |
| Y2 | 15 | 200 | 60K | €1.32M |
| Y3 | 30 | 500 | 200K | €3.4M |
| Y5 | 100 | 2,000 | 1M | €14M |

---

## Business Model

### Revenue Streams

1. **Clinic Subscription** (€500/clinic/month)
   - Patient record aggregation tools
   - Sharing and request management
   - Integration with clinic EMR

2. **Patient Volume Tier** (€2/active patient/year)
   - Patients with connected records
   - Storage and processing costs
   - Scales with clinic size

3. **Premium Features** (€200/clinic/month)
   - Advanced analytics and reporting
   - White-label patient app
   - Priority integrations

### Unit Economics (Target)

| Metric | Target |
|--------|--------|
| Clinic Chain Annual Value | €70K |
| CAC per Chain | €30K |
| Payback Period | 5 months |
| Gross Margin | 70% |
| Net Revenue Retention | 130%+ (as clinics add locations/patients) |

---

## Competition

### Competitive Landscape

| Company | Focus | Funding | Gap |
|---------|-------|---------|-----|
| **Particle Health** | Enterprise interoperability | $43M | Too big for clinic-level |
| **Datavant** | Data tokenization | $7B valuation | Enterprise infrastructure |
| **Redox** | EHR integration platform | $110M+ | Developer tool, not patient-facing |
| **Health Gorilla** | Health information network | $50M+ | US-focused, enterprise |
| **Apple Health** | Consumer aggregation | $2T company | Passive, no clinic integration |

### Our Positioning

```
                    Enterprise ──────────────────────────── Consumer
                         │                                      │
                         │  Datavant    Particle               │
                         │     ●           ●                   │
              Clinic     │                                     │
              Workflow   │        PatientThread                │
              Integrated │             ●                       │
                         │                                     │
                         │                           Apple     │
              Patient    │                           Health    │
              Only       │                              ●      │
                         │                                     │
                         └──────────────────────────────────────┘
```

**PatientThread differentiation:**
1. **Clinic-level entry point** - Affordable for small chains, not just hospitals
2. **Patient-controlled** - GDPR-native, consent-first model
3. **European focus** - Built for EU regulatory environment
4. **Workflow integration** - Works with existing clinic systems

---

## Traction / Validation

### Problem Validation

**Personal Experience:**
> "With my regular preventive tests... all the imaging and diagnostics are left on paper. And rarely are they stored in one place throughout the years for easy access and comparison."
> — Cinzia, Co-founder

**Market Validation:**
- Poor interoperability costs NHS £1B+ annually
- 68% of legacy EHR clinics pay €20K+ for integration tools
- 60+ companies pledging to CMS interoperability framework
- Patients increasingly demanding data portability

### Technical Validation
- Yerezhan built cross-clinic data systems at Impress (9 countries, 200+ clinics)
- FHIR, DICOM, HL7 = known standards for this team
- Cloud infrastructure for health data = solved problems

### Next Validation Steps
1. Partner with 2 multi-location clinic chains in Spain
2. Build aggregation MVP with manual upload + FHIR connections
3. Measure patient activation and sharing rates

---

## Team

### Yerezhan Tashbenbetov - Co-founder, CPTO
**Built cross-clinic data systems at scale.**

- CTO & CPO at Impress for 5+ years
- Unified infrastructure across 200+ clinics in 9 countries
- DICOM handling, EMR integration, compliance tooling
- Experience with patient data portability challenges

**Why this matters:** Yerezhan has solved the technical challenge of connecting disparate clinic systems at multi-country scale.

### Cinzia Palumbo - Co-founder, CRO/COO
**GTM leader who understands healthcare procurement.**

- Co-founder of Genie (developer tools, PLG motion)
- Scaled enterprise relationships at DJI
- Experience with complex, multi-stakeholder sales
- Personal motivation from fragmented health records

**Why this matters:** Selling to clinic chains requires navigating procurement, compliance, and IT - Cinzia has relevant enterprise sales experience.

### Why Us

| Dimension | Evidence |
|-----------|----------|
| Technical capability | Built multi-country clinic data platform |
| Domain expertise | Healthcare data, compliance, integration |
| Customer access | Existing network from Impress |
| Relevant experience | FHIR, DICOM, EMR integration |
| Passion for problem | Personal frustration with fragmented records |

---

## Financial Projections

### Revenue Forecast

| Year | Clinic Chains | Clinics | Patients | ARR |
|------|---------------|---------|----------|-----|
| Y1 | 5 | 50 | 10K | €320K |
| Y2 | 15 | 200 | 60K | €1.32M |
| Y3 | 30 | 500 | 200K | €3.4M |
| Y4 | 60 | 1,000 | 500K | €7M |
| Y5 | 100 | 2,000 | 1M | €14M |

### Cost Structure (Y3)

| Category | Amount | % of Revenue |
|----------|--------|--------------|
| Engineering (12 FTE) | €1.4M | 41% |
| Sales & Marketing | €800K | 24% |
| Infrastructure | €300K | 9% |
| G&A | €400K | 12% |
| **Total OpEx** | €2.9M | 85% |
| **Gross Profit** | €2.4M | 70% |
| **EBITDA** | €500K | 15% |

### Path to Profitability
- Higher CAC and longer sales cycles than other opportunities
- Break-even at ~€4M ARR (Y3-Y4)
- Infrastructure plays require more capital but create defensibility

---

## The Ask

### Seed Round: €2M

**Use of Funds:**

| Category | Amount | Purpose |
|----------|--------|---------|
| Product Development | €1M | FHIR integrations, aggregation platform |
| Sales & Marketing | €600K | 5 pilot clinic chains |
| Compliance & Legal | €200K | GDPR, health data handling |
| Operations | €200K | Support, admin |

**Milestones:**
- MVP with 5 FHIR integrations + manual upload
- 5 clinic chain pilots (50 clinics, 10K patients)
- €300K ARR
- GDPR compliance certification

### Why This Requires More Capital
- Infrastructure business with longer time to value
- Integration work is front-loaded
- Network effects require scale to kick in

---

## Exit Potential

### Acquisition Targets
- **Epic / Cerner (Oracle)** - Patient engagement layer
- **Veradigm (Allscripts)** - Ambulatory care focus
- **Datavant** - Roll-up into data network
- **European health systems** - National health services want this
- **Insurance companies** - Better data = better risk management

### Comparable Transactions
- Datavant: $7B valuation
- Redox: $110M+ raised
- Health Gorilla: $50M+ raised

### Strategic Value
- **Network effects** - More patients + clinics = more valuable data graph
- **Regulatory moat** - GDPR-compliant infrastructure is hard to build
- **Switching costs** - Patients won't want to rebuild their timeline elsewhere

---

## Appendix: Research Summary

### Interoperability Market Data

| Metric | Value | Source |
|--------|-------|--------|
| Cost of poor interoperability (UK NHS) | £1B+ annually | NHS Digital 2024 |
| Clinics paying for integration tools | 68% | Black Book Research |
| Average integration tool spend | €20K+/year | Black Book Research |
| Companies pledging CMS framework | 60+ | CMS 2025 |

### Funded Competitors

| Company | Funding | Focus |
|---------|---------|-------|
| Particle Health | $43M | Enterprise API |
| Datavant | $7B valuation | Data tokenization |
| Redox | $110M+ | EHR integration |
| Health Gorilla | $50M+ | QHIN network |
| 1upHealth | $47M | FHIR platform |

### Technology Trends
- FHIR becoming mandatory for US healthcare (CMS)
- TEFCA creating trusted exchange networks
- 22% of healthcare orgs implemented domain-specific AI (7x increase)
- Patient demand for data portability increasing

### Regulatory Landscape
- **EU:** GDPR, EHDS (European Health Data Space) incoming
- **US:** CMS Interoperability rules, TEFCA
- **UK:** NHS App becoming central patient portal
- Trend: Patients gaining more rights to their data globally
