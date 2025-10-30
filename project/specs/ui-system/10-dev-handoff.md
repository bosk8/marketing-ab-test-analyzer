# Developer Handoff Artifacts

**Version:** 1.0  
**Date:** 2025-01-27  
**Style Reference:** `style.md`

This document provides implementation-ready artifacts for developers: CSS token map, spacing redlines, code snippets, and acceptance checklist.

---

## 1. CSS Variables (Design Tokens)

### Complete Token Map

Copy this entire block to your root CSS file or `:root` selector:

```css
:root {
  /* Typography */
  --font-ui: JetBrains Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, DejaVu Sans Mono, Courier New, monospace;
  --fs-base: clamp(16px, calc(15.2px + 0.25vw), 20px);

  /* Colors */
  --bg-black: #000;
  --bg-elev1: #0A0A0A;
  --surface-card: #09090B;
  --text-primary: #fff;
  --text-muted: #e8e8e8;
  --text-subtle: #a1a1aa;
  --text-dim: #71717a;
  --text-highlight: #f4f4f5;
  --accent-success: #22c55e;
  --border-color: rgb(39 39 42);
  --shadow-tint: #0000000d;

  /* Borders */
  --border-w: 1px;
  --border-outer-w: 1px;

  /* Radii */
  --r-sm: 4px;
  --r-md: 6px;

  /* Spacing */
  --space-0_5: 0.5rem;
  --space-0_75: 0.75rem;
  --space-1: 1rem;
  --space-1_5: 1.5rem;
  --space-2: 2rem;
  --space-4: 4rem;

  /* Layout */
  --container-max: min(1100px, 90vw);
}

/* Responsive Border Widths */
@media (min-width: 1024px) {
  :root {
    --border-w: 1.5px;
    --border-outer-w: 2px;
  }
}
```

**Note:** Typo in font stack ("한다ospace" → "monospace") — fix in implementation.

---

## 2. Global Resets & Base Styles

```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-size: var(--fs-base);
}

html, body {
  margin: 0;
  width: 100%;
  height: 100%;
  background-color: var(--bg-black);
  font-family: var(--font-ui);
  color: var(--text-primary);
}

/* Focus Visible (Accessibility Override) */
:focus-visible {
  outline: 2px solid var(--text-muted); /* Changed from --border-color for contrast */
  outline-offset: 2px;
}
```

---

## 3. Component CSS Snippets

### Card Component

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
  box-shadow: none;
}

.card.border-r {
  border-right: var(--border-w) solid var(--border-color);
  box-shadow: none;
}
```

### Number Input Component

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
  outline: 2px solid var(--text-muted);
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

### Button Component

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
  outline: 2px solid var(--text-muted);
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

### Alert Component

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
  border-left: 4px solid var(--accent-success); /* Derived — see Style Decisions Log */
}
```

### Metric Display Component

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
  color: var(--text-subtle); /* Changed from text-dim for contrast */
}

.metric-delta-neutral {
  color: var(--text-subtle);
}
```

### Label / Section Heading

```css
.meta-sm,
.meta-md,
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

### Accordion Component (FAQ Pattern)

```css
.faq-item {
  border-bottom: var(--border-w) solid var(--border-color);
  transition: background-color 0.15s;
}

.faq-item:hover {
  background: #18181b; /* From style.md FAQ pattern */
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
  font-size: 0.8rem; /* Derived — see Style Decisions Log */
  color: var(--text-subtle);
  line-height: 1.5;
  padding: 0 1.75rem 1.25rem;
}

.faq-a.active {
  display: block;
}
```

---

## 4. Spacing Redlines

### Component Spacing Hierarchy

| Element | Spacing | Value | Usage |
|---------|---------|-------|-------|
| Card padding (default) | `--space-2` | `2rem` | Standard card content padding |
| Card padding (small) | `--space-1` | `1rem` | Compact cards |
| Card margin-bottom | `--space-1_5` | `1.5rem` | Spacing between stacked cards |
| Input padding | `--space-0_75` | `0.75rem` | Number input internal padding |
| Input margin-bottom | `--space-1` | `1rem` | Spacing below inputs |
| Label margin-bottom | `--space-0_75` | `0.75rem` | Spacing below meta-sm labels |
| Button padding | `--space-0_75` / `--space-1_5` | `0.75rem` / `1.5rem` | Vertical / horizontal button padding |
| Metric gap | `--space-0_5` | `0.5rem` | Gap between label and value in metrics |

### Layout Spacing

| Element | Spacing | Value | Usage |
|---------|---------|-------|-------|
| Container max-width | `--container-max` | `min(1100px, 90vw)` | Main content container |
| Container padding (top) | `--space-4` | `4rem` | Top padding for hero spacing |
| Container padding (sides) | `--space-1` | `1rem` | Side padding (mobile) |
| Sidebar width | Fixed | `~300px` | Desktop sidebar width |

---

## 5. React Component Examples

### Card Component (React)

```tsx
import React from 'react';

interface CardProps {
  children: React.ReactNode;
  padding?: 'sm' | 'md' | 'lg';
  borderBottom?: boolean;
  borderRight?: boolean;
  className?: string;
}

export const Card: React.FC<CardProps> = ({
  children,
  padding = 'md',
  borderBottom = false,
  borderRight = false,
  className = '',
}) => {
  const paddingClass = {
    sm: 'space-1',
    md: 'space-2',
    lg: 'space-4',
  }[padding];

  return (
    <section
      className={`card ${paddingClass} ${
        borderBottom ? 'border-b' : ''
      } ${borderRight ? 'border-r' : ''} ${className}`}
    >
      {children}
    </section>
  );
};
```

### Number Input Component (React)

```tsx
import React from 'react';

interface NumberInputProps {
  label: string;
  value: number | string;
  onChange: (value: number) => void;
  min?: number;
  max?: number;
  step?: number;
  placeholder?: string;
  error?: boolean;
  errorMessage?: string;
  required?: boolean;
  id?: string;
}

export const NumberInput: React.FC<NumberInputProps> = ({
  label,
  value,
  onChange,
  min = 0,
  max,
  step = 1,
  placeholder,
  error = false,
  errorMessage,
  required = false,
  id,
}) => {
  const inputId = id || `input-${label.toLowerCase().replace(/\s+/g, '-')}`;
  const errorId = `${inputId}-error`;

  return (
    <div>
      <label htmlFor={inputId} className="meta-sm">
        {label}
        {required && <span aria-label="required">*</span>}
      </label>
      <input
        type="number"
        id={inputId}
        value={value}
        onChange={(e) => onChange(Number(e.target.value))}
        min={min}
        max={max}
        step={step}
        placeholder={placeholder}
        className={error ? 'error' : ''}
        aria-describedby={error ? errorId : undefined}
        aria-invalid={error}
        aria-required={required}
      />
      {error && errorMessage && (
        <div id={errorId} role="alert" className="alert alert-error">
          {errorMessage}
        </div>
      )}
    </div>
  );
};
```

---

## 6. Acceptance Checklist

### Visual Design
- [ ] All colors match `style.md` token values
- [ ] Typography uses JetBrains Mono font stack
- [ ] All spacing uses `style.md` spacing tokens
- [ ] Border widths responsive (1px mobile → 1.5px desktop)
- [ ] Card shadows match spec (outer border + subtle shadow)

### Components
- [ ] Card component renders with correct styling
- [ ] Number inputs have proper focus states (2px outline, text-muted)
- [ ] Buttons have hover/focus/disabled states
- [ ] Alerts display with error variant styling
- [ ] Metrics display with correct label/value/delta formatting
- [ ] Accordion expands/collapses correctly
- [ ] Labels use uppercase transform and letter-spacing

### Responsive Behavior
- [ ] Desktop (≥1024px): Sidebar fixed width, two-column main content
- [ ] Tablet (768px-1023px): Sidebar visible, border widths adjusted
- [ ] Mobile (<768px): Sidebar collapses to drawer, content stacks vertically

### Accessibility
- [ ] Focus indicators visible (2px outline, text-muted color)
- [ ] All inputs have associated labels
- [ ] Error messages use `role="alert"`
- [ ] Keyboard navigation works (Tab, Enter, Space)
- [ ] Screen reader announces labels and errors
- [ ] Color contrast meets WCAG AA (text-subtle or higher for body text)

### Functionality
- [ ] Real-time calculation on input change (debounced 100ms)
- [ ] CSV upload populates sidebar inputs
- [ ] Error validation displays alerts
- [ ] Decision banner shows correct variant based on results
- [ ] Power analysis updates when MDE/alpha changes

### Performance
- [ ] Calculation latency < 100ms for typical inputs
- [ ] Page load < 2s on 3G connection
- [ ] No layout shift on calculation

---

## 7. Known Limitations & Future Enhancements

### Limitations (Current)
1. **Error Color:** Uses green (`accent.success`) for errors (see Style Decisions Log)
2. **No Export:** Results cannot be exported (PDF/JSON)
3. **No History:** Test results are not saved
4. **No Power Curve:** Power analysis is text-only (no visualization)

### Future Enhancements
1. Add `colors.accent.error` and `colors.accent.warning` to `style.md`
2. Export functionality (PDF report, JSON data)
3. Historical test tracking / saved sessions
4. Power curve visualization
5. ROI calculation inputs (monthly visits, value per visit)

---

## 8. Implementation Notes

### Streamlit Integration
- Current app uses inline CSS via `st.markdown()` with `unsafe_allow_html=True`
- Consider migrating to React/Next.js for full design system control
- CSS variables can be injected into Streamlit via `st.markdown()` in `<style>` tag

### Testing Recommendations
1. **Visual Regression:** Use Percy or Chromatic for component snapshots
2. **Accessibility:** Run axe DevTools and WAVE scans
3. **Cross-Browser:** Test Chrome, Firefox, Safari, Edge
4. **Responsive:** Test mobile (320px), tablet (768px), desktop (1024px+)

---

**End of Developer Handoff Artifacts**

For questions or clarifications, refer to:
- `style.md` — Design system reference
- `09-style-decisions-log.md` — Assumptions and derivations
- `07-accessibility-checklist.md` — WCAG compliance details

