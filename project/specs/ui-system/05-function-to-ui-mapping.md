# Function-to-UI Mapping

**Version:** 1.0  
**Date:** 2025-01-27  
**Style Reference:** `style.md`

This document maps backend functions (`src/abtest.py`) to UI triggers, data contracts (inputs/outputs), validations, error states, and feedback patterns.

---

## Backend Function: `ztest_two_prop()`

**Location:** `src/abtest.py`, lines 14-71  
**Purpose:** Perform two-proportion z-test comparing conversion rates between variants A and B

### UI Trigger
- **Primary:** Input change in Variant A or Variant B number inputs (success_a, total_a, success_b, total_b)
- **Secondary:** Alpha (α) slider change
- **Debouncing:** Recommended 100ms debounce to avoid excessive calculations on rapid input changes
- **Initial Load:** Calculate on mount if all required inputs are present

### Input Contract

**Function Signature:**
```python
ztest_two_prop(success_a: int, total_a: int, success_b: int, total_b: int, alpha: float = 0.05) -> Dict[str, float | Tuple[float, float]]
```

**UI Inputs:**
| UI Element | Parameter | Type | Source | Validation |
|------------|-----------|------|--------|------------|
| Number Input "Successes (Variant A)" | `success_a` | `int` | Sidebar input | `success_a >= 0`, `success_a <= total_a` |
| Number Input "Total (Variant A)" | `total_a` | `int` | Sidebar input | `total_a > 0` |
| Number Input "Successes (Variant B)" | `success_b` | `int` | Sidebar input | `success_b >= 0`, `success_b <= total_b` |
| Number Input "Total (Variant B)" | `total_b` | `int` | Sidebar input | `total_b > 0` |
| Slider "Significance level (α)" | `alpha` | `float` | Sidebar slider | `0.01 <= alpha <= 0.10` |

**Validation Rules (Client-Side):**
1. **Before API Call:**
   - Check: `success_a >= 0`, `success_b >= 0`
   - Check: `total_a > 0`, `total_b > 0`
   - Check: `success_a <= total_a`, `success_b <= total_b`
   - Check: `0.01 <= alpha <= 0.10`
2. **On Validation Failure:**
   - Display Alert component with error message
   - Highlight invalid input(s) with error state (red border)
   - Block calculation (do not call function)
   - Show error message: "Error: [specific validation failure]"

### Output Contract

**Function Returns:**
```python
{
    "z": float,        # z-statistic
    "p": float,        # two-sided p-value
    "lift": float,     # difference in proportions (pb - pa)
    "ci": tuple        # 95% confidence interval (lower, upper)
}
```

**UI Display Mapping:**
| Output Field | UI Element | Format | Component |
|--------------|------------|--------|-----------|
| `z` | Statistical Results Card → "Z-statistic" metric | `{z:.4f}` | Metric Display |
| `p` | Statistical Results Card → "P-value" metric | `{p:.6f}` | Metric Display |
| `p` | Statistical Results Card → "P-value" delta | "Significant" if `p < alpha`, else "Not significant" | Metric Display (delta) |
| `lift` | Conversion Rates Card → "Lift" metric | `{lift*100:+.3f} percentage points` | Metric Display |
| `lift` | Statistical Results Card → "Lift" metric | `{lift*100:+.3f} pp` | Metric Display |
| `ci[0]`, `ci[1]` | Confidence Interval Card | `{ci[0]:.6f} to {ci[1]:.6f} ({ci_lower_pct:+.3f} pp to {ci_upper_pct:+.3f} pp)` | Confidence Interval Display |
| Decision (derived) | Decision Banner Card | See Decision Logic below | Decision Banner |

**Decision Logic (Derived from Outputs):**
```javascript
if (results.p < alpha && results.ci[0] > 0) {
  decision = "b-wins";
  message = "✅ VARIANT B WINS — Statistically significant improvement detected.";
} else if (results.ci[0] > 0 && results.p >= alpha) {
  decision = "inconclusive-positive";
  message = "⚠️ INCONCLUSIVE — Positive lift but not statistically significant. Consider extending sample size.";
} else if (results.ci[1] < 0) {
  decision = "a-better";
  message = "ℹ️ VARIANT A BETTER OR EQUIVALENT — Confidence interval suggests no improvement or decrease.";
} else {
  decision = "inconclusive-zero";
  message = "⚠️ INCONCLUSIVE — Confidence interval includes zero. Consider extending sample size.";
}
```

### Error States

**Backend Exceptions:**
| Exception | Trigger | UI Feedback | Component |
|-----------|---------|-------------|-----------|
| `ValueError("Total counts must be positive")` | `total_a <= 0` or `total_b <= 0` | Alert: "Error: Total counts must be positive" | Alert (error variant) |
| `ValueError("Success counts cannot be negative")` | `success_a < 0` or `success_b < 0` | Alert: "Error: Success counts cannot be negative" | Alert (error variant) |
| `ValueError("Success counts cannot exceed total counts")` | `success_a > total_a` or `success_b > total_b` | Alert: "Error: Success count cannot exceed total count for any variant." | Alert (error variant) |
| `ValueError("Alpha must be between 0 and 1")` | `alpha <= 0` or `alpha >= 1` | Alert: "Error: Alpha must be between 0 and 1" | Alert (error variant) |

**UI Error Handling:**
- Catch exceptions in try-catch block
- Display error in Alert component in results area (main content)
- Clear/reset previous results display
- Keep inputs unchanged (user can correct)

### Loading States

**During Calculation:**
- Show loading indicator (skeleton or spinner) in results cards
- Disable inputs (optional — can allow concurrent edits)
- Calculation time: Typically < 100ms, so loading state may not be visible

---

## Backend Function: `power()`

**Location:** `src/abtest.py`, lines 74-107  
**Purpose:** Compute statistical power for detecting a minimum detectable effect (MDE)

### UI Trigger
- **Primary:** Input change in Variant A or Variant B totals (total_a, total_b)
- **Secondary:** MDE slider change
- **Tertiary:** Alpha (α) slider change
- **Calculation Dependency:** Requires control conversion rate (`p_control = success_a / total_a`)
- **Debouncing:** 100ms debounce (same as ztest)

### Input Contract

**Function Signature:**
```python
power(n_a: int, n_b: int, p_control: float, min_detectable_diff: float = 0.02, alpha: float = 0.05) -> float
```

**UI Inputs:**
| UI Element | Parameter | Type | Source | Validation |
|------------|-----------|------|--------|------------|
| Number Input "Total (Variant A)" | `n_a` | `int` | Sidebar input | `total_a > 0` |
| Number Input "Total (Variant B)" | `n_b` | `int` | Sidebar input | `total_b > 0` |
| Calculated (from success_a/total_a) | `p_control` | `float` | Derived | `0 <= p_control <= 1` |
| Slider "MDE for power calculation (pp)" | `min_detectable_diff` | `float` | Sidebar slider (converted from pp to decimal) | `0.001 <= min_detectable_diff <= 0.10` |
| Slider "Significance level (α)" | `alpha` | `float` | Sidebar slider | `0.01 <= alpha <= 0.10` |

**Validation Rules:**
1. **Before API Call:**
   - Check: `total_a > 0`, `total_b > 0`
   - Check: `success_a <= total_a` (for p_control calculation)
   - Check: `0.001 <= min_detectable_diff <= 0.10` (0.1pp to 10.0pp)
   - Check: `0.01 <= alpha <= 0.10`
2. **On Validation Failure:**
   - Display Alert in Power Analysis Card
   - Block calculation
   - Show error message

### Output Contract

**Function Returns:**
```python
float  # Statistical power (0.0 to 1.0)
```

**UI Display Mapping:**
| Output Field | UI Element | Format | Component |
|--------------|------------|--------|-----------|
| `power` | Power Analysis Card → Power metric | `{power:.1%}` | Metric Display |
| `power` (threshold) | Power Analysis Card → Threshold indicator | If `power < 0.8`: Warning text<br>If `power >= 0.8`: Success text | Alert (warning/success variant) |

**Threshold Indicator Logic:**
```javascript
if (power < 0.8) {
  showWarning("⚠️ Power is below the recommended 80% threshold. Consider increasing sample sizes.");
} else {
  showSuccess("✅ Power is sufficient (≥80%) for detecting a {mde:.1f}pp difference.");
}
```

### Error States

**Backend Exceptions:**
| Exception | Trigger | UI Feedback | Component |
|-----------|---------|-------------|-----------|
| `ValueError("Sample sizes must be positive")` | `n_a <= 0` or `n_b <= 0` | Alert: "Error: Sample sizes must be positive" | Alert (error variant) |
| `ValueError("Control proportion must be between 0 and 1")` | `p_control < 0` or `p_control > 1` | Alert: "Error: Invalid control proportion" | Alert (error variant) |
| `ValueError("Alpha must be between 0 and 1")` | `alpha <= 0` or `alpha >= 1` | Alert: "Error: Alpha must be between 0 and 1" | Alert (error variant) |

**UI Error Handling:**
- Display error in Power Analysis Card (Alert component)
- Clear power metric display
- Keep inputs unchanged

---

## Backend Function: `load_aggregated_data()`

**Location:** `src/abtest.py`, lines 110-165  
**Purpose:** Load aggregated A/B test data from CSV file

### UI Trigger
- **Primary:** CSV file upload in sidebar (file input change)
- **File Format:** CSV with columns `group`, `success`, `total`
- **Action:** On file selection, parse and populate sidebar inputs

### Input Contract

**Function Signature:**
```python
load_aggregated_data(filepath: str) -> Tuple[int, int, int, int]
```

**UI Inputs:**
| UI Element | Parameter | Type | Source | Validation |
|------------|-----------|------|--------|------------|
| File Input "Choose CSV file" | `filepath` | `string` | File upload | File exists, `.csv` extension, readable |

**File Format Validation:**
1. **Client-Side (before upload):**
   - Check file extension: `.csv`
   - Check file size: Warn if > 10MB (optional)
2. **Backend Validation:**
   - Check file exists
   - Check required columns: `group`, `success`, `total`
   - Check variant A and B present

### Output Contract

**Function Returns:**
```python
Tuple[int, int, int, int]  # (success_a, total_a, success_b, total_b)
```

**UI Display Mapping:**
| Output Field | UI Element | Action |
|--------------|------------|--------|
| `success_a` | Sidebar → "Successes (Variant A)" input | Set value |
| `total_a` | Sidebar → "Total (Variant A)" input | Set value |
| `success_b` | Sidebar → "Successes (Variant B)" input | Set value |
| `total_b` | Sidebar → "Total (Variant B)" input | Set value |
| Auto-trigger | Results calculation | Automatically trigger `ztest_two_prop()` and `power()` |

**File Info Display:**
- Show filename in file upload area: "Selected: {filename}.csv"
- Display in `var(--text-subtle)` color, `0.875rem` font size

### Error States

**Backend Exceptions:**
| Exception | Trigger | UI Feedback | Component |
|-----------|---------|-------------|-----------|
| `FileNotFoundError` | File doesn't exist | Alert: "Error: File not found: {filepath}" | Alert (error variant) |
| `ValueError("Missing required columns: [...]")` | Missing columns | Alert: "Error: Missing required columns: group, success, total" | Alert (error variant) |
| `ValueError("Variant A data not found in CSV")` | No group 'A' in CSV | Alert: "Error: Variant A data not found in CSV" | Alert (error variant) |
| `ValueError("Variant B data not found in CSV")` | No group 'B' in CSV | Alert: "Error: Variant B data not found in CSV" | Alert (error variant) |
| `ValueError("Success counts cannot be negative")` | Negative success value | Alert: "Error: Success counts cannot be negative" | Alert (error variant) |
| `ValueError("Total counts must be positive")` | Zero or negative total | Alert: "Error: Total counts must be positive" | Alert (error variant) |
| `ValueError("Success counts cannot exceed total counts")` | success > total | Alert: "Error: Success count cannot exceed total count" | Alert (error variant) |

**UI Error Handling:**
- Display error in Alert component in sidebar (near file upload)
- Clear file selection
- Do not populate inputs
- User can retry upload

### Loading States

**During File Upload/Parse:**
- Show loading spinner on file input button
- Disable file input
- Display "Uploading..." text
- Duration: Typically < 500ms for small CSV files

---

## Backend Function: `load_row_level_data()`

**Location:** `src/abtest.py`, lines 168-219  
**Purpose:** Load row-level A/B test data from CSV and aggregate to counts

### UI Trigger
- **Primary:** CSV file upload (same file input as aggregated)
- **File Format:** CSV with columns `user_id`, `group`, `converted`
- **Auto-Detection:** Detect format based on columns present

### Input Contract

**Function Signature:**
```python
load_row_level_data(filepath: str) -> Tuple[int, int, int, int]
```

**File Format:**
- Columns: `user_id`, `group`, `converted`
- `converted`: Must be 0 or 1
- `group`: Must be 'A' or 'B'

**Validation:**
- Same client-side validation as aggregated data
- Backend validates `converted` values are 0 or 1

### Output Contract

**Function Returns:**
```python
Tuple[int, int, int, int]  # (success_a, total_a, success_b, total_b)
```

**UI Display Mapping:**
- Same as `load_aggregated_data()` — populates sidebar inputs and triggers calculations

### Error States

**Additional Exceptions:**
| Exception | Trigger | UI Feedback | Component |
|-----------|---------|-------------|-----------|
| `ValueError("Converted column must contain only 0 or 1 values")` | Invalid converted values | Alert: "Error: Converted column must contain only 0 or 1 values" | Alert (error variant) |

---

## Data Flow Summary

```
User Input (Sidebar)
    ↓
[Validation (Client-Side)]
    ↓
Backend Function Call (ztest_two_prop, power, load_*)
    ↓
[Error Handling]
    ↓
Results → UI Display (Main Content)
    ↓
[Decision Logic (Client-Side)]
    ↓
Decision Banner Display
```

## Validation Summary Table

| Validation | Location | Error Message | UI Component |
|------------|----------|---------------|--------------|
| `success_a < 0` | Client | "Error: Success counts cannot be negative" | Alert (error), Input (error state) |
| `total_a <= 0` | Client | "Error: Total counts must be positive" | Alert (error), Input (error state) |
| `success_a > total_a` | Client | "Error: Success count cannot exceed total count" | Alert (error), Input (error state) |
| `alpha < 0.01` or `alpha > 0.10` | Client | "Error: Alpha must be between 0.01 and 0.10" | Alert (error) |
| `mde < 0.001` or `mde > 0.10` | Client | "Error: MDE must be between 0.1pp and 10.0pp" | Alert (error) |
| File not found | Backend | "Error: File not found: {filepath}" | Alert (error) |
| Missing CSV columns | Backend | "Error: Missing required columns: [...]" | Alert (error) |
| Invalid CSV format | Backend | "Error: [specific validation failure]" | Alert (error) |

---

**Next:** See `06-navigation-routing.md` for navigation and routing model (minimal for single-page app).

