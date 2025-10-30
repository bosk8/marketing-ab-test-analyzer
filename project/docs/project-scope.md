# Marketing Campaign A/B Test Analyzer — Project Scope  
**Stack:** Python • SciPy • statsmodels • Statistics

## 0) Purpose
Decide if **Variant B** improves conversion versus **A**. Provide p-value, 95% CI for lift, power/MDE, and a clear ship/hold decision with ROI estimate.

## 1) Success Criteria
- Notebook runs start-to-finish from clean clone.
- Reports: z, p-value, **95% CI for difference in proportions**, power vs sample size.
- Decision rule documented and applied.

## 2) Scope and Non-Goals
- Scope: single A vs B fixed-horizon test on conversions.
- Non-Goals: sequential peeking, CUPED, multi-arm corrections.

## 3) Prereqs
- Python 3.10+, Git.

## 4) Repository Layout
````

ab-test-analyzer/
├─ data/sample_ab.csv
├─ src/abtest.py
├─ notebooks/01_ab_test.ipynb
├─ app/ab_app.py                # optional streamlit
├─ env/requirements.txt
└─ README.md

```

### env/requirements.txt
```

pandas>=2.2
numpy>=1.26
scipy>=1.12
statsmodels>=0.14
matplotlib>=3.8
streamlit>=1.39

```

## 5) Data Format
Use aggregated counts or row-level data.

**Aggregated (recommended)**
```

group,success,total
A,123,5000
B,155,5000

```

**Row-level**
```

user_id,group,converted
u1,A,0
u2,B,1

````

## 6) Build Steps

### 6.1 Create environment
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r env/requirements.txt
````

### 6.2 Core stats functions (`src/abtest.py`)

```python
import numpy as np
from statsmodels.stats.proportion import proportions_ztest, power_proportions_2indep

def ztest_two_prop(success_a, total_a, success_b, total_b, alpha=0.05):
    count = np.array([success_a, success_b]); nobs = np.array([total_a, total_b])
    z, p = proportions_ztest(count, nobs, alternative="two-sided")
    pa, pb = count / nobs
    se = np.sqrt(pa*(1-pa)/total_a + pb*(1-pb)/total_b)
    diff = pb - pa
    zcrit = 1.96 if alpha == 0.05 else 1.96
    ci = (float(diff - zcrit*se), float(diff + zcrit*se))
    return {"z": float(z), "p": float(p), "lift": float(diff), "ci": ci}

def power(n_a, n_b, p_control, min_detectable_diff=0.02, alpha=0.05):
    ratio = n_b / n_a
    res = power_proportions_2indep(diff=min_detectable_diff, prop2=p_control, nobs1=n_a, ratio=ratio, alpha=alpha)
    return float(res.power)
```

### 6.3 Notebook outline (`notebooks/01_ab_test.ipynb`)

1. Load `data/sample_ab.csv` or compute counts from row-level.
2. Run `ztest_two_prop`. Report z, p, lift, and 95% CI.
3. Power analysis: vary MDE from 0.2pp to 5pp at observed control rate; plot power curve.
4. Decision rule:

   * If `p < 0.05` **and** CI lower bound > 0 → B wins; estimate ROI = `lift × monthly_visits × value_per_visit`.
   * Else → inconclusive; extend sample or redesign test.

### 6.4 Optional Streamlit (`app/ab_app.py`)

* Inputs: `success_a`, `total_a`, `success_b`, `total_b`, `alpha`.
* Outputs: p-value, CI, lift (pp), and power at current sample.

## 7) Assumptions and Risks

* Independent Bernoulli trials; equal eligibility for A and B.
* Fixed horizon (no repeated peeks). If peeking is needed, adopt sequential methods (out of scope here).
* If multiple variants exist, adjust for multiplicity (out of scope here).

## 8) QA

* Recompute counts from raw logs to confirm CSV.
* Sanity checks: if lifts are large, p should be very small.
* Ensure sample sizes not too small for normal approx; else use exact tests.

## 9) Deliverables

* Notebook with conclusions, plots, and ROI calc.
* `src/abtest.py` functions.
* README explaining assumptions and decision.

## 10) Troubleshooting

* Mismatched totals: recompute from raw event logs.
* Very wide CI: increase sample or reduce variance with stratification (future work).

````
