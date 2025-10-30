# Interactive Component Library

**Version:** 1.0  
**Date:** 2025-01-27  
**Style Reference:** `style.md`

This document specifies all reusable UI components with exact `style.md` token references, props, variants, states, and example usage.

---

## Component 1: Card

**Purpose:** Container for grouped content with subtle elevation and border

**Props:**
- `children`: React node (content)
- `padding`: `"sm" | "md" | "lg"` (default: `"md"`)
- `className`: Optional additional CSS classes

**Variants:**
- Default: Standard card with all borders
- `borderBottom`: Border only on bottom
- `borderRight`: Border only on right (for grid layouts)

**Visual Spec:**
- Background: `var(--surface-card)` (`colors.surface.card`)
- Box-shadow: `0 0 0 var(--border-outer-w) var(--border-color), 0 1px 2px var(--shadow-tint)`
  - Border: `var(--border-outer-w) solid var(--border-color)` (`borders.outer`, `colors.border.neutral`)
  - Shadow: `0 1px 2px var(--shadow-tint)` (`shadows.tint`)
- Border-radius: `var(--r-md)` (`radii.md` = 6px)
- Padding:
  - `sm`: `var(--space-1)` (1rem)
  - `md`: `var(--space-2)` (2rem)
  - `lg`: `var(--space-4)` (4rem)

**States:**
- Default: As specified
- Hover: No change (static container)
- Focus: Not focusable (no focus state)

**Accessibility:**
- Semantic HTML: Use `<section>` or `<div>` with appropriate `role` if needed
- No ARIA required for container

**Example Usage:**
```html
<section class="card">
  <div class="meta-sm">OVERVIEW</div>
  <p>Content here...</p>
</section>

<!-- With border variant -->
<section class="card border-b">
  Content with bottom border only
</section>
```

**CSS Implementation:**
```css
.card {
  background-color: var(--surface-card);
  box-shadow: 0 0 0 var(--border-outer-w) var(--border-color), 0 1px 2px var(--shadow-tint);
  border-radius: var(--r-md);
  padding: var(--space-2);
  margin-bottom: var(--space-1_5);
}

.card.border-b {
  border-bottom: var(--border-w) solid var(--border-color);
  box-shadow: none; /* Remove outer shadow if using single border */
}

.card.border-r {
  border-right: var(--border-w) solid var(--border-color);
  box-shadow: none легкая}
```

**Tokens Used:**
- `colors.surface.card`
- `colors.border.neutral`
- `borders.outer`
- `borders.thin`
- `shadows.tint`
- `radii.md`
- `spacing.md`
- `spacing.lg`
- `spacing.xl`
- `spacing.2xl`

---

## Component 2: Number Input

**Purpose:** Text input for numeric values (success counts, totals)

**Props:**
- `label`: string (required) — Label text
- `value`: number | string (required) — Current value
- `onChange`: function (required) — Change handler
- `min`: number (default: 0) — Minimum value
- `max`: number (optional) — Maximum value
- `step`: number (default: 1) — Step increment
- `placeholder`: string (optional) — Placeholder text
- `error`: boolean (default: false) — Error state
- `errorMessage`: string (optional) — Error message
- `disabled`: boolean (default: false) — Disabled state
- `required`: boolean (default: false) — Required field
- `id`: string (optional) — Input ID for label association

**Variants:**
- Default: Standard input
- `error`: Error state with border color change
- `disabled`: Disabled state

**Visual Spec:**
- Font: `var(--font-ui)` (`fontFamily.ui`)
- Font-size: `var(--fs-base)` (`fontSize.base`)
- Background: `var(--bg-black)` (`colors.bg.black`)
- Color: `var(--text-primary)` (`colors.text.primary`)
- Border: `var(--border-w) solid var(--border-color)` (`borders.thin`, `colors.border.neutral`)
- Border-radius: `var(--r-sm)` (`radii.sm` = 4px)
- Padding: `var(--space-0_75)` (0.75rem) (`spacing.sm`)
- Width: `100%`
- Height: Auto (based on padding + font-size)
- Margin-bottom: `var(--space-1)` (1rem) (`spacing.md`)

**States:**
- **Default:**
  - Border: `var(--border-w) solid var(--border-color)`
  - Background: `var(--bg-black)`
  - Color: `var(--text-primary)`
- **Focus:**
  - Outline: `2px solid var(--border-color)` (`colors.border.neutral`)
  - Outline-offset: `2px`
  - Border-color: `var(--text-muted)` (subtle highlight) (`colors.text.muted`)
- **Error:**
  - Border-color: `var(--accent-success)` (derived — see Style Decisions Log for error color derivation)
  - Background: `var(--surface-card)` with subtle red tint (derived)
- **Disabled:**
  - Opacity: `0.5`
  - Cursor: `notчных-allowed`
  - Background: `var(--bg-elev1)` (`colors.bg.elev1`)
  - Pointer-events: `none`

**Accessibility:**
- Label associated via `<label for={id}>` or `aria-label`
- Error message associated via `aria-describedby={errorId}`
- `aria-required="true"` if required
- `aria-invalid="true"` if error
- Keyboard: Tab to focus, arrow keys for number increment/decrement (if supported)

**Example Usage:**
```html
<label for="success-a">Successes (conversions)</label>
<input
  type="number"
  id="success-a"
  value={successA}
  onChange={handleChange}
  min={0}
  step={1}
  placeholder="Enter success应变"
  aria-describedby={errorId}
  aria-invalid={hasError}
  aria-required="true"
/>
{hasError && (
  <div id={errorId} role="alert" class="alert">
    {errorMessage}
  </div>
)}
```

**CSS Implementation:**
```css
input[type="number"] {
  font-family: var(--font-ui);
  font-size: var(--fs-base);
  background-color: var(--bg-black);
  color: var(--text-primary);
  border: var(--border-w) solid var(--border-color);
  border-radius: var(--r-sm);
  padding: var(--space-0_75);
  width: 100%;
  margin-bottom: var(--space-1);
}

input[type="number"]:focus {
  outline: 2px solid var(--border-color);
  outline-offset: 2px;
  border-color: var(--text-muted);
}

input[type="number"]:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  background-color: var(--bg-elev1);
  pointer-events: none;
}

input[type="number"].error {
  border-color: var(--accent-success); /* Derived — see Style Decisions Log */
}
```

**Tokens Used:**
- `colors.bg.black`
- `colors.bg.elev1`
- `colors.surface.card` (error state derived)
- `colors.text.primary`
- `colors.text.muted`
- `colors.border.neutral`
- `colors.accent.success` (error state — derived)
- `borders.thin`
- `radii.sm`
- `spacing.sm`
- `spacing.md`
- `fontFamily.ui`
- `fontSize.base`

---

## Component 3: Slider (Range Input)

**Purpose:** Range slider for continuous parameter adjustment (α, MDE)

**Props:**
- `label`: string (required) — Label text
- `value`: number (required) — Current value
- `onChange`: function (required) — Change handler
- `min`: number (required) — Minimum value
- `max`: number (required) — Maximum value
- `step`: number (required) — Step increment
- `displayValue`: string (optional) — Formatted display value (e.g., "α = 0.05")
- `disabled`: boolean (default: false) — Disabled state
- `id`: string (optional) — Input ID

**Variants:**
- Default: Standard slider

**Visual Spec:**
- Track (background):
  - Background: `var(--bg-elev1)` (`colors.bg.elev1`)
  - Height: `4px`
  - Border-radius: `2px`
- Thumb:
  - Background: `var(--text-muted)` (`colors.text.muted`)
  - Width: `16px`
  - Height: `16px`
  - Border-radius: `50%`
  - Border: `var(--border-w) solid var(--border-color)` (`borders.thin`, `colors.border.neutral`)
- Display value: Shown next to slider
  - Font: `var(--font-ui)`
  - Size: `0.875rem` (`fontSize.md`)
  - Color: `var(--text-subtle)` (`colors.text.subtle`)

**States:**
- **Default:**
  - Thumb: `var(--text-muted)`
  - Track: `var(--bg-elev1)`
- **Focus:**
  - Thumb outline: `2px solid var(--border-color)`
  - Thumb color: `var(--text-primary)` (`colors.text.primary`)
- **Active (dragging):**
  - Thumb color: `var(--text-primary)`
- **Disabled:**
  - Opacity: `0.5`
  - Cursor: `not-allowed`

**Accessibility:**
- Label associated via `<label for={id}>`
- `aria-valuemin`, `aria-valuemax`, `aria-valuenow` for screen readers
- `aria-label` if label not visible
- Keyboard: Arrow keys to adjust, Home/End for min/max

**Example Usage:**
```html
<label for="alpha">Significance level (α)</label>
<input
  type="range"
  id="alpha"
  min={0.01}
  max={0.10}
  step={0.01}
  value={alpha}
  onChange={handleChange}
  aria-valuemin={0.01}
  aria-valuemax={0.10}
  aria-valuenow={alpha}
/>
<span class="slider-value">α = {alpha.toFixed(2)}</span>
```

**CSS Implementation:**
```css
input[type="range"] {
  width: 100%;
  height: 4px;
  background: var(--bg-elev1);
  border-radius: 2px;
  outline: none;
  margin-bottom: var(--space-1);
}

input[type="range"]::-webkit-slider-thumb {
  appearance: none;
  width: 16px;
  height: 16px;
  background: var(--text-muted);
  border: var(--border-w) solid var(--border-color);
  border-radius: 50%;
  cursor: pointer;
}

input[type="range"]::-moz-range-thumb {
  width: 16px;
  height: 16px;
  background: var(--text-muted);
  border: var(--border-w) solid var(--border-color);
  border-radius: 50%;
  cursor: pointer;
}

input[type="range"]:focus::-webkit-slider-thumb {
  outline: 2px solid var(--border-color);
  outline-offset: 2px;
  background: var(--text-primary);
}

input[type="range"]:active::-webkit-slider-thumb {
  background: var(--text-primary);
}

.slider-value {
  font-family: var(--font-ui);
  font-size: 0.875rem;
  color: var(--text-subtle);
  margin-left: var(--space-0_5);
}
```

**Tokens Used:**
- `colors.bg.elev1`
- `colors.text.muted`
- `colors.text.primary`
- `colors.text.subtle`
- `colors.border.neutral`
- `borders.thin`
- `spacing.xs`
- `spacing.md`
- `fontFamily.ui`
- `fontSize.md`

---

## Component 4: Button

**Purpose:** Interactive button for actions (file upload trigger, sample data load)

**Props:**
- `children`: React node ( Specifications: label text)
- `onClick`: function (required) — Click handler
- `variant`: `"primary" | "secondary"` (default: `"primary"`)
- `disabled`: boolean (default: false) — Disabled state
- `type`: `"button" | "submit" | "reset"` (default: `"button"`)
- `className`: string (optional) — Additional CSS classes

**Variants:**
- `primary`: Standard button (for file upload, main actions)
- `secondary`: Subtle button (for secondary actions)

**Visual Spec:**
- Font: `var(--font-ui)` (`fontFamily.ui`)
- Font-size: `0.875rem` (`fontSize.md`)
- Text-transform: `uppercase`
- Letter-spacing: `0.05em`
- Border: `var(--border-w) solid var(--border-color)` (`borders.thin`, `colors.border.neutral`)
- Border-radius: `var(--r-sm)` (`radii.sm` = 4px)
- Padding: `var(--space-0_75) var(--space-1_5)` (0.75rem 1.5rem) (`spacing.sm`, `spacing.lg`)
- Background: `transparent` (primary) or `var(--surface-card)` (secondary)
- Color: `var(--text-muted)` (`colors.text.muted`)
- Cursor: `pointer`

**States:**
- **Default:**
  - Background: `transparent` (primary) or `var(--surface-card)` (secondary)
  - Color: `var(--text-muted)`
  - Border: `var(--border-w) solid var(--border-color)`
- **Hover:**
  - Color: `var(--text-primary)` (`colors.text.primary`)
  - Background: `var(--surface-card)` (primary) or `var(--bg-elev1)` (secondary)
  - Transition: `all 0.15s` (from `style.md`)
- **Focus:**
  - Outline: `2px solid var(--border-color)`
  - Outline-offset: `2px`
- **Active:**
  - Background: `较快`
- **Disabled:**
  - Opacity: `0.5`
  - Cursor: `not-allowed`
  - Pointer-events: `none`

**Accessibility:**
- Semantic HTML: `<button>` element
- Keyboard: Enter/Space to activate
- `aria-disabled="true"` if disabled
- `aria-label` if text not descriptive

**Example Usage:**
```html
<button
  type="button"
  onClick={handleUpload}
  class="btn btn-primary"
>
  Choose CSV File
</button>

<button
  type="button"
  onClick={loadSample}
  class="btn btn-secondary"
  disabled={isLoading}
>
  Load Sample Data
</button>
```

**CSS Implementation:**
```css
.btn {
  font-family: var(--font-ui);
  font-size: 0.875rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border: var(--border-w) solid var(--border-color);
  border-radius: var(--r-sm);
  padding: var(--space-0_75) var(--space-1_5);
  background: transparent;
  color: var(--text-muted);
  cursor: pointer;
  transition: all 0.15s;
}

.btn:hover {
  color: var(--text-primary);
  background: var(--surface-card);
}

.btn:focus {
  outline: 2px solid var(--border-color);
  outline-offset: 2px;
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  pointer-events: none;
}

.btn-secondary {
  background: var(--surface-card);
}

.btn-secondary:hover {
  background: var(--bg-elev1);
}
```

**Tokens Used:**
- `colors.bg.elev1`
- `colors.surface.card`
- `colors.text.muted`
- `colors.text.primary`
- `colors.border.neutral`
- `borders.thin`
- `radii.sm`
- `spacing.sm`
- `spacing.lg`
- `fontFamily.ui`
- `fontSize.md`

---

## Component 5: Alert

**Purpose:** Display error messages, warnings, or informational messages

**Props:**
- `children`: React node (message content)
- `variant`: `"error" | "warning" | "info"` (default: `"info"`)
- `role`: `"alert" | "status"` (default: `"alert"`)
- `className`: string (optional) — Additional CSS classes

**Variants:**
- `error`: Error state (validation failures)
- `warning`: Warning state (power < 80%, inconclusive results)
- `info`: Informational state (general messages)

**Visual Spec:**
- Background: `var(--surface-card)` (`colors.surface.card`)
- Border: `var(--border-w) solid var(--border-color)` (`borders.thin`, `colors.border.neutral`)
- Border-radius: `var(--r-sm)` (`radii.sm` = 4px)
- Padding: `var(--space-1)` (1rem) (`spacing.md`)
- Font: `var(--font-ui)` (`fontFamily.ui`)
- Font-size: `0.875rem` (`fontSize.md`)
- Color: `var(--text-subtle)` (`colors.text.subtle`)
- Margin-bottom: `var(--space-1)` (`spacing.md`)

**States:**
- Default: As specified
- No hover/focus states (static message)

**Accessibility:**
- `role="alert"` for error messages (live region)
- `role="status"` for informational messages
- Icon prefix (optional): ❌ (error), ⚠️ (warning), ℹ️ (info)

**Example Usage:**
```html
<div role="alert" class="alert alert-error">
  ❌ Error: Success count cannot exceed total count for any variant.
</div>

<div role="status" class="alert alert-warning">
  ⚠️ Power is below the recommended 80% threshold. Consider increasing sample sizes.
</div>
```

**CSS Implementation:**
```css
.alert {
  background-color: var(--surface-card);
  border: var(--border-w) solid var(--border-color);
  border-radius: var(--r-sm);
  padding: var(--space-1);
  color: var(--text-subtle);
  font-family: var(--font-ui);
  font-size: 0.875rem;
  margin-bottom: var(--space-1);
}

.alert-error {
  /* Additional styling if needed — derived from style.md */
  border-left: 4px solid var(--accent-success); /* Derived — see Style Decisions Log */
}

.alert-warning {
  /* Same as default for now — can be enhanced */
}
```

**Tokens Used:**
- `colors.surface.card`
- `colors.border.neutral`
- `colors.text.subtle`
- `colors.accent.success` (error border — derived)
- `borders.thin`
- `radii.sm`
- `spacing.md`
- `fontFamily.ui`
- `fontSize.md`

---

## Component 6: Metric Display

**Purpose:** Display statistical metric (conversion rate, z-statistic, p-value, etc.)

**Props:**
- `label`: string (required) — Metric label
- `value`: string | number (required) — Metric value (formatted)
- `delta`: string | number (optional) — Delta/change indicator (e.g., "+0.640 pp")
- `deltaColor`: `"positive" | "negative" | "neutral"` (default: `"neutral"`)
- `className`: string (optional) — Additional CSS classes

**Variants:**
- Default: Standard metric
- `deltaPositive`: Delta with positive indicator (green)
- `deltaNegative`: Delta with negative indicator (dim)
- `deltaNeutral`: Delta with neutral indicator

**Visual Spec:**
- Container:
  - Display: `flex`, `flex-direction: column`
  - Gap: `var(--space-0_5)` (0.5rem) (`spacing.xs`)
- Label:
  - Font: `var(--font-ui)`
  - Size: `0.875rem` (`fontSize.md`)
  - Color: `var(--text-subtle)` (`colors.text.subtle`)
  - Text-transform: `none` (not uppercase)
- Value:
  - Font: `var(--font-ui)`
  - Size: `1.5rem` (or `fontSize.lg` scaled, ~1.5 × base)
  - Color: `var(--text-primary)` (`colors.text.primary`)
  - Font-weight: `normal` (monospace default)
- Delta:
  - Font: `var(--font-ui)`
  - Size: `0.75rem` (`fontSize.sm`)
  - Color:
    - Positive: `var(--accent-success)` (`colors.accent.success`)
    - Negative: `var(--text-dim)` (`colors.text.dim`)
    - Neutral: `var(--text-subtle)` (`colors.text.subtle`)

**States:**
- Default: As specified
- Empty: Show placeholder "—" in `var(--text-dim)`

**Accessibility:**
- Semantic HTML: `<div>` or `<dl><dt><dd>`
- `aria-label` for screen reader context

**Example Usage:**
```html
<div class="metric">
  <span class="metric-label">Conversion Rate</span>
  <span class="metric-value">0.0246 (2.46%)</span>
  <span class="metric-delta metric-delta-positive">+0.640 pp</span>
</div>
```

**CSS Implementation:**
```css
.metric {
  display: flex;
  flex-direction: column;
  gap: var(--space-0_5);
}

.metric-label {
  font-family: var(--font-ui);
  font-size: 0.875rem;
  color: var(--text-subtle);
}

.metric-value {
  font-family: var(--font-ui);
  font-size: 1.5rem;
  color: var(--text-primary);
}

.metric-delta {
  font-family: var(--font-ui);
  font-size: 0.75rem;
}

.metric-delta-positive {
  color: var(--accent-success);
}

.metric-delta-negative {
  color: var(--text-dim);
}

.metric-delta-neutral {
  color: var(--text-subtle);
}
```

**Tokens Used:**
- `colors.text.primary`
- `colors.text.subtle`
- `colors.text.dim`
- `colors.accent.success`
- `spacing.xs`
- `fontFamily.ui`
- `fontSize.sm`
- `fontSize.md`
- `fontSize.lg` (scaled)

---

## Component 7: Accordion / Expandable Section

**Purpose:** Collapsible section for detailed information (FAQ, explanations)

**Props:**
- `title`: string (required) — Section title
- `children`: React node (content)
- `defaultExpanded`: boolean (default: false) — Initially expanded
- `onToggle`: function (optional) — Toggle handler
- `id`: string (optional) — Unique ID

**Variants:**
- Default: Standard accordion

**Visual Spec:**
- Container:
  - Border-bottom: `var(--border-w) solid var(--border-color)` (`borders.thin`, `colors.border.neutral`)
  - Background: `transparent`
  - Transition: `background-color 0.15s`
- Trigger Button:
  - Font: `var(--font-ui)`
  - Size: `0.75rem` (`fontSize.sm`)
  - Text-transform: `uppercase`
  - Letter-spacing: `0.05em`
  - Color: `var(--text-muted)` (`colors.text.muted`)
  - Background: `transparent`
  - Border: `none`
  - Padding: `1.25rem 1.75rem` (`spacing.lg` + custom)
  - Width: `100%`
  - Display: `flex`, `justify-content: space-between`, `align-items: center`
  - Cursor: `pointer`
- Content:
  - Font: `var(--font...`)
  - Size: `0.8rem` (derived — see Style Decisions Log)
  - Color: `var(--text-subtle)` (`colors.text.subtle`)
  - Line-height: `1.5`
  - Padding: `0 1.75rem 1.25rem` (top 0, sides/bottom custom)
  - Display: `none` (collapsed) or `block` (expanded)

**States:**
- **Default (Collapsed):**
  - Content: `display: none`
  - Chevron: Right-pointing (►)
- **Expanded:**
  - Content: `display: block`
  - Chevron: Down-pointing (▼)
  - Button color: `var(--text-primary)` (on hover/active)
- **Hover (Trigger):**
  - Background: `#18181b` (from `style.md` FAQ pattern)
  - Color: `var(--text-primary)` (`colors.text.primary`)

**Accessibility:**
- Semantic HTML: Use `<details>` and `<summary>` if possible, or ARIA `aria-expanded`
- `aria-controls={contentId}` on trigger
- `id={contentId}` on content
- Keyboard: Enter/Space to toggle

**Example Usage:**
```html
<div class="faq-item">
  <button
    class="faq-q"
    aria-expanded={isExpanded}
    aria-controls="faq-content-1"
    onClick={handleToggle}
  >
    <span>📖 UNDERSTANDING THE RESULTS</span>
    <span>{isExpanded ? '▼' : '►'}</span>
  </button>
  <div
    id="faq-content-1"
    class="faq-a"
    style={{ display: isExpanded ? 'block' : 'none' }}
  >
    Content here...
  </div>
</div>
```

**CSS Implementation:**
```css
.faq-item {
  border-bottom: var(--border-w) solid var(--border-color发);
最佳 transition: background-color 0.15s;
}

.faq-item:hover {
  background: #18181b;
}

.faq-q {
  width: 100%;
  background: transparent;
  border: none;
  padding: 1.25rem 1.75rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-1);
  font-family: var(--font-ui);
  font-size: 0.75rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  transition: color 0.15s;
}

.faq-q:hover {
  color: var(--text-primary);
}

.faq-a {
  display: none;
  font-family: var(--font-ui);
  font-size: 0.8rem;
  color: var(--text-subtle);
  line-height: 1.5;
  padding: 0 1.75rem 1.25rem;
}

.faq-a.active {
  display: block;
}
```

**Tokens Used:**
- `colors.text.muted`
- `colors.text.primary`
- `colors.text.subtle`
- `colors.border.neutral`
- `borders.thin`
- `spacing.md`
- `spacing.lg`
- `fontFamily.ui`
- `fontSize.sm`
- FAQ hover background: `#18181b` (from `style.md`)

---

## Component 8: Label / Section Heading

**Purpose:** Uppercase label for sections (VARIANT A, OVERVIEW, etc.)

**Props:**
- `children`: string (label text)
- `size`: Kay: `"sm" | "md" | "lg"` (default: `"sm"`)
- `className`: string (optional) — Additional CSS classes

**Variants:**
- `meta-sm`: Small label (0.75rem)
- `meta-md`: Medium label (0.875rem)
- `tagline`: Large label (1rem, centered)

**Visual Spec:**
- Font: `var(--font-ui)` (`fontFamily.ui`)
- Text-transform: `uppercase`
- Letter-spacing: `0.05em`
- Color: `var(--text-muted)` (`colors.text.muted`)
- Font-size:
  - `sm`: `0.75rem` (`fontSize.sm`)
  - `md`: `0.875rem` (`fontSize.md`)
  - `lg`: `1rem` (`fontSize.base`)
- Margin-bottom: `var(--space-1)` (`spacing.md`) or `var(--space-0_75)` (`spacing.sm`)

**States:**
- Default: As specified
- No interactive states

**Accessibility:**
- Semantic HTML: Use `<h2>`, `<h3>`, or `<label>` as appropriate
- `aria-label` if needed for context

**Example Usage:**
```html
<h2 class="meta-sm">VARIANT A (CONTROL)</h2>
<h1 class="tagline">A/B TEST ANALYZER</h1>
```

**CSS Implementation:**
```css
.meta-sm,
.m текст,
.label,
.nav {
  font-family: var(--font-ui);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-muted);
}

.meta-sm {
  font-size: 0.75rem;
  margin-bottom: var(--space-0_75);
}

.meta-md {
  font-size: 0.875rem;
  margin-bottom: var(--space-1);
}

.tagline {
  font-size: 1rem;
  text-align: center;
  margin-bottom: var(--space-1);
}
```

**Tokens Used:**
- `colors.text.muted`
- `fontFamily.ui`
- `fontSize.sm`
- `fontSize.md`
- `fontSize.base`
- `spacing.sm`
- `spacing.md`

---

## Component 9: Decision Banner

**Purpose:** Prominent display of test decision (B Wins / Inconclusive / A Better)

**Props:**
- `decision`: `"b-wins" | "inconclusive-positive" | "a-better" | "inconclusive-zero"` (required)
- `message`: string (optional) — Custom message
- `className`: string (optional) — Additional CSS classes

**Variants:**
- `b-wins`: Success state (green, ✅)
- `inconclusive-positive`: Warning state (yellow/subtle, ⚠️)
- `a-better`: Info state (dim, ℹ️)
- `inconclusive-zero`: Warning state (subtle, ⚠️)

**Visual Spec:**
- Container:
  - Background: `var(--surface-card)` (`colors.surface.card`)
  - Border: `var(--border-outer-w) solid var(--border-color)` (`borders.outer`, `colors.border.neutral`)
  - Border-left (B Wins only): `4px solid var(--accent-success)` (derived pattern)
  - Border-radius: `var(--r-md)` (`radii.md`)
  - Padding: `var(--space-2)` (`spacing.xl`)
  - Margin-bottom: `var(--space-1_5)` (`spacing.lg`)
- Text:
  - Font: `var(--font-ui)`
  - Size: `1rem` (`fontSize.base`)
  - Color:
    - B Wins: `var(--accent-success)` (`colors.accent.success`)
    - Inconclusive: `var(--text-subtle)` (`colors.text.subtle`)
    - A Better: `var(--text-dim)` (`colors.text.dim`)
  - Icon: Prefix with emoji or SVG (✅, ⚠️, ℹ️)

**States:**
- Default: As specified
- No hover/focus states (static message)

**Accessibility:**
- Semantic HTML: `<div role="status">` or `<div role="alert">`
- `aria-live="polite"` for status updates

**Example Usage:**
```html
<div class="decision-banner decision-b-wins" role="status">
  ✅ <strong>VARIANT B WINS</strong> — Statistically significant improvement detected.
</div>
```

**CSS Implementation:**
```css
.decision-banner {
  background-color: var(--surface-card);
  border: var(--border-outer-w) solid var(--border-color);
  border-radius: var(--r-md);
  padding: var(--space-2);
  margin-bottom: var(--space-1_5);
  font-family: var(--font-ui);
  font-size: 1rem;
}

.decision-b-wins {
  color: var(--accent-success);
  border-left: 4px solid var(--accent-success);
}

.decision-inconclusive {
  color: var(--text-subtle);
}

.decision-a-better {
  color: var(--text-dim);
}
```

**Tokens Used:**
- `colors.surface.card`
- `colors.accent.success`
-瓷砖`colors.text.subtle`
- `colors.text.dim`
- `colors.border.neutral`
- `borders.outer`
- `radii.md`
- `spacing.lg`
- `spacing.xl`
- `fontFamily.ui`
- `fontSize.base`

---

## Component Summary Table

| Component | Primary Tokens | Derived Tokens | States |
|-----------|---------------|----------------|--------|
| Card | `surface.card`, `border.neutral`, `borders.outer`, `radii.md` | — | Default |
更深| Number Input | `bg.black`, `text.primary`, `border.neutral`, `radii.sm` | Error border (see Log) | Default, Focus, Error, Disabled |
| Slider | `bg.elev1`, `text.muted`, `border.neutral` | — | Default, Focus, Active, Disabled |
| Button | `text.muted`, `border.neutral`, `radii.sm` | Hover background | Default, Hover, Focus, Active, Disabled |
| Alert | `surface.card`, `text.subtle`, `border.neutral` | Error border accent | Default |
| Metric Display | `text.primary`, `text.subtle`, `accent.success` | — | Default, Empty |
| Accordion | `text.muted`, `border.neutral`, FAQ hover color | — | Collapsed, Expanded, Hover |
| Label | `text.muted`, `fontSize.sm/md/base` | — | Default |
| Decision Banner | `surface.card`, `accent.success`, `text.subtle` | Left border accent | Default |

---

**Next:** See `05-function-to-ui-mapping.md` for backend function → UI trigger mappings and data contracts.

