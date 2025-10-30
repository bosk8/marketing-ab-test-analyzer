## Style Decisions Log

Timestamp: 2025-10-30

1) Tokens Source of Truth
- Decision: Only use tokens and patterns from `style.md`.
- Rationale: Absolute rule (1) prohibits inventing tokens.

2) Derived Spacing Scale Usage
- Need: Component spacing beyond examples (forms and cards).
- Derivation: Use existing `--space-0_5`, `--space-0_75`, `--space-1`, `--space-1_5`, `--space-2`, `--space-4` to compose vertical rhythm (e.g., labels `--space-0_5`, groups `--space-1`).
- Justification: Rule (2) — derived from existing spacing tokens without introducing new names.

3) Status Styles (Warning/Info)
- Need: Warning/info without new colors.
- Decision: Use text colors (`--text-muted`, `--text-subtle`, `--text-dim`) and `--border-color` with `.card` surfaces, reserving `--accent-success` for success only.
- Rationale: Rule (1) — no new tokens; align with `style.md` tone.

4) Focus Outline
- Decision: Use `:focus-visible { outline: 2px solid var(--border-color); outline-offset: 2px; }` exactly as in `style.md`.
- Rationale: Accessibility guidance in `style.md`.

5) Motion Constraints
- Decision: Limit transitions to ≤200ms for hover/tooltip per `style.md` patterns.
- Rationale: Motion guidance in `style.md`.

6) Conflict: Streamlit Native Widgets vs Custom CSS
- Issue: Streamlit styles may differ from `style.md`.
- Resolution: Prefer `style.md` rules; where Streamlit limits styling, wrap content in HTML blocks or minimal custom CSS that maps exactly to provided tokens; record any unavoidable deviations.
- Rule: (3) Resolve in favor of `style.md`.

Open Questions
- None currently.


