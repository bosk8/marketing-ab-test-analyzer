# Marketing Campaign A/B Test Analyzer

A Python tool for statistically rigorous analysis of A/B test results. This analyzer helps determine if Variant B improves conversion rates versus Variant A by providing p-values, confidence intervals, power analysis, and clear decision-making guidance with ROI estimates.

## Project Structure

```
project/
├── app/                    # Streamlit web application
│   └── ab_app.py          # Main application file
├── src/                    # Core statistical functions
│   ├── abtest.py          # Statistical analysis functions
│   └── test_abtest.py     # Unit tests
├── specs/                  # UI/UX system specifications
│   └── ui-system/         # Complete design system specs
│       ├── 01-executive-summary.md
│       ├── 02-information-architecture.md
│       ├── 03-screen-specs.md
│       ├── 04-component-library.md
│       ├── 05-function-to-ui-mapping.md
│       ├── 06-navigation-routing.md
│       ├── 07-accessibility-checklist.md
│       ├── 08-style-compliance-matrix.md
│       ├── 09-style-decisions-log.md
│       ├── 10-dev-handoff.md
│       └── README.md
├── data/                   # Sample data files
│   └── sample_ab.csv      # Example A/B test data
├── notebooks/              # Jupyter notebooks
│   └── 01_ab_test.ipynb   # Complete analysis workflow
├── docs/                   # Documentation
│   ├── README.md          # This file (original)
│   ├── project-scope.md   # Project scope document
│   ├── DEPLOYMENT.md      # Deployment instructions
│   └── SANITY_CHECK.md    # Final verification summary
└── config/                 # Configuration files
    └── requirements.txt    # Python dependencies
```

## Features

- **Two-Proportion Z-Test**: Statistical comparison of conversion rates between two variants
- **Confidence Intervals**: 95% confidence intervals for lift estimates
- **Power Analysis**: Assess test sensitivity across different minimum detectable effects (MDE)
- **Data Flexibility**: Support for both aggregated and row-level data formats
- **Reproducible Analysis**: Jupyter notebook for complete end-to-end workflow
- **Interactive Interface**: Streamlit web app for real-time analysis
- **Full UI/UX Specification**: Complete design system documentation

## Requirements

- Python 3.10+
- See `config/requirements.txt` for dependencies

## Installation

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r config/requirements.txt
```

## Quick Start

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

## Decision Rule

The analyzer applies the following decision rule:

- **Variant B Wins**: If p < 0.05 **AND** 95% CI lower bound > 0
  - Provides ROI estimate based on lift × monthly visits × value per visit
  
- **Inconclusive**: Otherwise
  - Recommends extending sample size or redesigning the test

## UI/UX System Specifications

Complete design system documentation is available in `specs/ui-system/`:

- Executive summary and personas
- Information architecture and user flows
- Screen-by-screen specifications
- Component library with exact token references
- Function-to-UI mapping
- Accessibility checklist (WCAG 2.2 AA)
- Style compliance matrix
- Developer handoff artifacts

## Running Tests

```bash
python -m pytest src/test_abtest.py
# or
python src/test_abtest.py
```

## License

[Specify your license here]

## Contributing

[Specify contribution guidelines here]

