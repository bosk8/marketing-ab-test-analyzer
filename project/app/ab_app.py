"""
Interactive A/B Test Analyzer - Streamlit App

This Streamlit application provides an interactive interface for analyzing A/B test results.
Users can input test data and get real-time statistical analysis.
Fully implements the UI/UX system specification from specs/ui-system/
"""

import sys
import os
# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

import streamlit as st
from abtest import ztest_two_prop, power, load_aggregated_data, load_row_level_data
import pandas as pd

st.set_page_config(
    page_title="A/B Test Analyzer",
    page_icon="📊",
    layout="wide"
)

# Inject complete Bosk8 design system from style.md and specifications
st.markdown(
    """
    <style>
    /* CSS Variables - Complete Token Map from style.md */
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
      --container-max: min(1100px, 90vw);
    }
    
    @media (min-width: 1024px) {
      :root {
        --border-w: 1.5px;
        --border-outer-w: 2px;
      }
    }
    
    /* Global Resets & Base */
    * { box-sizing: border-box; margin: 0; padding: 0; }
    html { font-size: var(--fs-base); }
    html, body {
      margin: 0;
      width: 100%;
      height: 100%;
      background-color: var(--bg-elev1);
      font-family: var(--font-ui);
      color: var(--text-primary);
    }
    
    /* Container */
    .bosk8-container {
      width: 100%;
      max-width: var(--container-max);
      margin: 0 auto;
      padding: var(--space-4) var(--space-1) var(--space-1);
      padding-top: 10rem; /* hero spacing */
      background-color: var(--bg-elev1);
    }
    
    /* Cards */
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
    
    /* Typography */
    .tagline, .meta, .label, .nav {
      font-family: var(--font-ui);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
    }
    
    .tagline {
      font-size: 1rem;
      text-align: center;
      margin-bottom: var(--space-1);
    }
    
    .meta-sm {
      font-size: 0.75rem;
      margin-bottom: var(--space-0_75);
    }
    
    .meta-md {
      font-size: 0.875rem;
      margin-bottom: var(--space-1);
    }
    
    /* Links */
    .link {
      color: var(--text-muted);
      text-decoration: none;
      transition: all 0.15s;
    }
    
    .link:hover {
      color: var(--text-primary);
      text-decoration: underline;
      text-underline-offset: 4px;
    }
    
    /* Focus Visible - Accessibility Override */
    :focus-visible {
      outline: 2px solid var(--text-muted); /* Changed from --border-color for contrast */
      outline-offset: 2px;
    }
    
    /* Status Success */
    .status-success {
      color: var(--accent-success);
    }
    
    /* Alert Component */
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
      border-left: 4px solid var(--accent-success); /* Derived - see Style Decisions Log */
    }
    
    /* Decision Banner */
    .decision-banner {
      background-color: var(--surface-card);
      border: var(--border-outer-w) solid var(--border-color);
      border-radius: var(--r-md);
      padding: var(--space-2);
      margin-bottom: var(--space-1_5);
      font-family: var(--font-ui);
      font-size: 1rem;
    }
    
    .decision-b-wins {
      color: var(--accent-success);
      border-left: 4px solid var(--accent-success);
    }
    
    .decision-inconclusive {
      color: var(--text-subtle);
    }
    
    .decision-a-better {
      color: var(--text-subtle);
    }
    
    /* Metric Display */
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
      color: var(--text-subtle);
    }
    
    /* Streamlit Component Overrides */
    /* Hide default Streamlit styling where needed */
    .stNumberInput input, .stSlider div {
      font-family: var(--font-ui);
      font-size: var(--fs-base);
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
      background-color: var(--bg-elev1);
    }
    
    [data-testid="stSidebar"] .stNumberInput {
      margin-bottom: var(--space-1);
    }
    
    [data-testid="stSidebar"] .stSlider {
      margin-bottom: var(--space-1_5);
    }
    
    /* Override Streamlit metric styling */
    [data-testid="stMetricValue"] {
      font-family: var(--font-ui);
      color: var(--text-primary);
    }
    
    [data-testid="stMetricLabel"] {
      font-family: var(--font-ui);
      color: var(--text-subtle);
      font-size: 0.875rem;
    }
    
    /* Override Streamlit info/warning/success boxes */
    .stAlert {
      border: var(--border-w) solid var(--border-color);
      border-radius: var(--r-sm);
      background-color: var(--surface-card);
      color: var(--text-subtle);
    }
    
    /* Accordion/Expander Styling */
    .stExpander {
      border: var(--border-w) solid var(--border-color);
      border-radius: var(--r-sm);
      background-color: var(--surface-card);
    }
    
    .stExpander label {
      font-family: var(--font-ui);
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Start container
st.markdown("<div class=\"bosk8-container\">", unsafe_allow_html=True)

# Hero/Title Card
st.markdown(
    "<section class=\"card\"><h1 class=\"tagline\">A/B TEST ANALYZER</h1></section>",
    unsafe_allow_html=True,
)

# Overview Card
st.markdown(
    """<section class="card">
    <div class="meta-sm">OVERVIEW</div>
    <p style="color: var(--text-subtle); font-family: var(--font-ui); font-size: var(--fs-base); line-height: 1.5;">
    Interactive tool for analyzing A/B test results. Enter your test data below to get statistical analysis including p-values, confidence intervals, and power analysis.
    </p>
    </section>""",
    unsafe_allow_html=True,
)

# Sidebar for inputs
with st.sidebar:
    st.markdown("<div class=\"meta-sm\">VARIANT A (CONTROL)</div>", unsafe_allow_html=True)
    success_a = st.number_input(
        "Successes (conversions)",
        min_value=0,
        value=st.session_state.get('success_a', 123),
        step=1,
        key="success_a",
        help="Number of successful conversions in variant A"
    )
    total_a = st.number_input(
        "Total observations",
        min_value=1,
        value=st.session_state.get('total_a', 5000),
        step=1,
        key="total_a",
        help="Total number of observations in variant A"
    )
    
    st.markdown("<div class=\"meta-sm\" style=\"margin-top: var(--space-1_5);\">VARIANT B (TREATMENT)</div>", unsafe_allow_html=True)
    success_b = st.number_input(
        "Successes (conversions)",
        min_value=0,
        value=st.session_state.get('success_b', 155),
        step=1,
        key="success_b",
        help="Number of successful conversions in variant B"
    )
    total_b = st.number_input(
        "Total observations",
        min_value=1,
        value=st.session_state.get('total_b', 5000),
        step=1,
        key="total_b",
        help="Total number of observations in variant B"
    )
    
    st.markdown("<div class=\"meta-sm\" style=\"margin-top: var(--space-1_5);\">STATISTICAL PARAMETERS</div>", unsafe_allow_html=True)
    alpha = st.slider(
        "Significance level (α)",
        min_value=0.01,
        max_value=0.10,
        value=0.05,
        step=0.01,
        help="Significance level for statistical test"
    )
    st.markdown(f"<div style=\"color: var(--text-subtle); font-size: 0.875rem; margin-bottom: var(--space-1);\">α = {alpha:.2f}</div>", unsafe_allow_html=True)
    
    mde_for_power = st.slider(
        "MDE for power calculation (pp)",
        min_value=0.1,
        max_value=10.0,
        value=2.0,
        step=0.1,
        help="Minimum detectable effect for power analysis in percentage points"
    ) / 100
    st.markdown(f"<div style=\"color: var(--text-subtle); font-size: 0.875rem; margin-bottom: var(--space-1_5);\">MDE = {mde_for_power*100:.1f} pp</div>", unsafe_allow_html=True)
    
    # CSV Upload
    st.markdown("<div class=\"meta-sm\" style=\"margin-top: var(--space-1_5);\">DATA UPLOAD</div>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Choose CSV file",
        type=['csv'],
        help="Upload aggregated (group,success,total) or row-level (user_id,group,converted) CSV"
    )
    
    if uploaded_file is not None:
        try:
            # Save uploaded file temporarily and read it
            import tempfile
            
            with tempfile.NamedTemporaryFile(delete=False, suffix='.csv', mode='wb') as tmp_file:
                # Write uploaded file content to temp file (binary mode)
                tmp_file.write(uploaded_file.getvalue())
                tmp_path = tmp_file.name
            
            # Read CSV to detect format
            df = pd.read_csv(tmp_path)
            
            # Detect format and load accordingly
            if 'group' in df.columns and 'success' in df.columns and 'total' in df.columns:
                # Aggregated format
                sa, ta, sb, tb = load_aggregated_data(tmp_path)
                # Update session state to reflect loaded values
                if 'success_a' not in st.session_state or st.session_state.get('file_loaded') != uploaded_file.name:
                    st.session_state.success_a = sa
                    st.session_state.success_b = sb
                    st.session_state.total_a = ta
                    st.session_state.total_b = tb
                    st.session_state.file_loaded = uploaded_file.name
                    st.markdown(f"<div style=\"color: var(--text-subtle); font-size: 0.875rem;\">✅ Loaded: {uploaded_file.name}</div>", unsafe_allow_html=True)
                    st.rerun()
            elif 'user_id' in df.columns and 'group' in df.columns and 'converted' in df.columns:
                # Row-level format
                sa, ta, sb, tb = load_row_level_data(tmp_path)
                # Update session state to reflect loaded values
                if 'success_a' not in st.session_state or st.session_state.get('file_loaded') != uploaded_file.name:
                    st.session_state.success_a = sa
                    st.session_state.success_b = sb
                    st.session_state.total_a = ta
                    st.session_state.total_b = tb
                    st.session_state.file_loaded = uploaded_file.name
                    st.markdown(f"<div style=\"color: var(--text-subtle); font-size: 0.875rem;\">✅ Loaded: {uploaded_file.name}</div>", unsafe_allow_html=True)
                    st.rerun()
            else:
                st.markdown(
                    "<div class=\"alert alert-error\" role=\"alert\">❌ Error: Invalid CSV format. Expected columns: group, success, total (aggregated) or user_id, group, converted (row-level)</div>",
                    unsafe_allow_html=True,
                )
            
            # Clean up temp file
            import os
            try:
                os.unlink(tmp_path)
            except:
                pass
                
        except Exception as e:
            st.markdown(
                f"<div class=\"alert alert-error\" role=\"alert\">❌ Error loading file: {str(e)}</div>",
                unsafe_allow_html=True,
            )

# Main content area
# Validation (accessible alert)
if success_a > total_a or success_b > total_b:
    st.markdown(
        "<div class=\"alert alert-error\" role=\"alert\">❌ Error: Success count cannot exceed total count for any variant.</div>",
        unsafe_allow_html=True,
    )
    st.stop()

# Calculate conversion rates
pa = success_a / total_a if total_a > 0 else 0
pb = success_b / total_b if total_b > 0 else 0
lift = pb - pa

# Main content in two columns (desktop)
col1, col2 = st.columns(2)

# Conversion Rates Card
with col1:
    st.markdown("<div class=\"card\">", unsafe_allow_html=True)
    st.markdown("<div class=\"meta-sm\">CONVERSION RATES</div>", unsafe_allow_html=True)
    st.metric("Variant A", f"{pa:.4f} ({pa*100:.2f}%)", delta=None)
    st.metric("Variant B", f"{pb:.4f} ({pb*100:.2f}%)", delta=f"{lift*100:+.3f} pp")
    st.metric("Lift", f"{lift*100:+.3f} percentage points")
    st.markdown("</div>", unsafe_allow_html=True)

# Perform statistical test
try:
    results = ztest_two_prop(success_a, total_a, success_b, total_b, alpha=alpha)
    
    # Statistical Results Card
    with col2:
        st.markdown("<div class=\"card\">", unsafe_allow_html=True)
        st.markdown("<div class=\"meta-sm\">STATISTICAL TEST RESULTS</div>", unsafe_allow_html=True)
        st.metric("Z-statistic", f"{results['z']:.4f}")
        st.metric(
            "P-value",
            f"{results['p']:.6f}",
                 delta="Significant" if results['p'] < alpha else "Not significant",
            delta_color="normal" if results['p'] < alpha else "off"
        )
        st.metric("Lift", f"{results['lift']*100:+.3f} pp")
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Confidence Interval Card
    st.markdown("<div class=\"card\">", unsafe_allow_html=True)
    st.markdown("<div class=\"meta-sm\">95% CONFIDENCE INTERVAL</div>", unsafe_allow_html=True)
    ci_lower_pct = results['ci'][0] * 100
    ci_upper_pct = results['ci'][1] * 100
    st.markdown(
        f"""
        <div style="
            font-family: var(--font-ui);
            font-size: var(--fs-base);
            color: var(--text-primary);
            background-color: var(--surface-card);
            padding: var(--space-1);
            border: var(--border-w) solid var(--border-color);
            border-radius: var(--r-sm);
        ">
        <strong>{results['ci'][0]:.6f}</strong> to <strong>{results['ci'][1]:.6f}</strong><br>
        ({ci_lower_pct:+.3f} pp to {ci_upper_pct:+.3f} pp)
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Decision Banner Card
    st.markdown("<div class=\"card\">", unsafe_allow_html=True)
    st.markdown("<div class=\"meta-sm\">DECISION</div>", unsafe_allow_html=True)
    
    if results['p'] < alpha and results['ci'][0] > 0:
        decision_class = "decision-banner decision-b-wins"
        decision_text = "✅ <strong>VARIANT B WINS</strong> — Statistically significant improvement detected."
    elif results['ci'][0] > 0 and results['p'] >= alpha:
        decision_class = "decision-banner decision-inconclusive"
        decision_text = "⚠️ <strong>INCONCLUSIVE</strong> — Positive lift but not statistically significant. Consider extending sample size."
    elif results['ci'][1] < 0:
        decision_class = "decision-banner decision-a-better"
        decision_text = "ℹ️ <strong>VARIANT A BETTER OR EQUIVALENT</strong> — Confidence interval suggests no improvement or decrease."
    else:
        decision_class = "decision-banner decision-inconclusive"
        decision_text = "⚠️ <strong>INCONCLUSIVE</strong> — Confidence interval includes zero. Consider extending sample size."
    
    st.markdown(
        f'<div class="{decision_class}" role="status">{decision_text}</div>',
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Power Analysis Card
    st.markdown("<div class=\"card\">", unsafe_allow_html=True)
    st.markdown("<div class=\"meta-sm\">POWER ANALYSIS</div>", unsafe_allow_html=True)
    p_control = pa
    current_power = power(total_a, total_b, p_control, min_detectable_diff=mde_for_power, alpha=alpha)
    st.metric(
        f"Power to detect {mde_for_power*100:.1f}pp difference",
        f"{current_power:.1%}",
        delta=None
    )
    
    if current_power < 0.8:
        st.markdown(
            f'<div class="alert" role="status">⚠️ Power is below the recommended 80% threshold. Consider increasing sample sizes.</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f'<div class="alert" style="color: var(--accent-success);" role="status">✅ Power is sufficient (≥80%) for detecting a {mde_for_power*100:.1f}pp difference.</div>',
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Additional info - Accordion/Expander
    with st.expander("📖 UNDERSTANDING THE RESULTS"):
        st.markdown(
            """
        **Z-statistic**: Measures how many standard errors the observed difference is from zero.
        
        **P-value**: Probability of observing this result (or more extreme) if there's no real difference.
        - p < α: Reject null hypothesis (significant difference)
        - p ≥ α: Fail to reject null hypothesis (no significant difference)
        
        **Lift**: The difference in conversion rates (B - A).
        
        **Confidence Interval**: Range of plausible values for the true lift.
        - If CI excludes 0: Likely a real difference
        - If CI includes 0: Cannot rule out no difference
        
        **Power**: Probability of detecting an effect if it exists. Recommended: ≥80%.
            """,
            unsafe_allow_html=False,
        )
    
except ValueError as e:
    st.markdown(
        f"<div class=\"alert alert-error\" role=\"alert\">❌ Error in calculation: {str(e)}</div>",
        unsafe_allow_html=True,
    )
except Exception as e:
    st.markdown(
        f"<div class=\"alert alert-error\" role=\"alert\">❌ Unexpected error: {str(e)}</div>",
        unsafe_allow_html=True,
    )

# Footer/Assumptions Card
st.markdown("<div class=\"card\">", unsafe_allow_html=True)
st.markdown("<div class=\"meta-sm\">NOTE</div>", unsafe_allow_html=True)
st.markdown(
    """
This analysis assumes:
- Independent observations
- Large sample sizes (normal approximation valid)
- Fixed-horizon testing (no sequential peeking)
- Equal allocation between variants

For small samples or sequential testing, consider alternative methods.
""",
    unsafe_allow_html=False,
)
st.markdown("</div>", unsafe_allow_html=True)

# Close container
st.markdown("</div>", unsafe_allow_html=True)
