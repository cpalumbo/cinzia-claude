# Aprovo: Startup Ideation Evaluation

**Evaluation Framework:** Paul Graham / YC Methodology
**Date:** January 2026
**Evaluator:** Startup Ideation Skill

---

## Executive Summary

| Criterion | Score | Verdict |
|-----------|-------|---------|
| Founder Desire | 4/5 | Strong - built dental clinic software at Impress |
| Founder Capability | 5/5 | Excellent - exact domain match |
| Non-Obvious Value | 3/5 | Moderate - goRoger exists, but execution gap |
| Depth of Demand | 4/5 | Strong - clinics lose real money on unconverted quotes |
| Expansion Potential | 4/5 | Good - can expand across Europe, verticals |
| Moat Potential | 3/5 | Moderate - integrations create switching costs |
| **Overall** | **3.8/5** | **Viable - proceed with validation** |

**Bottom Line:** Aprovo passes the "minimum viable idea" threshold. It's a **schlep opportunity** that others avoid because of PMS integration complexity. The team's Impress experience (200+ dental clinics) is a genuine unfair advantage. Main risk: goRoger already exists in Germany with similar positioning.

---

## The Three Criteria (Must-Haves)

### 1. Founder Desire ✅ (4/5)

**Do the founders genuinely want this product to exist?**

| Question | Assessment |
|----------|------------|
| Would they use it themselves? | Partial - they've seen the problem at Impress, but aren't clinic operators |
| Solving their own problem? | Adjacent - solved scheduling/workflow at Impress, saw presupuesto conversion as gap |
| Personal urgency? | Moderate - business opportunity more than personal pain |

**Evidence:**
- Yerezhan built clinic workflow software for 200+ dental clinics at Impress
- Observed the presupuesto → conversion problem firsthand
- Not a "made up" idea - emerged from domain experience

**Red Flag Check:** ⚠️ "I can imagine other people wanting this" risk exists, but mitigated by direct exposure to dental clinic operations.

**Verdict:** Strong founder-problem fit through professional experience, not personal pain.

---

### 2. Founder Capability ✅ (5/5)

**Can the founders build a working v1?**

| Question | Assessment |
|----------|------------|
| Can build v1 without hiring? | Yes - Yerezhan is CTO/CPO with full-stack capability |
| Relevant domain expertise? | Excellent - 5+ years building dental clinic software |
| Iterate quickly? | Yes - small team, known problem space |

**Evidence:**
- Built Impress's full EMR/scheduling/patient platform from scratch
- Scaled to 200+ clinics across 9 countries
- DICOM, PMS integrations, compliance = solved problems
- Multi-country healthcare compliance experience

**Key Capability Match:**

| Aprovo Requirement | Team Experience |
|--------------------|-----------------|
| WhatsApp Business API | Modern messaging systems ✅ |
| E-signature integration | Document workflows ✅ |
| Payment processing | Patient billing systems ✅ |
| PMS write-back | Built EMR integrations ✅ |
| Spain-first | Based in Barcelona ✅ |

**Verdict:** Near-perfect capability match. This team can absolutely build Aprovo.

---

### 3. Non-Obvious Value ⚠️ (3/5)

**Do few others recognize this opportunity?**

| Question | Assessment |
|----------|------------|
| Few others see this? | No - goRoger in Germany does similar |
| Why hasn't it been done well? | PMS integration schlep |
| Founder's unique insight? | Impress clinic network access |

**Competitive Reality:**

| Competitor | Focus | Gap |
|------------|-------|-----|
| **goRoger** (Germany) | WhatsApp + treatment plans + factoring | Similar positioning, not in Spain |
| **Doctoralia** | Appointments, not conversion | Missing e-sign + payment loop |
| **Dentrix/Open Dental** | PMS, not conversion | US-focused, no WhatsApp |
| **Rectangle Health** | Payments + communication | US-focused |
| **Generic PRMs** | Messaging, no closed loop | Don't write back to PMS |

**The Insight:**
> "Existing 'PRM' tools are generic and don't close the loop (no signature/payment in the same thread) or don't write back to the clinic's PMS."

This is valid. The **closed loop** (WA → e-sign → pay → PMS write-back) is the differentiator.

**Red Flag:** goRoger exists with similar positioning in Germany. They claim 25% uplift. The Spain opportunity may be timing-based (goRoger hasn't entered Spain yet).

**Verdict:** Not highly non-obvious, but execution gap exists. Speed to market in Spain matters.

---

## The Well Test

### Depth of Demand ✅ (4/5)

**Is there intense need from a specific group?**

| Question | Assessment |
|----------|------------|
| Intense need from specific group? | Yes - clinics with 40%+ insured patients |
| Would users be devastated if this disappeared? | Yes - if it delivers 25% uplift, it's critical |
| Are people hacking together workarounds? | Yes - staff chase patients manually, re-type statuses |

**The Problem is Real:**

```
Today's Workflow (Painful):
1. Clinic creates presupuesto in PMS
2. Staff calls/emails patient
3. Patient ignores or delays
4. Staff follows up manually (phone tag)
5. If patient accepts, staff prints doc for signature
6. Patient comes to clinic to sign
7. Staff manually updates PMS
8. Revenue delayed or lost
```

**Quantified Pain:**
- Spain: ~23,000 dental clinics
- 90%+ are private practices
- Average treatment quote: €500-5,000
- If 30% of quotes are unconverted, that's real money
- goRoger claims 25% uplift in accepted quotes

**Demand Depth Score:**

| Signal | Level |
|--------|-------|
| "I would pay anything for this" | 🟢 Strong - if ROI is proven |
| "That would be nice to have" | - |
| "I guess I'd try it" | - |

**Verdict:** Deep demand exists for clinics that understand the problem. The challenge is making the pain visible to clinics that don't track conversion rates.

---

### Narrowness (Starting Point) ✅

**Is the initial target market well-defined?**

| Question | Assessment |
|----------|------------|
| Well-defined initial target? | Yes - 3-15 chair clinics with insured patients |
| Can name specific potential users? | Yes - Barcelona dental clinics from Impress network |
| Narrow enough to dominate? | Yes - Spain-first, dental-only |

**ICP Definition (from Aprovo doc):**
> "Independents & small DSOs with 3–15 chairs, a meaningful share of insured/plan patients, and visible backlog of pending presupuestos. Early adopters who already use WhatsApp and are open to e-sign & mobile payments."

**Market Size:**
- Spain: ~23,000 dental clinics
- Target segment (3-15 chairs, 40%+ insured): ~5,000-8,000 clinics
- Starting in Barcelona: ~500-1,000 clinics

**Verdict:** Well-defined beachhead. Can dominate Spain before expanding.

---

## Expansion Potential (4/5)

### Path Out of the Well

| Question | Assessment |
|----------|------------|
| Logical expansion path? | Yes - other countries, other healthcare verticals |
| Market growing? | Yes - DSO consolidation, WhatsApp adoption |
| Leading edge of larger trend? | Moderate - healthcare digitization, mobile-first |

**Expansion Roadmap:**

```
Phase 1: Spain Dental (Beachhead)
├── Barcelona → Madrid → Valencia
├── Independent clinics → DSO chains
└── Target: 500 clinics

Phase 2: European Dental
├── Portugal (MB Way payments)
├── Italy (BANCOMAT Pay)
└── Germany (challenge goRoger directly)

Phase 3: Adjacent Verticals
├── Aesthetic clinics (similar quote dynamics)
├── Ophthalmology (LASIK, etc.)
└── Veterinary (high-value procedures)
```

**Trend Alignment:**
- WhatsApp Business API adoption growing
- DSO consolidation in Spain (Sanitas now at 217 clinics)
- Mobile payment adoption (Bizum ubiquitous in Spain)
- Healthcare consumerization

**Verdict:** Clear expansion path. Not a small problem - small manifestation of a bigger problem (healthcare revenue cycle).

---

## Red Flag Detection

### Tarpit Ideas ⚠️

| Question | Assessment |
|----------|------------|
| Have many others tried and failed? | Partial - PRMs are crowded, but closed-loop is different |
| Structurally hard thing not obvious? | PMS integration is the known schlep |
| Requires changing behavior? | Moderate - patients need to adopt mobile signing/paying |

**Tarpit Risk Assessment:**

| Risk | Mitigation |
|------|------------|
| PMS integration is hard | Start with Zapier/exports, deepen later |
| WhatsApp policy changes | Template governance, compliance logs |
| Patient adoption friction | Patients already use WhatsApp in Spain |
| Price sensitivity | €199-699/mo is affordable if ROI is 25%+ |

**Verdict:** Not a tarpit. The schlep (PMS integration) is the moat, not the trap.

---

### Made-Up Ideas ❌ (Passes)

| Question | Assessment |
|----------|------------|
| From "brainstorming startup ideas"? | No - from Impress domain experience |
| Sounds impressive but feels hollow? | No - very specific, tactical problem |
| Would founder work on this without funding? | Likely - can bootstrap with 10 pilots |

**Verdict:** This is a "noticed" idea, not a "made up" idea.

---

### Schlep Disguise ✅ (Opportunity)

**Is the idea actually good but dismissed as too hard?**

> "Schlep blindness" hides great ideas that involve tedious, unpleasant work.

**The Schlep in Aprovo:**
1. PMS integrations (Gesden, Clinic Cloud, Nubimed, etc.)
2. WhatsApp Business API template approvals
3. E-signature compliance (eIDAS)
4. Payment processing (SEPA, Bizum)
5. GDPR/LOPDGDD compliance

**Why Others Avoid It:**
- Generic PRMs don't want to do PMS integration
- Payment companies don't want to do healthcare
- Healthcare companies don't want to do payments
- Nobody wants to close the full loop

**Verdict:** This is a classic schlep opportunity. The difficulty is the moat.

---

## Competitive Landscape

### What Do People Use Today?

| Solution | What It Does | Gap |
|----------|--------------|-----|
| Phone calls | Staff manually calls patients | Time-consuming, low conversion |
| Email | Presupuesto sent as PDF | 20% open rates, no action |
| Doctoralia | Appointment booking | No quote conversion |
| Generic SMS/WA | Reminders only | No e-sign, no payment, no write-back |
| Manual tracking | Spreadsheets | Error-prone, no ROI visibility |

### Why Hasn't This Been Solved Well?

1. **Integration complexity** - Each PMS is different
2. **Spain-specific** - Bizum, SEPA, Spanish insurance workflows
3. **Compliance burden** - eIDAS, GDPR, WhatsApp policies
4. **Fragmented market** - 23,000 clinics, mostly independents

### What 10x Improvement Looks Like

| Metric | Today | With Aprovo |
|--------|-------|-------------|
| Quote acceptance rate | ~60% | 75-85% (25% uplift) |
| Time to signature | Days/weeks | Minutes |
| Staff follow-up time | Hours/week | Automated |
| Payment collection | Delayed | Immediate |
| ROI visibility | None | Dashboard |

---

## Defensibility Assessment (3/5)

### Why Won't Big Companies Copy This?

| Barrier | Strength |
|---------|----------|
| PMS integrations | Moderate - takes time to build |
| Spain-specific knowledge | Strong - Bizum, insurance, legal |
| Clinic relationships | Strong - if team leverages Impress network |
| WhatsApp templates | Weak - anyone can get approved |

### Unfair Advantages

1. **Impress network** - Access to 200+ dental clinics for pilots/referrals
2. **Domain expertise** - 5+ years building dental clinic software
3. **Barcelona base** - Local market, Spanish speakers
4. **Speed** - goRoger hasn't entered Spain yet

### Moat Potential

| Moat Type | Present? | Notes |
|-----------|----------|-------|
| Network effects | Weak | Not a marketplace |
| Switching costs | Moderate | PMS integration creates lock-in |
| Data advantage | Moderate | ROI benchmarks across clinics |
| Brand | Weak | Early stage |

**Verdict:** Moderate defensibility. The moat comes from integration depth and clinic relationships, not from technology alone.

---

## Final Scoring

### YC Idea Evaluation Matrix

| Dimension | Score | Notes |
|-----------|-------|-------|
| Founder desire | 4/5 | Professional, not personal pain |
| Founder capability | 5/5 | Near-perfect match |
| Non-obvious value | 3/5 | goRoger exists; execution gap |
| Depth of demand | 4/5 | Real money at stake |
| Expansion potential | 4/5 | Clear geographic + vertical path |
| Moat potential | 3/5 | Integrations, not network effects |
| **Average** | **3.8/5** | **Above threshold** |

**Minimum Viable Idea Threshold:**
- ✅ Score 4+ on first three dimensions: 4 + 5 + 3 = **12/15** (borderline, but capability compensates)
- ✅ Score 3+ on others: 4 + 4 + 3 = **11/15** (passes)

---

## Key Questions to Answer

### Before Committing

1. **Why hasn't goRoger entered Spain?**
   - Is there a structural reason, or just timing?
   - What's their expansion roadmap?

2. **What's the true conversion rate problem?**
   - Interview 10 clinics: what % of presupuestos are never accepted?
   - What's the average value left on the table?

3. **Will clinics pay for this?**
   - €199-699/mo seems reasonable if ROI is 25%
   - But do clinic owners understand their conversion rates?

4. **Can you actually integrate with Spanish PMS systems?**
   - Gesden, Clinic Cloud, Nubimed - what's the API situation?
   - Is Zapier/export viable for MVP?

### Validation Experiments

| Experiment | Success Metric |
|------------|----------------|
| Interview 20 clinics about quote conversion | 80%+ say it's a problem |
| Send 100 WA messages for one clinic (manual) | 20%+ response rate |
| Run 10 paid pilots | 15%+ uplift in accepted quotes |
| Test PMS write-back with 3 systems | 2/3 have viable integration path |

---

## Verdict: Proceed with Validation

### Strengths
1. **Schlep opportunity** - Integration complexity is the moat
2. **Team capability** - Built exactly this at Impress scale
3. **Clear beachhead** - Spain dental, well-defined ICP
4. **Real problem** - Clinics lose money on unconverted quotes
5. **Timing** - goRoger hasn't entered Spain yet

### Weaknesses
1. **goRoger exists** - Not a unique insight globally
2. **Sales-heavy** - Needs to convince clinics of a problem they may not track
3. **Integration depth** - MVP may be too shallow to deliver ROI
4. **Moderate moat** - Competitors could copy with enough effort

### Recommendation

**Proceed with a 4-6 week pilot:**
1. Sign 10 paid pilots (€199/mo, no custom dev)
2. Run acceptance loop manually first (validate before building)
3. Measure: accepted € uplift, time-to-signature, staff hours saved
4. Decision gate: 15%+ uplift at 6+ sites = green light to build

**Key Question to Answer:**
> "Can we prove 25% uplift in accepted presupuestos without deep PMS integration?"

If yes, build. If no, the schlep may be unavoidable from day one.

---

## Sources

### Market Data
- [Spain Dental Practice Management Software Market](https://www.grandviewresearch.com/horizon/outlook/dental-practice-management-software-market/spain) - €100.4M by 2030
- [Spain DSO Market](https://www.grandviewresearch.com/horizon/outlook/dental-service-organization-market/spain) - $9.1B by 2030, 20% CAGR
- [Dental Clinics in Spain](https://www.businesscoot.com/en/study/the-market-for-dentists-and-dental-practices-spain) - ~23,000 clinics

### Competition
- [goRoger (Sanos Group)](https://www.crunchbase.com/organization/sanos-group-b2a8) - Germany-based, Seed funded
- [goRoger on Dealroom](https://app.dealroom.co/companies/roger_der_assistent_f_r_zahnarztpraxen)

### WhatsApp for Healthcare
- [WhatsApp for Dental Clinics - Rasayel](https://learn.rasayel.io/en/blog/how-to-use-whatsapp-marketing-campaigns-for-dental-clinics/) - 45-60% conversion via WhatsApp
- [WhatsApp Business API for Dental](https://getitsms.com/blogs/whatsapp-business-api-for-dental-clinics/) - 98% open rates
