# Project Setup Guide

This document provides instructions for setting up and running the A/B Test Analyzer project.

## Quick Start

### 1. Install Dependencies

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r config/requirements.txt
```

### 2. Run the Streamlit App

```bash
# From project root directory
streamlit run app/ab_app.py
```

The app will be available at `http://localhost:8501`

### 3. Run Tests

```bash
# From project root directory
python -m pytest src/test_abtest.py
# or
python src/test_abtest.py
```

### 4. Run Jupyter Notebook

```bash
# From project root directory
jupyter notebook notebooks/01_ab_test.ipynb
```

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
├── data/                   # Sample data files
│   └── sample_ab.csv      # Example A/B test data
├── notebooks/              # Jupyter notebooks
│   └── 01_ab_test.ipynb   # Complete analysis workflow
├── docs/                   # Documentation
│   ├── README.md          # Main documentation
│   ├── project-scope.md   # Project scope
│   ├── DEPLOYMENT.md      # Deployment instructions
│   └── SANITY_CHECK.md    # Verification summary
├── config/                 # Configuration files
│   └── requirements.txt    # Python dependencies
├── README.md               # Project overview
├── SETUP.md                # This file
└── .gitignore              # Git ignore rules
```

## Troubleshooting

### Import Errors

If you get import errors, ensure you're running from the project root directory:

```bash
# From project root
streamlit run app/ab_app.py
```

### Path Issues

The app automatically adds `src/` to the Python path. If you encounter path issues, check that the directory structure matches the structure above.

## Next Steps

- Review `docs/README.md` for detailed documentation
- Check `specs/ui-system/README.md` for UI/UX specifications
- See `docs/DEPLOYMENT.md` for deployment instructions

