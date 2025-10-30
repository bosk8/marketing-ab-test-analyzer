## Style Compliance Matrix

Screen/Component → Tokens Used

- Page Wrapper
  - Background: `--bg-elev1`
  - Font: `--font-ui`, base size `--fs-base`

- Container
  - Width: `min(1100px, 90vw)` per `style.md` `.container`

- Cards (Sections: Inputs, Metrics, Results)
  - Surface: `--surface-card`
  - Border ring: `--border-outer-w` + `--border-color`
  - Shadow: `--shadow-tint`
  - Radius: `--r-md`

- Labels / Meta
  - Typography: uppercase mono (`.label` pattern)
  - Color: `--text-muted`
  - Tracking: 0.05em (per `.tagline, .meta, .label, .nav`)

- Body Text
  - Color: `--text-primary` / `--text-subtle` (secondary)

- Links
  - Class: `.link`; hover → `--text-primary`

- Inputs
  - Spacing: `--space-0_5`, `--space-1`, `--space-1_5`
  - Focus: `:focus-visible` outline `--border-color`

- Tooltips
  - Structure: `.tooltip-trigger`, `.tooltip`
  - Border: `--border-w` + `--border-color`
  - Surface: `--surface-card`
  - Text: `--text-subtle`
  - Motion: opacity/visibility < 200ms

- Grid Tiles (Optional summary)
  - Pattern: `.grid-tiles` 2→4 columns @ 768px

- Success State
  - Accent color: `--accent-success`


