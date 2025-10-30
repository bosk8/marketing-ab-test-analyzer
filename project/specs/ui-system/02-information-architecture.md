# Information Architecture & User Flows

**Version:** 1.0  
**Date:** 2025-01-27  
**Style Reference:** `style.md`

## Sitemap

The A/B Test Analyzer is a **single-page application (SPA)** with no routing required. All functionality exists on one view.

```
┌─────────────────────────────────────────────┐
│         A/B Test Analyzer (Home)            │
│                                             │
│  ┌───────────────────────────────────────┐ │
│  │  Header / Hero Section                │ │
│  │  - Title: "A/B TEST ANALYZER"         │ │
│  │  - Tagline / Overview                 │ │
│  └───────────────────────────────────────┘ │
│                                             │
│  ┌──────────────┐  ┌─────────────────────┐ │
│  │   Sidebar    │  │   Main Content      │ │
│  │   (Inputs)   │  │   (Results)         │ │
│  │              │  │                     │ │
│  │  - Variant A │  │  - Conversion Rates │ │
│  │  - Variant B │  │  - Statistical Test │ │
│  │  - α, MDE    │  │  - Decision Banner  │ │
│  │  - CSV Upload│  │  - Power Analysis   │ │
│  │              │  │  - Info/FAQ         │ │
│  └──────────────┘  └─────────────────────┘ │
│                                             │
│  ┌───────────────────────────────────────┐ │
│  │  Footer / Assumptions Note            │ │
│  └───────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

### Responsive Layout Structure

**Desktop (≥ 768px):**
- Sidebar: Fixed width (~300px), left side
- Main content: Remaining width, right side
- Two-column layout for metrics (conversion rates, statistical results)

**Mobile (< 768px):**
- Sidebar: Collapses to top section or drawer overlay (toggle button)
- Main content: Full width, stacked vertically
- Single-column layout for all metrics

## User Flows

### Flow 1: Quick Analysis (Primary Happy Path)

**Actor:** Data Analyst  
**Goal:** Get decision on whether Variant B outperforms A  
**Duration:** < 30 seconds

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Entry: User opens application                           │
│    → Landing on home page                                  │
│    → Empty state or sample data pre-filled                 │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. Input: User enters test data in sidebar                 │
│    → Variant A: Success = 123, Total = 5000                │
│    → Variant B: Success = 155, Total = 5000                │
│    → α = 0.05 (default), MDE = 2.0pp (default)            │
│    → Input validation: Real-time checks                    │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. Automatic Calculation (on input change)                 │
│    → Backend: ztest_two_prop() called                      │
│    → Backend: power() called                               │
│    → Results computed: z, p, lift, CI, power               │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. Display Results (main content area)                     │
│    → Conversion Rates: Card with metrics                   │
│    → Statistical Test Results: z, p-value, lift            │
│    → Confidence Interval: Range display                    │
│    → Decision Banner: "Variant B Wins" (green)             │
│    → Power Analysis: Current power at MDE                  │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ 5. Action: User reviews decision                           │
│    → If B wins: ROI estimate shown (if provided)           │
│    → If inconclusive: Recommendation text shown            │
│    → User can adjust parameters and re-calculate           │
└─────────────────────────────────────────────────────────────┘
```

**Success Criteria:**
- Results appear within 100ms of input
- Decision is unambiguous (clear banner)
- All metrics clearly labeled and formatted

### Flow 2: CSV Upload Analysis

**Actor:** Data Analyst  
**Goal:** Analyze test results from CSV file  
**Duration:** < 45 seconds

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Entry: User opens application                           │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. Upload: User clicks "Upload CSV" in sidebar             │
│    → File picker opens                                     │
│    → User selects file (aggregated or row-level format)    │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. Validation: System parses and validates CSV             │
│    → If invalid: Error alert shown, format guidance        │
│    → If valid: Data extracted, sidebar inputs populated    │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. Auto-calculation: Results computed automatically        │
│    → Same as Flow 1, step 3-5                              │
└─────────────────────────────────────────────────────────────┘
```

**Edge Cases:**
- **Invalid format:** Show error with expected format example
- **Missing columns:** List missing columns in error
- **Empty file:** Show "File is empty" error
- **Multiple groups:** Use first A and B found (warn if duplicates)

### Flow 3: Parameter Exploration

**Actor:** Developer/Researcher  
**Goal:** Understand sensitivity to α and MDE  
**Duration:** Variable (exploratory)

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Entry: User has test data entered                       │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. Adjust α: User moves α slider (0.01 to 0.10)           │
│    → Results update in real-time                           │
│    → p-value threshold changes                             │
│    → Decision may flip (significant ↔ not significant)     │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. Adjust MDE: User moves MDE slider (0.1pp to 10.0pp)    │
│    → Power value updates                                   │
│    → Power threshold indicator updates (80% line)          │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. Expand Details: User clicks "Understanding Results"     │
│    → Expandable section opens                              │
│    → Detailed explanations of metrics                      │
│    → Tooltips on technical terms                           │
└─────────────────────────────────────────────────────────────┘
```

### Flow 4: Error Handling (Edge Case)

**Actor:** Any User  
**Goal:** Recover from input errors  
**Duration:** < 10 seconds Luft per error

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Invalid Input: User enters success > total              │
│    → Real-time validation triggers                         │
│    → Error alert appears: "Success count cannot exceed     │
│      total count for any variant."                         │
│    → Input field highlighted (border color: error state)   │
│    → Calculation blocked (results not shown or stale)      │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. Correction: User fixes input                            │
│    → Error alert dismisses                                 │
│    → Input field returns to normal state                   │
│    → Calculation resumes automatically                     │
└─────────────────────────────────────────────────────────────┘
```

**Error Types:**
- **Validation errors:** Success > total, negative values, zero totals → Inline alerts
- **Calculation errors:** Numerical overflow, invalid inputs → Error alert in results area
- **File errors:** Invalid CSV format, missing file → Alert with format guidance

### Flow 5: Empty State (First Visit)

**Actor:** New User  
**Goal:** Understand tool purpose and how to use it  
**Duration:** < 20 seconds

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Entry: User opens application for first time            │
│    → Empty state: No data entered                          │
│    → Placeholder text in inputs: "Enter success count"     │
│    → Sample data button: "Load Sample Data"                │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. Guidance: User sees overview section                    │
│    → Overview card explains tool purpose                   │
│    → Instructions: "Enter test data in sidebar to begin"   │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. Action: User either:                                    │
│    → Option A: Clicks "Load Sample Data" → Sample fills    │
│    → Option B: Enters own data → Flow 1 continues          │
└─────────────────────────────────────────────────────────────┘
```

## Navigation Model

### Global Navigation
- **None required** — single-page application

### Secondary Navigation (Within Page)
- **Scroll-to sections:** (Future enhancement) Jump links for:
  - Conversion Rates
  - Statistical Results
  - Decision
  - Power Analysis
- **Expandable sections:** "Understanding the Results" accordion/collapsible

### Breadcrumbs
- **None** — single level

## Empty States

### 1. No Data Entered (Initial State)
- **Location:** Main content area
- **Content:**
  - Message: "Enter test data in the sidebar to begin analysis."
  - Action button: "Load Sample Data" (optional, fills with sample_ab.csv data)
- **Visual:** Centered text, subtle (`--text-subtle`), card background

### 2. Calculation Error
- **Location:** Results area
- **Content:**
  - Error icon
  - Message: "Error in calculation: [specific error]"
  - Action: "Please check inputs and try again."
- **Visual:** Alert component (`--surface-card`, `--border-color`, `--text-subtle`)

### 3. No File Selected (CSV Upload)
- **Location:** Sidebar, file upload area
- **Content:**
  - Placeholder: "No file selected"
  - Button: "Choose File"
- **Visual:** Button with border (`--border-w solid --border-color`)

## First-Run Experience

1. **Landing:** User sees hero section with title "A/B TEST ANALYZER"
2. **Overview:** Overview card explains tool purpose and steps
3. **Sidebar:** Inputs are empty with placeholder text
4. **Guidance:** Subtle hint text: "Enter your test data above to see results"
5. **Sample Option:** Optional "Load Sample Data" button to populate with example

---

**Next:** See `03-screen-specs.md` for detailed screen-by-screen specifications with wireframes and component breakdowns.

