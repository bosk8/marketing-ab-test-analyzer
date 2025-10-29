# Marketing Campaign A/B Test Analyzer

A Python tool for statistically rigorous analysis of A/B test results. This analyzer helps determine if Variant B improves conversion rates versus Variant A by providing p-values, confidence intervals, power analysis, and clear decision-making guidance with ROI estimates.

## Features

- **Two-Proportion Z-Test**: Statistical comparison of conversion rates between two variants
- **Confidence Intervals**: 95% confidence intervals for lift estimates
- **Power Analysis**: Assess test sensitivity across different minimum detectable effects (MDE)
- **Data Flexibility**: Support for both aggregated and row-level data formats
- **Reproducible Analysis**: Jupyter notebook for complete end-to-end workflow
- **Interactive Interface**: Optional Streamlit web app for real-time analysis

## Requirements

- Python 3.10+
- See `env/requirements.txt` for dependencies

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd 03-marketing-ab-test-analyzer
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r env/requirements.txt
```

## Quick Start

### Using the Jupyter Notebook

1. Start Jupyter:
```bash
jupyter notebook notebooks/01_ab_test.ipynb
```

2. Run all cells to perform a complete analysis including:
   - Data loading
   - Statistical testing
   - Power analysis visualization
   - Decision rule application
   - ROI estimation

### Using the Streamlit App

1. Launch the Streamlit app:
```bash
streamlit run app/ab_app.py
```

2. Input your test data in the sidebar:
   - Success counts and totals for variants A and B
   - Significance level (α)
   - MDE for power calculation

3. View real-time results including p-values, confidence intervals, and power analysis.

### Using the Python Functions Directly

```python
from src.abtest import ztest_two_prop, power, load_aggregated_data

# Load data
success_a, total_a, success_b, total_b = load_aggregated_data('data/sample_ab.csv')

# Perform statistical test
results = ztest_two_prop(success_a, total_a, success_b, total_b, alpha=0.05)
print(f"Z-statistic: {results['z']:.4f}")
print(f"P-value: {results['p']:.6f}")
print(f"Lift: {results['lift']:.4f}")
print(f"95% CI: {results['ci']}")

# Calculate power
p_control = success_a / total_a
power_val = power(total_a, total_b, p_control, min_detectable_diff=0.02, alpha=0.05)
print(f"Power: {power_val:.2%}")
```

## Data Formats

### Aggregated Format (Recommended)

CSV file with columns: `group`, `success`, `total`

```csv
group,success,total
A,123,5000
B,155,5000
```

### Row-Level Format

CSV file with columns: `user_id`, `group`, `converted` (0 or 1)

```csv
user_id,group,converted
u1,A,0
u2,A,1
u3,B,1
u4,B,1
```

The row-level format is automatically aggregated to counts during loading.

## Decision Rule

The analyzer applies the following decision rule:

- **Variant B Wins**: If p < 0.05 **AND** 95% CI lower bound > 0
  - Provides ROI estimate based on lift × monthly visits × value per visit
  
- **Inconclusive**: Otherwise
  - Recommends extending sample size or redesigning the test

## Assumptions and Limitations

### Statistical Assumptions

1. **Independent Observations**: Each trial is independent (no user appears in both groups)
2. **Large Sample Sizes**: Normal approximation is appropriate (typically n > 30 per group)
3. **Fixed-Horizon Testing**: No sequential peeking; results are only evaluated once at the end
4. **Equal Eligibility**: Both variants have equal chance of assignment

### Limitations (Out of Scope)

- **Sequential Testing**: This tool is for fixed-horizon tests only. Sequential peeking invalidates results.
- **CUPED**: Covariate adjustment is not implemented
- **Multiplicity Corrections**: Multiple variant corrections are not applied
- **Exact Tests**: Uses normal approximation; exact binomial tests for small samples not included

## Project Structure

```
ab-test-analyzer/
├── data/
│   └── sample_ab.csv          # Sample aggregated data
├── src/
│   ├── abtest.py              # Core statistical functions
│   └── test_abtest.py         # Unit tests
├── notebooks/
│   └── 01_ab_test.ipynb       # Complete analysis workflow
├── app/
│   └── ab_app.py              # Streamlit web app (optional)
├── env/
│   └── requirements.txt       # Python dependencies
└── README.md                  # This file
```

## Running Tests

```bash
python -m pytest src/test_abtest.py
# or
python src/test_abtest.py
```

## Troubleshooting

### Mismatched Totals

If you suspect data issues, recompute counts from raw event logs to confirm CSV accuracy.

### Very Wide Confidence Intervals

Wide CIs indicate low precision. Solutions:
- Increase sample size
- Consider variance reduction techniques (e.g., stratification - future work)

### Small Sample Sizes

If sample sizes are very small (< 30 per group), the normal approximation may not be valid. Consider:
- Using exact tests (not implemented in this tool)
- Collecting more data before analysis

### Import Errors

Ensure you've installed all dependencies:
```bash
pip install -r env/requirements.txt
```

If using the notebook or app, ensure the `src` directory is in your Python path.

## Example Output

```
============================================================
A/B TEST RESULTS
============================================================

Z-statistic: 2.3456
P-value (two-sided): 0.019045

Lift (difference in proportions): 0.006400 (0.640 percentage points)

95% Confidence Interval for difference:
  Lower bound: 0.001234 (0.123 pp)
  Upper bound: 0.011566 (1.157 pp)
============================================================

✅ VARIANT B WINS

Statistical significance: p = 0.019045 < 0.05 (alpha)
Confidence interval lower bound: 0.001234 > 0

Variant B shows a statistically significant improvement of 0.640 percentage points.
```

## License

[Specify your license here]

## Contributing

[Specify contribution guidelines here]

## References

- Statistical methods based on standard two-proportion z-tests
- Uses `statsmodels` and `scipy` for statistical calculations
- For more information on A/B testing best practices, see [reference materials]

