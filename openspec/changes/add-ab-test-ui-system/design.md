## Context
Single source of truth is `style.md` for all visuals and interactions. Current UI is Streamlit-based; we will specify system-agnostic tokens and patterns that can be applied in Streamlit or any future web UI.

## Goals / Non-Goals
- Goals: Reusable component library, precise token mapping, accessible flows, responsive rules
- Non-Goals: Theming beyond dark mode; adding new tokens not derivable from `style.md`

## Information Architecture
- Global: `Home (Analyzer)`
  - Input Panel (A/B counts, alpha, MDE)
  - Results: Metrics (z, p, lift), 95% CI, Decision, Power
  - Learn More: Explanation tooltip/expander

## Navigation & Routing
- Single-page layout with primary content area and sidebar (or stacked on mobile). Breadcrumbs unnecessary for now.

## Layout and Grid
- Page wrapper uses `--bg-elev1`; content inside `.container` with `min(1100px, 90vw)`
- Cards for sections with outer ring and subtle shadow per `style.md` `.card`
- `grid-tiles` for key feature tiles when needed; responsive 2 → 4 columns at 768px

## Components (Visual + Behavior)
- Card: background `--surface-card`; shadow ring `--border-outer-w` + `--border-color`
- Inputs (number, slider): label style uses uppercase mono (`.label` semantics), spacing via `--space-*`
- Metrics: numeric emphasis with default text styles; muted labels `--text-muted`
- Tooltip: `.tooltip-trigger` + `.tooltip` as in `style.md`; hover on desktop, tap-activate on mobile
- Buttons/Links: `.link` styles; copy/CTA as inline link patterns
- Toast/Status: success uses `--accent-success`; info/warning use text colors with borders; no new colors introduced
- Focus: `:focus-visible` outline `2px` in `--border-color` on `--surface-card`

## Typography
- UI fonts: `--font-ui`; uppercase meta/labels with 0.05em tracking; sizes from `fontSize` map (xs/sm/md/lg)

## Spacing and Radii
- Radii `--r-sm`/`--r-md` as needed; spacing tokens `--space-*`

## Motion
- Transitions under 200ms; use hover/opacity transitions from `style.md` examples

## Token Mapping
- Colors: `--bg-black`, `--bg-elev1`, `--surface-card`, `--text-*`, `--accent-success`, `--border-color`
- Borders: `--border-w`, `--border-outer-w`
- Shadow: `--shadow-tint`
- Font and sizes: `--font-ui`, `--fs-base`; use `.meta-sm`, `.meta-md`

## Accessibility
- Keyboard-tab order preserved; all interactive elements keyboard-activatable
- ARIA: tooltips use `aria-describedby`; metrics have clear labels; error states use role="alert"
- Contrast: white-on-black with muted/subtle variants satisfies AA

## Open Questions
- None blocking; derivations recorded in Style Decisions Log


