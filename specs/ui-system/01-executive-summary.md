# Executive Summary — A/B Test Analyzer UI/UX System

**Version:** 1.0  
**Date:** 2025-01-27  
**Style Reference:** `style.md` (Bosk8 Design System — Dark Minimal Mono)

## Goals

Deliver a production-ready web interface for the Marketing Campaign A/B Test Analyzer that:

1. **Enables rapid statistical analysis** of A/B test results through an intuitive, single-page interface
2. **Provides clear, actionable insights** via statistical metrics (p-values, confidence intervals, power analysis) with plain-language decision guidance
3. **Adheres strictly to Bosk8 design system** (`style.md`) for visual consistency and brand alignment
4. **Maintains accessibility** (WCAG 2.2 AA) and responsive behavior across desktop and mobile devices
5. **Supports both aggregated and row-level data** input via manual entry or CSV upload

## Primary Personas

### 1. Data Analyst (Primary)
- **Goals:** Quickly determine if Variant B outperforms Variant A with statistical rigor
- **Needs:** Clear p-values, confidence intervals, power analysis, and a binary decision (ship/hold)
- **Context:** Regular analysis of marketing campaign tests; understands statistics but values speed and clarity
- **Pain Points:** Existing tools require multiple steps or lack clear decision rules; need for ROI estimates when B wins

### 2. Marketing Manager (Secondary)
- **Goals:** Understand test results at a high level and make go/no-go decisions
- **Needs:** Simple interpretation of statistical results, clear decision recommendation, ROI estimates
- **Context:** Oversees campaigns but may not be deeply statistical; needs confidence in decisions
- **Pain Points:** Statistical jargon; unclear actionable outcomes

### 3. Developer/Researcher (Tertiary)
- **Goals:** Validate statistical calculations, explore power curves, understand assumptions
- **Needs:** Detailed metrics, assumptions documentation, exportable results
- **Context:** Deep dives into test methodology; may integrate with other tools
- **Pain Points:** Opaque calculations; lack of methodology transparency

## Major User Flows

### Flow 1: Quick Analysis (Happy Path) — Data Analyst
1. **Entry:** User opens sine-page application
2. **Input:** Enters test data (success counts, totals for A and B) in sidebar
3. **Calculation:** System automatically computes results on input change
4. **Review:** Views conversion rates, z-statistic, p-value, confidence interval in main area
5. **Decision:** Sees clear decision banner (Variant B Wins / Inconclusive / Variant A Better)
6. **Power:** Reviews power analysis for current sample size
7. **Action:** If B wins, sees ROI estimate; if inconclusive, sees recommendations

### Flow 2: CSV Upload Analysis — Data Analyst
1. **Entry:** User opens application
2. **Upload:** Uploads CSV file (aggregated or row-level format)
3. **Validation:** System validates format and displays parsed data
4. **Calculation:** Automatic calculation triggers
5. **Review:** Same as Flow 1 steps 4-7

### Flow 3: Parameter Exploration — Developer/Researcher
1. **Entry:** User opens application
2. **Adjust:** Modifies significance level (α) or MDE for power calculation via sliders
3. **Observe:** Watches results update in real-time
4. **Explore:** Expands "Understanding the Results" section for detailed explanations
5. **Export:** (Future) Exports results or power curve visualization

### Ferguson Cases (Edge Cases)
- **Invalid Input:** Success count > total count → Clear error alert, input highlighting
- **Zero Conversions:** One or both variants have 0 conversions → Results still compute with appropriate warnings
- **Very Small Samples:** Sample size < 30 per group → Warning about normal approximation validity
- **Wide Confidence Intervals:** CI spans negative and positive → Inconclusive decision with recommendation
- **File Upload Error:** Invalid CSV format → Error message with expected format guidance
- **No Data:** Empty state before any input → Placeholder text and sample data option

## Constraints

### Technical Constraints
- **Framework:** Streamlit (current) — consider future migration to React/Next.js for full design system control
- **Backend:** Python-based statistical functions (` (`src/abtest.py`) — must maintain API compatibility
- **Data Format:** CSV support required for both aggregated (`group,success,total`) and row-level (`user_id,group,converted`) formats
- **Performance:** Real-time calculation updates; must handle sample sizes up to 100k+ observations without lag

### Design Constraints
- **Style System:** Must strictly adhere to `style.md` tokens — no new color tokens, typography, or spacing values
- **Accessibility:** WCAG 2.2 AA minimum — all interactive elements keyboard accessible, sufficient color contrast
- **Responsive:** Must work on mobile (320px+) and desktop (1024px+) with layout adaptations at 768px breakpoint
- **Browser Support:** Modern browsers (Chrome, Firefox, Safari, Edge) — latest 2 versions

### Functional Constraints
- **Statistical Rigor:** Cannot compromise on calculation accuracy; must match `src在有test.py` exactly
- **Decision Rule:** Must implement exact rule: p < α AND CI lower bound > 0 → B wins; else inconclusive
- **Power Analysis:** Must support MDE range 0.1pp to 10.0pp for power calculation
- **No Sequential Testing:** UI must not support sequential peeking (out of scope per project scope)

## Success Metrics

### User Experience Metrics
- **Time to Insight:** User can enter data and see decision in < 30 seconds
- **Error Rate:** < 5% of users encounter input validation errors (indicating clear guidance)
- **Accessibility Score:** Lighthouse accessibility score ≥ 95

### Technical Metrics
- **Calculation Latency:** Statistical results compute in < 100ms for typical inputs
- **Load Time:** Initial page load < 2s on 3G connection
- **Style Compliance:** 100% of UI elements reference `style.md` tokens (verified via Style Compliance Matrix)

## Assumptions Logged

See `09-style-decisions-log.md` for detailed assumptions, but key high-level assumptions:

1. **Single-page application** — no routing needed; all functionality accessible from one view
2. **Real-time calculation** — results update on every input change (debounced if performance issues)
3. **Streamlit migration path** — current Streamlit app can be enhanced incrementally; future full rewrite possible
4. **No authentication** — tool is standalone; no user accounts or saved sessions (future enhancement)
5. **CSV upload optional** — manual entry is primary method; CSV upload is convenience feature
6. **ROI calculation placeholder** — requires user-provided `monthly_visits` and `value_per_visit` (not in scope for first pass, logged for future)

## Open Questions

1. **Export functionality** — Should results be exportable (PDF report, JSON data)? → Deferred businesses; logged for Phase 2
2. **Historical test tracking** — Should users be able to save/compare multiple tests? → Out of scope for MVP
3. **Visualization needs** — Power curve visualization required or text-only sufficient? → Power curve recommended but deferrable
4. **Mobile optimization** — Should sidebar collapse on mobile or remain accessible? → Sidebar should collapse/overlay on mobile (< 768px)

---

**Next:** See `02-information-architecture.md` for sitemap and detailed user flows.

