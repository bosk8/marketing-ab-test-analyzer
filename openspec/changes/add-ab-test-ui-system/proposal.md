## Why
The project currently delivers solid statistical capabilities (notebook, core functions, optional Streamlit UI) but lacks a production-ready, consistent UI/UX system. We need a reusable, accessible, and token-driven interface that strictly adheres to `style.md` for dark, minimal, mono design across screens and components.

## What Changes
- Establish a token-driven UI system mapped directly to `style.md` (colors, type, spacing, radii, shadows, motion)
- Define Information Architecture, navigation, and core user flows for A/B analysis
- Specify reusable components (cards, inputs, grid tiles, tooltips, metrics, toasts/modals) with states and accessibility
- Map backend functions (`src/abtest.py`) to UI interactions and validations
- Provide Style Compliance Matrix and Style Decisions Log (assumptions/derivations only from `style.md`)
- Add acceptance checklist and dev-handoff artifacts (CSS variables, example snippets)

## Impact
- Affected specs: `ui-system`
- Affected code: `app/ab_app.py` (visual behavior and structure), future UI modules/components
- No breaking API changes to `src/abtest.py`

## Executive Summary
- Goals: Fast, clear decisioning for A/B tests; reusable UI primitives; strict brand/style compliance
- Personas: Data analysts, growth marketers, PMs
- Major flows: Data input/validation → stats calc → interpret (p, CI, lift) → decision → power guidance
- Constraints: Single source of truth is `style.md`; WCAG 2.2 AA; minimal motion; responsive


