"""
Interactive A/B Test Analyzer - Streamlit App

This Streamlit application provides an interactive interface for analyzing A/B test results.
Users can input test data and get real-time statistical analysis.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

import streamlit as st
from abtest import ztest_two_prop, power

st.set_page_config(
    page_title="A/B Test Analyzer",
    page_icon="📊",
    layout="wide"
)

# Inject Bosk8 tokens and styles from style.md (CSS-only, no new tokens)
st.markdown(
    """
    <style>
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
    html, body { background-color: var(--bg-elev1); color: var(--text-primary); font-family: var(--font-ui); font-size: var(--fs-base); }
    .bosk8-container { max-width: min(1100px, 90vw); margin: 0 auto; }
    .card { background-color: var(--surface-card); box-shadow: 0 0 0 var(--border-outer-w) var(--border-color), 0 1px 2px var(--shadow-tint); border-radius: var(--r-md); padding: var(--space-2); margin-bottom: var(--space-1_5); }
    .tagline, .meta, .label, .nav { font-family: var(--font-ui); text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted); }
    .meta-sm { font-size: 0.75rem; }
    .link { color: var(--text-muted); text-decoration: none; transition: all .15s; }
    .link:hover { color: var(--text-primary); text-decoration: underline; text-underline-offset: 4px; }
    .tooltip-trigger { position: relative; background: transparent; border: none; padding: 0; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; color: var(--text-dim); }
    .tooltip { position: absolute; left: 50%; bottom: calc(100% + .5rem); transform: translate(-50%); background-color: var(--surface-card); border: var(--border-w) solid var(--border-color); padding: .5rem; font-size: .625rem; font-family: var(--font-ui); color: var(--text-subtle); max-width: 280px; width: max-content; line-height: 1.5; opacity: 0; visibility: hidden; transition: opacity .15s, visibility .15s; pointer-events: none; z-index: 10; }
    .tooltip:before { content: ""; position: absolute; top: 100%; left: 50%; transform: translate(-50%); border-left: 4px solid transparent; border-right: 4px solid transparent; border-top: 4px solid var(--border-color); }
    .tooltip:after  { content: ""; position: absolute; top: calc(100% - 1px); left: 50%; transform: translate(-50%); border-left: 3px solid transparent; border-right: 3px solid transparent; border-top: 3px solid rgb(9 9 11); }
    @media (min-width: 768px) { .tooltip-trigger:hover .tooltip { opacity: 1; visibility: visible; } }
    @media (max-width: 767px) { .tooltip-trigger.active .tooltip { opacity: 1; visibility: visible; } }
    :focus-visible { outline: 2px solid var(--border-color); outline-offset: 2px; }
    .status-success { color: var(--accent-success); }
    .alert { border: var(--border-w) solid var(--border-color); border-radius: var(--r-sm); padding: var(--space-1); color: var(--text-subtle); background-color: var(--surface-card); }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class=\"bosk8-container\">", unsafe_allow_html=True)

st.markdown("<section class=\"card\"><h1 class=\"tagline\">A/B TEST ANALYZER</h1></section>", unsafe_allow_html=True)

st.markdown(
    "<section class=\"card\"><div class=\"meta-sm\">Overview</div><p class=\"\">Interactive tool for analyzing A/B test results. Enter your test data below to get statistical analysis including p-values, confidence intervals, and power analysis.</p></section>",
    unsafe_allow_html=True,
)

# Sidebar for inputs
st.sidebar.header("Test Parameters")

with st.sidebar:
    st.markdown("<div class=\"meta-sm\">Variant A (Control)</div>", unsafe_allow_html=True)
    success_a = st.number_input("Successes (conversions)", min_value=0, value=123, step=1, key="success_a")
    total_a = st.number_input("Total observations", min_value=1, value=5000, step=1, key="total_a")
    
    st.markdown("<div class=\"meta-sm\">Variant B (Treatment)</div>", unsafe_allow_html=True)
    success_b = st.number_input("Successes (conversions)", min_value=0, value=155, step=1, key="success_b")
    total_b = st.number_input("Total observations", min_value=1, value=5000, step=1, key="total_b")
    
    st.markdown("<div class=\"meta-sm\">Statistical Parameters</div>", unsafe_allow_html=True)
    alpha = st.slider("Significance level (α)", min_value=0.01, max_value=0.10, value=0.05, step=0.01)
    mde_for_power = st.slider("MDE for power calculation (pp)", min_value=0.1, max_value=10.0, value=2.0, step=0.1) / 100

# Main content area
col1, col2 = st.columns(2)

# Validation (accessible alert)
if success_a > total_a or success_b > total_b:
    st.markdown("<div class=\"alert\" role=\"alert\">❌ Error: Success count cannot exceed total count for any variant.</div>", unsafe_allow_html=True)
    st.stop()

# Calculate conversion rates
pa = success_a / total_a if total_a > 0 else 0
pb = success_b / total_b if total_b > 0 else 0
lift = pb - pa

# Display conversion rates
with col1:
    st.markdown("<div class=\"meta-sm\">Conversion Rates</div>", unsafe_allow_html=True)
    st.metric("Variant A", f"{pa:.4f} ({pa*100:.2f}%)", delta=None)
    st.metric("Variant B", f"{pb:.4f} ({pb*100:.2f}%)", delta=f"{lift*100:+.3f} pp")
    st.metric("Lift", f"{lift*100:+.3f} percentage points")

# Perform statistical test
try:
    results = ztest_two_prop(success_a, total_a, success_b, total_b, alpha=alpha)
    
    with col2:
        st.markdown("<div class=\"meta-sm\">Statistical Test Results</div>", unsafe_allow_html=True)
        st.metric("Z-statistic", f"{results['z']:.4f}")
        st.metric("P-value", f"{results['p']:.6f}", 
                 delta="Significant" if results['p'] < alpha else "Not significant",
                 delta_color="normal" if results['p'] < alpha else "off")
        st.metric("Lift", f"{results['lift']*100:+.3f} pp")
    
    # Confidence interval
    st.markdown("<div class=\"meta-sm\">95% Confidence Interval</div>", unsafe_allow_html=True)
    ci_lower_pct = results['ci'][0] * 100
    ci_upper_pct = results['ci'][1] * 100
    st.info(f"**{results['ci'][0]:.6f} to {results['ci'][1]:.6f}** ({ci_lower_pct:+.3f} pp to {ci_upper_pct:+.3f} pp)")
    
    # Decision
    st.markdown("<div class=\"meta-sm\">Decision</div>", unsafe_allow_html=True)
    if results['p'] < alpha and results['ci'][0] > 0:
        st.markdown("<div class=\"status-success\">✅ <strong>Variant B Wins</strong> - Statistically significant improvement detected.</div>", unsafe_allow_html=True)
    elif results['ci'][0] > 0 and results['p'] >= alpha:
        st.warning("⚠️ **Inconclusive** - Positive lift but not statistically significant. Consider extending sample size.")
    elif results['ci'][1] < 0:
        st.info("ℹ️ **Variant A Better or Equivalent** - Confidence interval suggests no improvement or decrease.")
    else:
        st.warning("⚠️ **Inconclusive** - Confidence interval includes zero. Consider extending sample size.")
    
    # Power analysis
    st.markdown("<div class=\"meta-sm\">Power Analysis</div>", unsafe_allow_html=True)
    p_control = pa
    current_power = power(total_a, total_b, p_control, min_detectable_diff=mde_for_power, alpha=alpha)
    st.metric(
        f"Power to detect {mde_for_power*100:.1f}pp difference",
        f"{current_power:.1%}",
        delta=None
    )
    
    if current_power < 0.8:
        st.warning(f"⚠️ Power is below the recommended 80% threshold. Consider increasing sample sizes.")
    else:
        st.success(f"✅ Power is sufficient (≥80%) for detecting a {mde_for_power*100:.1f}pp difference.")
    
    # Additional info
    with st.expander("📖 Understanding the Results"):
        st.markdown("""
        **Z-statistic**: Measures how many standard errors the observed difference is from zero.
        
        **P-value**: Probability of observing this result (or more extreme) if there's no real difference.
        - p < α: Reject null hypothesis (significant difference)
        - p ≥ α: Fail to reject null hypothesis (no significant difference)
        
        **Lift**: The difference in conversion rates (B - A).
        
        **Confidence Interval**: Range of plausible values for the true lift.
        - If CI excludes 0: Likely a real difference
        - If CI includes 0: Cannot rule out no difference
        
        **Power**: Probability of detecting an effect if it exists. Recommended: ≥80%.
        """)
        st.markdown(
            "<button class=\"tooltip-trigger\" aria-describedby=\"tip-alpha\">α<span class=\"tooltip\" id=\"tip-alpha\">Two-sided z-test critical value computed via normal quantile.</span></button>",
            unsafe_allow_html=True,
        )
    
except ValueError as e:
    st.markdown(f"<div class=\"alert\" role=\"alert\">❌ Error in calculation: {str(e)}</div>", unsafe_allow_html=True)
except Exception as e:
    st.markdown(f"<div class=\"alert\" role=\"alert\">❌ Unexpected error: {str(e)}</div>", unsafe_allow_html=True)

# Footer
st.markdown("<section class=\"card\">", unsafe_allow_html=True)
st.markdown("<div class=\"meta-sm\">Note</div>", unsafe_allow_html=True)
st.markdown("""
This analysis assumes:
- Independent observations
- Large sample sizes (normal approximation valid)
- Fixed-horizon testing (no sequential peeking)
- Equal allocation between variants

For small samples or sequential testing, consider alternative methods.
""")
st.markdown("</section>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

