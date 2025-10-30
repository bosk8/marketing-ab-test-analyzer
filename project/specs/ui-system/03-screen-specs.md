# Screen-by-Screen Specifications

**Version:** 1.0  
**Date:** 2025-01-27  
**Style Reference:** `style.md`

## Screen 1: Main Analysis Page

**Purpose:** Single-page interface for A/B test analysis. All functionality accessible from one view.

**Route:** `/` (root ratio, single page)

---

### Layout Grid (Desktop ≥ 768px)

```
┌──────────────────────────────────────────────────────────────┐
│  Container: min(1100px, 90vw), centered                     │
│  Padding: var(--space-4) top, var(--space-1) sides/bottom   │
│  Background: var(--bg-elev1)                                 │
├─────────────────────────┬────────────────────────────────────┤
│  Sidebar                │  Main Content Area                 │
│  Width: ~300px          │  Flex: 1 (remaining width)        │
│  Sticky: Yes            │  Padding: var(--space-2)          │
│                         │                                    │
│  ┌─────────────────────┐│  ┌──────────────────────────────┐ │
│  │ Input Card          ││  │ Hero/Title Card              │ │
│  │ (Variant A)         ││  │                              │ │
│  └─────────────────────┘│  └──────────────────────────────┘ │
│                         │                                    │
│  ┌─────────────────────┐│  ┌──────────────────────────────┐ │
│  │ Input Card          ││  │ Overview Card                │ │
│  │ (Variant B)         ││  │                              │ │
│  └─────────────────────┘│  └──────────────────────────────┘ │
│                         │                                    │
│  ┌─────────────────────┐│  ┌──────────────┬───────────────┐ │
│  │ Parameters Card     ││  │ Conversion   │ Statistical   │ │
│  │ (α, MDE)            ││  │ Rates Card   │ Results Card  │ │
│  └─────────────────────┘│  └──────────────┴───────────────┘ │
│                         │                                    │
│  ┌─────────────────────┐│  ┌──────────────────────────────┐ │
│  │ CSV Upload Card     ││  │ Confidence Interval Card     │ │
│  │                     ││  │                              │ │
│  └─────────────────────┘│  └──────────────────────────────┘ │
│                         │                                    │
│                         │  ┌──────────────────────────────┐ │
│                         │  │ Decision Banner Card         │ │
│                         │  │                              │ │
│                         │  └──────────────────────────────┘ │
│                         │                                    │
│                         │  ┌──────────────────────────────┐ │
│                         │  │ Power Analysis Card          │ │
│                         │  │                              │ │
│                         │  └──────────────────────────────┘ │
│                         │                                    │
│                         │  ┌──────────────────────────────┐ │
│                         │  │ Info/FAQ Card (Expandable)   │ │
│                         │  │                              │ │
│                         │  └──────────────────────────────┘ │
│                         │                                    │
│                         │  ┌──────────────────────────────┐ │
│                         │  │ Assumptions/Footer Card      │ │
│                         │  │                              │ │
│                         │  └──────────────────────────────┘ │
└─────────────────────────┴────────────────────────────────────┘
```

### Layout Grid (Mobile < 768px)

```
┌──────────────────────────────────────────────────────────────┐
│  Container: 100vw, padding: var(--space-1)                  │
│  Background: var(--bg-elev1)                                 │
├──────────────────────────────────────────────────────────────┤
│  ┌────────────────────────────────────────────────────────┐ │
│  │ Mobile Header / Toggle                                 │ │
│  │ [☰ Menu] A/B TEST ANALYZER                            │ │
│  └────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────┤
│  ┌────────────────────────────────────────────────────────┐ │
│  │ Sidebar (Collapsible/Drawer)                           │ │
│  │ (Hidden by default, shown on menu click)               │ │
│  │                                                         │ │
│  │  - Input Card (Variant A)                              │ │
│  │  - Input Card (Variant B)                              │ │
│  │  - Parameters Card                                     │ │
│  │  - CSV Upload Card                                     │ │
│  └────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────┤
│  Main Content Area (Stacked vertically)                     │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ Hero/Title Card                                        │ │
│  └────────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ Overview Card                                          │ │
│  └────────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ Conversion Rates Card                                  │ │
│  └────────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ Statistical Results Card                               │ │
│  └────────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ Confidence Interval Card                               │ │
│  └────────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ Decision Banner Card                                   │ │
│  └────────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ Power Analysis Card                                    │ │
│  └────────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ Info/FAQ Card                                          │ │
│  └────────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ Assumptions/Footer Card                                │ │
│  └────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

---

## Component Breakdown by Section

### Section 1: Hero/Title Card

**Purpose:** Brand identity and tool identification

**Layout:**
- Centered alignment
- Full width within container
- Padding: `var(--space-2)`

**Components:**
- **Title (H1):** "A/B TEST ANALYZER"
  - Class: `tagline`
  - Font: `var(--font-ui)`
  - Size: `1rem` (from `fontSize.base`)
  - Transform: `uppercase`
  - Letter-spacing: `0.05em`
  - Color: `var(--text-muted)`
  - Text-align: `center`
  - Margin-bottom: `var(--space-1)`

**States:**
- Default: As specified
- No hover/focus states (static text)

**Responsive:**
- Mobile: Same styling, padding reduced to `var(--space-1_5)`

**Tokens Used:**
- `fontFamily.ui`
- `fontSize.base`
- `colors.text.muted`
- `spacing.md` (1rem)
- `spacing.lg` (1.5rem)
- `spacing.xl` (2rem)

---

### Section 2: Overview Card

**Purpose:** Brief explanation of tool functionality

**Layout:**
- Full width card
- Padding: `var(--space-2)`

**Components:**
- **Label:** "OVERVIEW"
  - Class: `meta-sm`
  - Font: `var(--font-ui)`
  - Size: `0.75rem` (`fontSize.sm`)
  - Transform: `uppercase`
  - Letter-spacing: `0.05em`
  - Color: `var(--text-muted)`
  - Margin-bottom: `var(--space-1)`
- **Body Text:**
  - Font: `var(--font-ui)`
  - Size: `var(--fs-base)`
  - Color: `var(--text-subtle)`
  - Line-height: `1.5`

**Card Styling:**
- Background: `var(--surface-card)`
- Border: `var(--border-outer-w) solid var(--border-color)`
- Box-shadow: `0 0 0 var(--border-outer-w) var(--border-color), 0 1px 2px var(--shadow-tint)`
- Border-radius: `var(--r-md)` (6px)
- Padding: `var(--space-2)`
- Margin-bottom: `var(--space-1_5)`

**States:**
- Default: As specified

**Responsive:**
- Mobile: Padding `var(--space-1_5)`, margin-bottom `var(--space-1)`

**Tokens Used:**
- `colors.surface.card`
- `colors.border.neutral`
- `borders.outer`
- `borders.md`
- `radii.md`
- `spacing.md`
- `spacing.lg`
- `spacing.xl`
- `shadows.tint`

---

### Section 3: Sidebar — Input Card (Variant A)

**Purpose:** Input control group for Variant A (control) data

**Layout:**
- Full width within sidebar
- Card container
- Padding: `var(--space-1_5)`
- Margin-bottom: `var(--space-1_5)`

**Components:**
- **Section Label:** "VARIANT A (CONTROL)"
  - Class: `meta-sm`
  - Font: `var(--font-ui)`
  - Size: `0.75rem`
  - Transform: `uppercase`
  - Letter-spacing: `0.05em`
  - Color: `var(--text-muted)`
  - Margin-bottom: `var(--space-0_75)`
- **Number Input 1:** "Successes (conversions)"
  - Type: `number`
  - Min: `0`
  - Step: `1`
  - Default: `123` (or empty)
  - Placeholder: "Enter success count"
  - Label: "Successes (conversions)"
- **Number Input 2:** "Total observations"
  - Type: `number`
  - Min: `1`
  - Step: `1`
  - Default: `5000` (or empty)
  - Placeholder: "Enter total count"
  - Label: "Total observations"

**Input Styling:**
- Font: `var(--font-ui)`
- Size: `var(--fs-base)`
- Background: `var(--bg-black)` (or `var(--surface-card)`)
- Color: `var(--text-primary)`
- Border: `var(--border-w) solid var(--border-color)`
- Border-radius: `var(--r-sm)` (4px)
- Padding: `var(--space-0_75)`
- Width: `100%`
- Margin-bottom: `var(--space-1)`

**Input States:**
- **Default:** As specified
- **Focus:**
  - Outline: `2px solid var(--border-color)`
  - Outline-offset: `2px`
  - Border-color: `var(--text-muted)` (subtle highlight)
- **Error:**
  - Border-color: `var(--accent-success)` (temporary — see Style Decisions Log)
  - Background: `var(--surface-card)` with subtle red tint (derived — see Style Decisions Log)
- **Disabled:**
  - Opacity: `0.5`
  - Cursor: `not-allowed`
  - Background: `var(--bg-elev1)`

**Validation:**
- Real-time validation: Check `success_a ≤ total_a`
- Error message: Alert component below input group if invalid

**Responsive:**
- Mobile: Same styling, inputs stack vertically

**Tokens Used:**
- `colors.bg.black`
- `colors.surface.card`
- `colors.text.primary`
- `colors.text.muted`
- `colors.border.neutral`
- `colors.accent.success` (error state — see Style Decisions Log)
- `borders.thin`
- `radii.sm`
- `spacing.xs`
- `spacing.sm`
- `spacing.md`
- `spacing.lg`

**Accessibility:**
- Label associated with each input (`<label>` or `aria-label`)
- Error message associated with `aria-describedby`
- Required field indication (visual + `aria-required`)

---

### Section 4: Sidebar — Input Card (Variant B)

**Purpose:** Input control group for Variant B (treatment) data

**Layout & Components:** Identical to Variant A section, with:
- Label: "VARIANT B (TREATMENT)"
- Input keys: `success_b`, `total_b`
- Default values: `155`, `5000` (or empty)

**All other specifications:** Same as Section 3.

---

### Section 5: Sidebar — Parameters Card

**Purpose:** Statistical parameter controls (α, MDE)

**Layout:**
- Full width within sidebar
- Card container
- Padding: `var(--space-1_5)`
- Margin-bottom: `var(--space-1_5)`

**Components:**
- **Section Label:** "STATISTICAL PARAMETERS"
  - Class: `meta-sm`
  - Styling: Same as Section 3 label
- **Slider 1:** "Significance level (α)"
  - Type: `range` (or custom slider component)
  - Min: `0.01`
  - Max: `0.10`
  - Step: `0.01`
  - Default: `0.05`
  - Display: Current value next to slider ("α = 0.05")
- **Slider 2:** "MDE for power calculation (pp)"
  - Type: `range`
  - Min: `0.1`
  - Max: `10.0`
  - Step: `0.1`
  - Default: `2.0`
  - Display: Current value ("MDE = 2.0 pp")
  - Note: Display percentage points (pp), store as decimal internally

**Slider Styling:**
- Track: `var(--bg-elev1)`, height `4px`, border-radius `2px`
- Thumb: `var(--text-muted)`, width `16px`, height `16px`, border-radius `50%`, border `var(--border-w) solid var(--border-color)`
- Active/Focus: Thumb color `var(--text-primary)`, outline `2px solid var(--border-color)`

**States:**
- Default: As specified
- Focus: Outline on thumb
- Active: Thumb color change

**Responsive:**
- Mobile: Same styling, sliders full width

**Tokens Used:**
- `colors.bg.elev1`
- `colors.text.muted`
- `colors.text.primary`
- `colors.border.neutral`
- `borders.thin`
- `spacing.md`
- `spacing.lg`

---

### Section 6: Sidebar — CSV Upload Card

**Purpose:** File upload for CSV data (aggregated or row-level)

**Layout:**
- Full width within sidebar
- Card container
- Padding: `var(--space-1_5)`
- Margin-bottom: `var(--space-1_5)`

**Components:**
- **Section Label:** "DATA UPLOAD"
  - Class: `meta-sm`
  - Styling: Same as Section 3 label
- **File Input:**
  - Type: `file`
  - Accept: `.csv`
  - Label: "Choose CSV file"
  - Button style: Use button component (see Component Library)
- **File Info Display:**
  - Shows selected filename if file chosen
  - Format: "Selected: sample_ab.csv" in `var(--text-subtle)`
  - Font size: `0.875rem`

**File Input Styling:**
- Hidden native input, custom button trigger
- Button: See Button component in Component Library

**States:**
- **Default:** "Choose CSV file" button visible
- **File Selected:** Filename displayed below button
- **Uploading:** Loading state (spinner, disabled button)
- **Error:** Error alert displayed (see Alert component)

**Validation:**
- File type: Must be `.csv`
- File size: Warn if > 10MB (optional)
- Format validation: After upload, validate columns (see backend function mapping)

**Responsive:**
- Mobile: Same styling

**Tokens Used:**
- `colors.text.subtle`
- `fontSize.md`
- `spacing.md`
- `spacing.lg`

---

### Section 7: Main Content — Conversion Rates Card

**Purpose:** Display calculated conversion rates for Variant A and B

**Layout:**
- Card container (desktop: half-width in two-column layout; mobile: full width)
- Padding: `var(--space-2)`

**Components:**
- **Section Label:** "CONVERSION RATES"
  - Class: `meta-sm`
  - Styling: Same as Overview label
  - Margin-bottom: `var(--space-1)`
- **Metric 1:** "Variant A"
  - Value: `{pa:.4f} ({pa*100:.2f}%)`
  - Format: "0.0246 (2.46%)"
  - Delta: None
- **Metric 2:** "Variant B"
  - Value: `{pb:.4f} ({pb*100:.2f}%)`
  - Delta: `{lift*100:+.3f} pp` (e.g., "+0.640 pp")
  - Delta color: Green if positive, neutral if zero/negative
- **Metric 3:** "Lift"
  - Value: `{lift*100:+.3f} percentage points`
  - Format: "+0.640 percentage points" or "-0.100 percentage points"

**Metric Styling:**
- Value font: `var(--font-ui)`
- Value size: `1.5rem` (or `fontSize.lg` scaled)
- Value color: `var(--text-primary)`
- Label font: `var(--font-ui)`
- Label size: `0.875rem` (`fontSize.md`)
- Label color: `var(--text-subtle)`
- Delta font: `var(--font-ui)`
- Delta size: `0.75rem`
- Delta color: `var(--accent-success)` if positive, `var(--text-dim)` if negative/zero

**Card Styling:**
- Same as Overview card

**States:**
- **Empty:** Placeholder "—" or "Enter data to see rates"
- **Calculated:** Display values as specified
- **Error:** Display error message instead of metrics

**Responsive:**
- Desktop: Half-width in two-column layout (with Statistical Results Card)
- Mobile: Full width, stacked

**Tokens Used:**
- `colors.surface.card`
- `colors.text.primary`
- `colors.text.subtle`
- `colors.text.dim`
- `colors.accent.success`
- `colors.border.neutral`
- `borders.outer`
- `radii.md`
- `spacing.md`
- `spacing.lg`
- `spacing.xl`

---

### Section 8: Main Content — Statistical Results Card

**Purpose:** Display z-statistic, p-value, and lift from statistical test

**Layout:**
- Card container (desktop: half-width in two-column layout with Conversion Rates; mobile: full width)
- Padding: `var(--space-2)`

**Components:**
- **Section Label:** "STATISTICAL TEST RESULTS"
  - Class: `meta-sm`
  - Styling: Same as Conversion Rates label
- **Metric 1:** "Z-statistic"
  - Value: `{z:.4f}`
  - Format: "2.3456"
- **Metric 2:** "P-value"
  - Value: `{p:.6f}`
  - Format: "0.019045"
  - Delta: "Significant" if `p < α`, else "Not significant"
  - Delta color: `var(--accent-success)` if significant, `var(--text-dim)` if not
- **Metric 3:** "Lift"
  - Value: `{lift*100:+.3f} pp`
  - Format: "+0.640 pp"

**Metric Styling:**
- Same as Conversion Rates metrics

**Card Styling:**
- Same as Conversion Rates card

**States:**
- **Empty:** Placeholder "—"
- **Calculated:** Display values
- **Error:** Error message

**Responsive:**
- Desktop: Half-width (with Conversion Rates)
- Mobile: Full width, stacked

**Tokens Used:**
- Same as Conversion Rates card

---

### Section 9: Main Content — Confidence Interval Card

**Purpose:** Display 95% confidence interval for lift

**Layout:**
- Full-width card
- Padding: `var(--space-2)`
- Margin-bottom: `var(--space-1_5)`

**Components:**
- **Section Label:** "95% CONFIDENCE INTERVAL"
  - Class: `meta-sm`
  - Styling: Same as other labels
- **Interval Display:**
  - Format: `{ci_lower:.6f} to {ci_upper:.6f} ({ci_lower_pct:+.3f} pp to {ci_upper_pct:+.3f} pp)`
  - Example: "0.001234 to 0.011566 (+0.123 pp to +1.157 pp)"
  - Font: `var(--font-ui)`
  - Size: `var(--fs-base)`
  - Color: `var(--text-primary)`
  - Background: Subtle card background (`var(--surface-card)`)
  - Padding: `var(--space-1)`
  - Border: `var(--border-w) solid var(--border-color)` (subtle)

**Card Styling:**
- Same as other cards

**States:**
- **Empty:** Placeholder "—"
- **Calculated:** Display interval
- **Zero Cross:** If CI includes zero, subtle visual indicator (border-left accent in `var(--text-dim)`)

**Responsive:**
- Mobile: Same styling, padding adjusted

**Tokens Used:**
- `colors.surface.card`
- `colors.text.primary`
- `colors.text.dim`
- `colors.border.neutral`
- `borders.thin`
- `radii.md`
- `spacing.md`
- `spacing.lg`
- `spacing.xl`

---

### b Section 10: Main Content — Decision Banner Card

**Purpose:** Clear binary decision output (Variant B Wins / Inconclusive / Variant A Better)

**Layout:**
- Full-width card
- Padding: `var(--space-2)`
- Margin-bottom: `var(--space-1_5)`

**Components:**
- **Decision Text:**
  - Condition 1 (B Wins): "✅ VARIANT B WINS" — Statistically significant improvement detected.
  - Condition 2 (Inconclusive — Positive but not sig): "⚠️ INCONCLUSIVE" — Positive lift but not statistically significant. Consider extending sample size.
  - Condition 3 (A Better/Equivalent): "ℹ️ VARIANT A BETTER OR EQUIVALENT" — Confidence interval suggests no improvement or decrease.
  - Condition 4 (Inconclusive — CI includes zero): "⚠️ INCONCLUSIVE" — Confidence interval includes zero. Consider extending sample size.

**Decision Styling:**
- Font: `var(--font-ui)`
- Size: `1rem` (`fontSize.base`)
- **B Wins:**
  - Color: `var(--accent-success)`
  - Icon: ✅ (emoji or SVG icon in success color)
- **Inconclusive:**
  - Color: `var(--text-subtle)` (warning variant — see Style Decisions Log)
  - Icon: ⚠️
- **A Better:**
  - Color: `var(--text-dim)`
  - Icon: ℹ️

**Card Styling:**
- Background: `var(--surface-card)`
- Border: `var(--border-outer-w) solid var(--border-color)`
- If B Wins: Border-left accent `4px solid var(--accent-success)` (derived pattern)

**States:**
- **Empty:** No decision shown
- **Calculated:** Decision displayed based on conditions
- **Loading:** Skeleton/placeholder

**Responsive:**
- Mobile: Same styling

**Tokens Used:**
- `colors.surface.card`
- `colors.accent.success`
- `colors.text.subtle`
- `colors.text.dim acetate`
- `colors.border.neutral`
- `borders.outer`
- `radii.md`
- `spacing.md`
- `spacing.lg`
- `spacing.xl`

---

### Section 11: Main Content — Power Analysis Card

**Purpose:** Display statistical power at current sample size and MDE

**Layout:**
- Full-width card
- Padding: `var(--space-2)`
- Margin-bottom: `var(--space-1_5)`

**Components:**
- **Section Label:** "POWER ANALYSIS"
  - Class: `meta-sm`
  - Styling: Same as other labels
- **Power Metric:**
  - Label: `Power to detect {mde:.1f}pp difference`
  - Value: `{power:.1%}`
  - Format: "85.3%"
  - Delta: None
- **Power Threshold Indicator:**
  - If power < 80%: Warning text "⚠️ Power is below the recommended 80% threshold. Consider increasing sample sizes."
  - If power ≥ 80%: Success text "✅ Power is sufficient (≥80%) for detecting a {mde:.1f}pp difference."
  - Warning color: `var(--text-subtle)`
  - Success color: `var(--accent-success)`

**Card Styling:**
- Same as other cards

**States:**
- **Empty:** Placeholder "—"
- **Calculated:** Display power and threshold indicator
- **Error:** Error message

**Responsive:**
- Mobile: Same styling

**Tokens Used:**
- Same as Decision Banner card (plus `colors.accent.success` for success state)

---

### Section 12: Main Content — Info/FAQ Card (Expandable)

**Purpose:** Expandable section with detailed explanations of statistical concepts

**Layout:**
- Full-width card (accordion/collapsible)
- Padding: `var(--space-2)` when expanded
- Margin-bottom: `var(--space-1_5)`

**Components:**
- **Trigger Button:** "📖 UNDERSTANDING THE RESULTS"
  - Class: Accordion trigger (see FAQ pattern in `style.md`)
  - Font: `var(--font-ui)`
  - Size: `0.75rem`
  - Transform: `uppercase`
  - Letter-spacing: `0.05em`
  - Color: `var(--text-muted)`
  - Background: `transparent`
  - Border: `none`
  - Padding: `1.25rem 1.75rem`
  - Width: `100%`
  - Display: `flex`, justify-content: `space-between`
  - Icon: Chevron (rotate on expand)
- **Content (Expanded):**
  - Explanations for:
    - Z-statistic
    - P-value
    - Lift
    - Confidence Interval
    - Power
  - Format: Bullet list or paragraphs
  - Font: `var(--font-ui)`
  - Size: `0.8rem`
  - Color: `var(--text-subtle)`
  - Line-height: `1.5`
  - Padding: `0 1.75rem 1.25rem`

**Accordion Styling:**
- Use FAQ pattern from `style.md`:
  - `.faq-item`: Border-bottom `var(--border-w) solid var(--border-color)`
  - `.faq-q`: Accordion trigger styling
  - `.faq-a`: Content area, `display: none` by default
  - `.faq-a.active`: `display: block`

**States:**
- **Collapsed:** Content hidden
- **Expanded:** Content visible
- **Hover:** Background `#18181b` (from `style.md` FAQ pattern)

**Responsive:**
- Mobile: Same styling, padding reduced

**Tokens Used:**
- `colors.surface.card`
- `colors.text.muted`
- `colors.text.subtle`
- `colors.border.neutral`
- `borders.thin`
- `radii.md`
- `spacing.md`
- `spacing.lg`
- `spacing.xl`
- FAQ hover background: `#18181b` (from `style.md`)

---

### Section 13: Footer/Assumptions Card

**Purpose:** Display statistical assumptions and limitations

**Layout:**
- Full-width card
- Padding: `var(--space-2)`

**Components:**
- **Section Label:** "NOTE"
  - Class: `meta-sm`
  - Styling: Same as other labels
- **Body Text:**
  - Lists assumptions:
    - Independent observations
    - Large sample sizes (normal approximation valid)
    - Fixed-horizon testing (no sequential peeking)
    - Equal allocation between variants
  - Font: `var(--font-ui)`
  - Size: `0.875rem`
  - Color: `var(--text-subtle)`
  - Line-height: `1.5`

**Card Styling:**
- Same as other cards

**States:**
- Default: Always visible

**Responsive:**
- Mobile: Same styling

**Tokens Used:**
- Same as Overview card

---

## Responsive Breakpoints

- **Mobile:** < 768px
  - Sidebar collapses to drawer/overlay
  - Main content stacks vertically
  - Cards full width
  - Padding reduced (`var(--space-1)` instead of `var(--space-2)`)
- **Tablet:** 768px — 1023px
  - Sidebar visible, fixed width
  - Main content two-column where applicable
  - Border width: `var(--border-w)` (1px)
- **Desktop:** ≥ 1024px
  - Sidebar visible, fixed width
  - Main content two-column where applicable
  - Border width: `var(--border-w)` (1.5px), `var(--border-outer-w)` (2px)

---

**Next:** See `04-component-library.md` for detailed component specifications with props, variants, and example usage.

