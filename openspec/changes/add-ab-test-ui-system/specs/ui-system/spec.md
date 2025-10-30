## ADDED Requirements

### Requirement: Token-Driven UI
The system SHALL implement visuals and interactions strictly using tokens from `style.md` (colors, typography, spacing, borders, radii, shadows, motion).

#### Scenario: Apply global tokens
- **WHEN** the UI renders the main page
- **THEN** page background uses `--bg-elev1` and text uses `--text-primary`
- **AND** base font uses `--font-ui` with `--fs-base`

### Requirement: Layout and Surfaces
The system SHALL use `.container` with max width `min(1100px, 90vw)` and surface cards per `style.md` `.card` pattern.

#### Scenario: Section cards
- **WHEN** sections (Inputs, Metrics, Results) are displayed
- **THEN** each section is a `.card` with outer ring using `--border-outer-w` and `--border-color`

### Requirement: Inputs and Labels
The system SHALL render input controls (number, slider) with uppercase mono labels and adhere to spacing tokens.

#### Scenario: Number inputs
- **WHEN** entering `success` and `total` values
- **THEN** labels are uppercase with `.label` semantics (mono, letter-spacing 0.05em)
- **AND** spacing uses `--space-1` and `--space-1_5`

### Requirement: Metrics and Results
The system MUST display z, p, lift, and 95% CI with clear labels and accessible text.

#### Scenario: Significant result
- **WHEN** `p < alpha` AND CI lower bound > 0
- **THEN** show success status with accent `--accent-success` and text compliant with AA

### Requirement: Tooltip Behavior
The system SHALL implement tooltips per `.tooltip-trigger` and `.tooltip` with hover on desktop and tap-activate on mobile.

#### Scenario: Desktop hover
- **WHEN** hovering the trigger at ≥768px
- **THEN** tooltip becomes visible via opacity/visibility transition < 200ms

### Requirement: Focus and Keyboard Accessibility
Interactive elements MUST support keyboard navigation and `:focus-visible` outlines.

#### Scenario: Focus outline
- **WHEN** a component receives keyboard focus
- **THEN** outline is `2px` in `--border-color` with offset per `style.md`

### Requirement: Responsive Grid
The system SHALL use `grid-tiles` pattern with 2 columns on mobile and 4 on desktop for tile-based summaries.

#### Scenario: Breakpoint behavior
- **WHEN** viewport width ≥ 768px
- **THEN** grid uses 4 columns; otherwise 2 columns

### Requirement: Error and Validation States
The system SHALL prevent invalid inputs and present accessible error messages.

#### Scenario: Success count exceeds total
- **WHEN** `success > total` is entered
- **THEN** show role="alert" error with clear guidance; calculations do not proceed

### Requirement: Power Analysis Display
The system SHALL display power for selected MDE and alpha, referencing current control rate.

#### Scenario: Low power warning
- **WHEN** computed power < 0.8
- **THEN** show warning style compliant with `style.md` colors (no new tokens)


