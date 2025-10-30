# Accessibility Checklist — WCAG 2.2 AA Compliance

**Version:** 1.0  
**Date:** 2025-01-27  
**Style Reference:** `style.md`

This checklist ensures the A/B Test Analyzer UI meets WCAG 2.2 Level AA standards.

---

## 1. Perceivable

### 1.1 Text Alternatives
- [ ] **1.1.1 Non-text Content (Level A)**
  - Images/icons have alt text or `aria-label`
  - Decorative icons have `aria-hidden="true"`
  - Status icons (✅, ⚠️, ℹ️) have `aria-label` or text alternative
  - **Implementation:** Use emoji with `aria-label` or replace with SVG icons

### 1.2 Time-based Media
- [ ] **N/A** — No time-based media in application

### 1.3 Adaptable
- [ ] **1.3.1 Info and Relationships (Level A)**
  - Use semantic HTML: `<label>`, `<input>`, `<button>`, `<section>`, `<h1>`-`<h6>`
  - Form inputs associated with labels via `for` attribute or `aria-label`
  - **Example:** `<label for="success-a">Successes (conversions)</label>`
- [ ] **1.3.2 Meaningful Sequence (Level A)**
  - Content order matches DOM order (sidebar → main content)
  - Mobile: Ensure logical reading order when sidebar collapses
- [ ] **1.3.3 Sensory Characteristics (Level A)**
  - Do not rely solely on color to convey information
  - **Example:** Error states use border color + icon + text message
  - **Example:** Decision banner uses color + icon + text

### 1.4 Distinguishable
- [ ] **1.4.3 Contrast (Minimum) — Level AA**
  - **Text Contrast Ratios:**
    - `--text-primary` (#FFFFFF) on `--bg-black` (#000000): 21:1 ✅ (exceeds AA 4.5:1)
    - `--text-muted` (#E8E8E8) on `--bg-black` (#000000): 13.5:1 ✅
    - `--text-subtle` (#A1A1AA) on `--bg-black` (#000000): 5.3:1 ✅
    - `--text-dim` (#71717A) on `--bg-black` (#000000): 3.7:1 ❌ (below 4.5:1)
      - **Action:** Use `--text-subtle` instead of `--text-dim` for body text
      - **OK for:** Non-essential UI elements (borders, icons)
  - **Large Text Contrast (18pt+ or 14pt+ bold):**
    - All large text meets 3:1 ratio ✅
  - **Interactive Elements:**
    - Buttons: `--text-muted` (#E8E8E8) on `--bg-black`: 13.5:1 ✅
    - Links: `--text-muted` with hover to `--text-primary`: 13.5:1 → 21:1 ✅
- [ ] **1.4.4 Resize Text (Level AA)**
  - Text can be resized up to 200% without loss of functionality
  - **Implementation:** Use relative units (`rem`, `em`, `%`), avoid fixed `px` for text
  - Font-size base: `clamp(16px, calc(15.2px + 0.25vw), 20px)` — responsive ✅
- [ ] **1.4.5 Images of Text (Level AA)**
  - No images of text (use actual text)
  - Icons are SVG or emoji (not image files)

---

## 2. Operable

### 2.1 Keyboard Accessible
- [ ] **2.1.1 Keyboard (Level A)**
  - All functionality available via keyboard
  - **Inputs:** Tab to focus, arrow keys for number increment/decrement
  - **Sliders:** Arrow keys to adjust, Home/End for min/max
  - **Buttons:** Enter/Space to activate
  - **Accordion:** Enter/Space to toggle
- [ ] **2.1.2 No Keyboard Trap (Level A)**
  - Tab order does not trap users in any component
  - **Sidebar:** Mobile drawer must allow escape via Tab or Close button
- [ ] **2.1.4 Character Key Shortcuts (Level A) — NEW in WCAG 2.2**
  - If keyboard shortcuts exist, provide way to turn off or remap
  - **Status:** No keyboard shortcuts in MVP; if added, provide settings

### 2.2 Enough Time
- [ ] **2.2.1 Timing Adjustable (Level A)**
  - No time limits on user input ✅
- [ ] **2.2.2 Pause, Stop, Hide (Level A)**
  - No auto-updating content ✅

### 2.3 Seizures and Physical Reactions
- [ ] **2.3.1 Three Flashes or Below Threshold (Level A)**
  - No flashing content ✅

### 2.4 Complement
- [ ] **2.4.1 Bypass Blocks (Level A)**
  - Skip to main content link (if page length > 3000px)
  - **Status:** Single-page app, short content — skip link optional
- [ ] **2.4.2 Page Titled (Level A)**
  - Page has descriptive title: `<title>A/B Test Analyzer</title>` ✅
- [ ] **2.4.3 Focus Order (Level A)**
  - Tab order follows visual/logical order:
    1. Sidebar inputs (Variant A → Variant B → Parameters)
    2. Main content (results, Meterics)
  - **Implementation:** Ensure DOM order matches visual order
- [ ] **2.4.4 Link Purpose (In Context) (Level A)**
  - Links have descriptive text
  - **Status:** Minimal links in app; ensure descriptive `aria-label` if icon-only
- [ ] **2.4.5 Multiple Ways (Level AA)**
  - Multiple ways to find content (site map, search, navigation)
  - **Status:** Single-page app — not applicable
- [ ] **2.4.6 Headings and Labels (Level AA)**
  - Headings and labels are descriptive
  - **Example:** "Successes (conversions)" not just "Successes"
  - **Example:** "VARIANT A (CONTROL)" clearly identifies control group
- [ ] **2.4.7 Focus Visible (Level AA)**
  - **Focus Indicator:**
    - Outline: `2px solid var(--border-color)` (`--border-color`: rgb(39 39 42))
    - Outline-offset: `2px`
    - **Contrast:** Border color (#27272A) on `--bg-black` (#000000): 2.1:1 ❌
      - **Action:** Use `--text-muted` (#E8E8E8) for focus outline for sufficient contrast
      - **Implementation:** `outline: 2px solid var(--text-muted); outline-offset: 2px;`
  - All interactive elements have visible focus indicator

---

## 3. Understandable

### 3.1 Readable
- [ ] **3.1.1 Language of Page (Level A)**
  - HTML lang attribute: `<html lang="en">` ✅
- [ ] **3.1.2 Language of Parts (Level AA)**
  - If content in other language, use `lang` attribute
  - **Status:** All content in English

### 3.2 Predictable
- [ ] **3.2.1 On Focus (Level A)**
  - No context changes on focus ✅
- [ ] **3.2.2 On Input (Level A)**
  - **Auto-calculation on input change:**
    - User expects results to update automatically ✅
    - No unexpected navigation or context changes
- [ ] **3.2.3 Consistent Navigation (Level AA)**
  - Navigation is consistent across pages
  - **Status:** Single-page app — navigation consistent (none)
- [ ] **3.2.4 Consistent Identification (Level AA)**
  - Components with same functionality have consistent labels
  - **Example:** "Successes (conversions)" consistent across Variant A and B

### 3.3 Input Assistance
- [ ] **3.3.1 Error Identification (Level A)**
  - **Error Messages:**
    - Clearly identify input with error
    - Describe error in text
    - **Example:** Alert component: "Error: Success count cannot exceed total count for any variant."
    - Input highlighted with error state (red border)
- [ ] **3.3.2 Labels or Instructions (Level A)**
  - **Labels:**
    - All inputs have associated labels (`<label for={id}>` or `aria-label`)
    - Required fields indicated (visual + `aria-required="true"`)
    - Instructions provided where needed (e.g., "Enter success count")
- [ ] **3.3.3 Sasistance Suggestions (Level AA)**
  - **Error Suggestions:**
    - Provide suggestions for correcting errors
    - **Example:** "Error: Success count cannot exceed total count. Please enter a value ≤ {total_a}."
- [ ] **3.3.4 Error Prevention (Legal, Financial, Data) (Level AA)**
  - For submissions with legal/financial consequences, allow review/correction
  - **Status:** No submissions; results are calculations only

---

## 4. Robust

### 4.1 Compatible
- [ ] **4.1.1 Parsing (Level A)**
  - HTML is valid (no duplicate IDs, proper nesting)
  - **Implementation:** Use React keys, ensure unique IDs
- [ ] **4.1.2 Name, Role, Value (Level A)**
  - **ARIA Usage:**
    - Interactive elements have accessible name (`aria-label`, `aria-labelledby`)
    - Roles specified where needed (`role="alert"`, `role="status"`, `role="button"`)
    - States communicated (`aria-expanded`, `aria-invalid`, `aria-required`)
    - **Examples:**
      - Input with error: `aria-invalid="true"`, `aria-describedby={errorId}`
      - Accordion: `aria-expanded={isExpanded}`, `aria-controls={contentId}`
      - Alert: `role="alert"` for errors, `role="status"` for info
- [ ] **4.1.3 Status Messages (Level AA) — NEW in WCAG 2.2**
  - Status messages announced to screen readers
  - **Implementation:**
    - Use `role="alert"` for error messages (live region)
    - Use `role="status"` for decision banner updates (live region)
    - **Example:** Decision banner: `<div role="status" aria-live="polite">✅ VARIANT B WINS</div>`

---

## Component-Specific Checklist

### Number Input
- [ ] Label associated via `for` attribute or `aria-label`
- [ ] Error message associated via `aria-describedby`
- [ ] `aria-required="true"` if required
- [ ] `aria-invalid="true"` if error
- [ ] Keyboard accessible (Tab, arrow keys)
- [ ] Focus visible (2px outline)

### Slider (Range Input)
- [ ] Label associated
- [ ] `aria-valuemin`, `aria-valuemax`, `aria-valuenow` attributes
- [ ] Keyboard accessible (arrow keys, Home/End)
- [ ] Focus visible

### Button
- [ ] Accessible name (`aria-label` if icon-only)
- [ ] Keyboard accessible (Enter/Space)
- [ ] Focus visible
- [ ] `aria-disabled="true"` if disabled

### Alert
- [ ] `role="alert"` for errors (live region)
- [ ] `role="status"` for informational messages
- [ ] Clear, descriptive error text
- [ ] Associated with input via `aria-describedby` (if input error)

### Accordion
- [ ] `aria-expanded` attribute on trigger
- [ ] `aria-controls` pointing to content ID
- [ ] Keyboard accessible (Enter/Space to toggle)
- [ ] Focus visible

### Decision Banner
- [ ] `role="status"` or `role="alert"` (depending on importance)
- [ ] `aria-live="polite"` for dynamic updates
- [ ] Clear, descriptive text (not color-only)

---

## Testing Checklist

### Automated Testing
- [ ] **axe DevTools** or **WAVE** scan: 0 errors
- [ ] **Lighthouse Accessibility Score:** ≥ 95
- [ ] **HTML Validator:** No errors

### Manual Testing
- [ ] **Keyboard Navigation:** Tab through all interactive elements
- [ ] **Screen Reader:** Test with NVDA (Windows) or VoiceOver (macOS)
  - All labels announced
  - Error messages announced
  - Status updates announced
- [ ] **Focus Indicators:** Visible on all interactive elements
- [ ] **Color Contrast:** Verify text contrast ratios (see 1.4.3)
- [ ] **Zoom:** Test 200% zoom — no loss of functionality

### Browser Testing
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)

---

## Implementation Notes

### Focus Outline Derivation
- **Issue:** `--border-color` (#27272A) has insufficient contrast (2.1:1) for focus outline
- **Solution:** Use `--text-muted` (#E8E8E8) for focus outline
- **CSS:**
  ```css
  :focus-visible {
    outline: 2px solid var(--text-muted); /* Changed from --border-color */
    outline-offset: 2px;
  }
  ```
- **Logged in:** Style Decisions Log

### Text Dim Color Usage
- **Issue:** `--text-dim` (#71717A) has contrast ratio 3.7:1 (below 4.5:1)
- **Solution:** Use `--text-dim` only for non-essential UI (borders, icons), not body text
- **Body text:** Use `--text-subtle` (#A1A1AA, 5.3:1 contrast) or `--text-muted` (#E8E8E8, 13.5:1)
- **Logged in:** Style Decisions Log

---

**Next:** See `08-style-compliance-matrix.md` for per-component token usage matrix.

