# Navigation & Routing Model

**Version:** 1.0  
**Date:** 2025-01-27  
**Style Reference:** `style.md`

## Overview

The A/B Test Analyzer is a **single-page application (SPA)** with no client-side routing. All functionality exists on one view (`/`).

## Route Structure

```
/ (root)
  └─ Main Analysis Page (single view)
```

**No nested routes required** — all features accessible from root view.

## Global Navigation

**None** — single-page application eliminates need for global navigation menu.

## Secondary Navigation (Within Page)

### Scroll-to Sections (Future Enhancement)

If page length exceeds viewport height, optional jump links could be added:

```
┌─────────────────────────────────────┐
│  [Conversion Rates] [Results]      │
│  [Decision] [Power Analysis]       │
└─────────────────────────────────────┘
```

**Implementation Notes:**
- Use anchor links: `#conversion-rates`, `#results`, `#decision`, `#power`
- Style as subtle links (`var(--text-subtle)`, hover to `var(--text-primary)`)
- Not required for MVP; can be added if content grows

### Accordion Navigation

**Expandable Sections:**
- "Understanding the Results" accordion (FAQ pattern from `style.md`)
- Toggle via button click
- State: Collapsed by default, expand on click

**No breadcrumbs** — single level structure.

## Empty States & First-Run

### Empty State (No Data)

- **Location:** Main content area
- **Content:** Placeholder text: "Enter test data in the sidebar to begin analysis."
- **Action:** Optional "Load Sample Data" button (populates with sample_ab.csv data)
- **Visual:** Centered, `var(--text-subtle)` color, card background

### First-Run Experience

1. User lands on `/`
2. Sees hero section: "A/B TEST ANALYZER"
3. Overview card explains tool purpose
4. Sidebar inputs are empty with placeholders
5. Optional sample data button available

## Mobile Navigation

### Sidebar Toggle (Mobile < 768px)

- **Pattern:** Collapsible drawer/overlay
- **Trigger:** Hamburger menu button (`☰`) in header
- **Behavior:**
  - Sidebar hidden by default on mobile
  - Click menu button → Sidebar slides in from left (or overlays)
  - Click outside or close button → Sidebar closes
- **Styling:**
  - Drawer background: `var(--surface-card)`
  - Border: `var(--border-w) solid var(--border-color)`
  - Z-index: 100 (above main content)

**Implementation:**
- Toggle state: `sidebarOpen` (boolean)
- CSS: `transform: translateX(-100%)` (hidden) or `translateX(0)` (visible)
- Transition: `transform 0.15s ease`

## Route Rules

**N/A** — single route `/`.

## Future Routing Considerations

If multi-page features are added in future:

1. **History Page:** `/history` (saved test results)
2. **Settings Page:** `/settings` (user preferences)
3. **Help Page:** `/help` (documentation)

**Routing Strategy:**
- Use React Router or Next.js routing if framework migration occurs
- Maintain single-page simplicity for MVP

---

**Next:** See `07-accessibility-checklist.md` for WCAG 2.2 AA compliance checklist.

