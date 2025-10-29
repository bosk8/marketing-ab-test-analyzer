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

st.title("📊 A/B Test Analyzer")
st.markdown("""
Interactive tool for analyzing A/B test results. Enter your test data below to get 
statistical analysis including p-values, confidence intervals, and power analysis.
""")

# Sidebar for inputs
st.sidebar.header("Test Parameters")

with st.sidebar:
    st.subheader("Variant A (Control)")
    success_a = st.number_input("Successes (conversions)", min_value=0, value=123, step=1, key="success_a")
    total_a = st.number_input("Total observations", min_value=1, value=5000, step=1, key="total_a")
    
    st.subheader("Variant B (Treatment)")
    success_b = st.number_input("Successes (conversions)", min_value=0, value=155, step=1, key="success_b")
    total_b = st.number_input("Total observations", min_value=1, value=5000, step=1, key="total_b")
    
    st.subheader("Statistical Parameters")
    alpha = st.slider("Significance level (α)", min_value=0.01, max_value=0.10, value=0.05, step=0.01)
    mde_for_power = st.slider("MDE for power calculation (pp)", min_value=0.1, max_value=10.0, value=2.0, step=0.1) / 100

# Main content area
col1, col2 = st.columns(2)

# Validation
if success_a > total_a or success_b > total_b:
    st.error("❌ Error: Success count cannot exceed total count for any variant.")
    st.stop()

# Calculate conversion rates
pa = success_a / total_a if total_a > 0 else 0
pb = success_b / total_b if total_b > 0 else 0
lift = pb - pa

# Display conversion rates
with col1:
    st.subheader("Conversion Rates")
    st.metric("Variant A", f"{pa:.4f} ({pa*100:.2f}%)", delta=None)
    st.metric("Variant B", f"{pb:.4f} ({pb*100:.2f}%)", delta=f"{lift*100:+.3f} pp")
    st.metric("Lift", f"{lift*100:+.3f} percentage points")

# Perform statistical test
try:
    results = ztest_two_prop(success_a, total_a, success_b, total_b, alpha=alpha)
    
    with col2:
        st.subheader("Statistical Test Results")
        st.metric("Z-statistic", f"{results['z']:.4f}")
        st.metric("P-value", f"{results['p']:.6f}", 
                 delta="Significant" if results['p'] < alpha else "Not significant",
                 delta_color="normal" if results['p'] < alpha else "off")
        st.metric("Lift", f"{results['lift']*100:+.3f} pp")
    
    # Confidence interval
    st.subheader("95% Confidence Interval")
    ci_lower_pct = results['ci'][0] * 100
    ci_upper_pct = results['ci'][1] * 100
    st.info(f"**{results['ci'][0]:.6f} to {results['ci'][1]:.6f}** ({ci_lower_pct:+.3f} pp to {ci_upper_pct:+.3f} pp)")
    
    # Decision
    st.subheader("Decision")
    if results['p'] < alpha and results['ci'][0] > 0:
        st.success("✅ **Variant B Wins** - Statistically significant improvement detected.")
    elif results['ci'][0] > 0 and results['p'] >= alpha:
        st.warning("⚠️ **Inconclusive** - Positive lift but not statistically significant. Consider extending sample size.")
    elif results['ci'][1] < 0:
        st.info("ℹ️ **Variant A Better or Equivalent** - Confidence interval suggests no improvement or decrease.")
    else:
        st.warning("⚠️ **Inconclusive** - Confidence interval includes zero. Consider extending sample size.")
    
    # Power analysis
    st.subheader("Power Analysis")
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
    
except ValueError as e:
    st.error(f"❌ Error in calculation: {str(e)}")
except Exception as e:
    st.error(f"❌ Unexpected error: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
**Note**: This analysis assumes:
- Independent observations
- Large sample sizes (normal approximation valid)
- Fixed-horizon testing (no sequential peeking)
- Equal allocation between variants

For small samples or sequential testing, consider alternative methods.
""")

