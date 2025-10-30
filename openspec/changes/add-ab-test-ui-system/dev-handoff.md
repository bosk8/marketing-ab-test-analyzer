## Dev Handoff Artifacts

### CSS Token Map (from `style.md`)
Use variables as provided in `style.md` under `:root`.

```css
:root {
  --font-ui: JetBrains Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, DejaVu Sans Mono, Courier New, monospace;
  --fs-base: clamp(16px, calc(15.2px + 0.25vw), 20px);
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
  --border-w: 1px;
  --border-outer-w: 1px;
  --shadow-tint: #0000000d;
  --r-sm: 4px;
  --r-md: 6px;
  --space-0_5: 0.5rem;
  --space-0_75: 0.75rem;
  --space-1: 1rem;
  --space-1_5: 1.5rem;
  --space-2: 2rem;
  --space-4: 4rem;
}
@media (min-width: 1024px) {
  :root { --border-w: 1.5px; --border-outer-w: 2px; }
}
```

### Sample Layout Snippet

```html
<main class="bosk8">
  <div class="container">
    <section class="card" style="padding: var(--space-2)">
      <h2 class="tagline">A/B TEST ANALYZER</h2>
    </section>
    <section class="card" style="margin-top: var(--space-1_5); padding: var(--space-2)">
      <div class="meta-sm" style="text-transform: uppercase; letter-spacing: .05em; color: var(--text-muted)">Inputs</div>
      <!-- inputs here -->
    </section>
  </div>
</main>
```

### Accessibility Snippet

```css
:focus-visible { outline: 2px solid var(--border-color); outline-offset: 2px; }
```

### Tooltip Snippet

```html
<button class="tooltip-trigger" aria-describedby="tip-1">i
  <span class="tooltip" id="tip-1">Two-sided z-test at alpha.</span>
</button>
```


