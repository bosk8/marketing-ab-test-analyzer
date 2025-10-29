"""
A/B Test Statistical Analysis Functions

This module provides functions for analyzing A/B test results using
two-proportion z-tests and power analysis.
"""

import numpy as np
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest, power_proportions_2indep
from typing import Dict, Tuple


def ztest_two_prop(
        success_a: int,
        total_a: int,
        success_b: int,
        total_b: int,
        alpha: float = 0.05) -> Dict[str,
                                    float | Tuple[float,
                                                  float]]:
    """
    Perform a two-proportion z-test comparing conversion rates between
    variants A and B.

    Args:
        success_a: Number of successes (conversions) in variant A
        total_a: Total number of trials in variant A
        success_b: Number of successes (conversions) in variant B
        total_b: Total number of trials in variant B
        alpha: Significance level (default: 0.05)

    Returns:
        Dictionary containing:
            - z: z-statistic
            - p: two-sided p-value
            - lift: difference in proportions (pb - pa)
            - ci: 95% confidence interval for the difference (tuple)

    Raises:
        ValueError: If any input is invalid (negative, zero totals, etc.)
    """
    # Validate inputs
    if total_a <= 0 or total_b <= 0:
        raise ValueError("Total counts must be positive")
    if success_a < 0 or success_b < 0:
        raise ValueError("Success counts cannot be negative")
    if success_a > total_a or success_b > total_b:
        raise ValueError("Success counts cannot exceed total counts")
    if not 0 < alpha < 1:
        raise ValueError("Alpha must be between 0 and 1")

    count = np.array([success_a, success_b])
    nobs = np.array([total_a, total_b])

    # Perform two-sided z-test
    z, p = proportions_ztest(count, nobs, alternative="two-sided")

    # Calculate proportions
    pa, pb = count / nobs

    # Calculate standard error for difference in proportions
    se = np.sqrt(pa * (1 - pa) / total_a + pb * (1 - pb) / total_b)

    # Calculate lift (difference)
    diff = pb - pa

    # Calculate z-critical value for confidence interval
    zcrit = stats.norm.ppf(1 - alpha / 2)

    # Calculate confidence interval
    ci = (float(diff - zcrit * se), float(diff + zcrit * se))

    return {
        "z": float(z),
        "p": float(p),
        "lift": float(diff),
        "ci": ci
    }


def power(n_a: int, n_b: int, p_control: float, min_detectable_diff: float = 0.02, alpha: float = 0.05) -> float:
    """
    Compute statistical power for detecting a minimum detectable effect (MDE).

    Args:
        n_a: Sample size for control group (variant A)
        n_b: Sample size for treatment group (variant B)
        p_control: Control group conversion rate (proportion, 0-1)
        min_detectable_diff: Minimum detectable effect size (difference in
                             proportions, default: 0.02)
        alpha: Significance level (default: 0.05)

    Returns:
        Statistical power (probability of detecting the effect) as a float between 0 and 1

    Raises:
        ValueError: If inputs are invalid
    """
    # Validate inputs
    if n_a <= 0 or n_b <= 0:
        raise ValueError("Sample sizes must be positive")
    if not 0 <= p_control <= 1:
        raise ValueError("Control proportion must be between 0 and 1")
    if not 0 < alpha < 1:
        raise ValueError("Alpha must be between 0 and 1")

    ratio = n_b / n_a
    res = power_proportions_2indep(
        diff=min_detectable_diff,
        prop2=p_control,
        nobs1=n_a,
        ratio=ratio,
        alpha=alpha
    )
    return float(res.power)


def load_aggregated_data(filepath: str) -> Tuple[int, int, int, int]:
    """
    Load aggregated A/B test data from CSV file.

    Expected CSV format:
        group,success,total
        A,123,5000
        B,155,5000

    Args:
        filepath: Path to the CSV file

    Returns:
        Tuple of (success_a, total_a, success_b, total_b)

    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If data format is invalid or missing expected groups
"""
    import pandas as pd

    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")

    # Validate required columns
    required_cols = ['group', 'success', 'total']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    # Extract data for variants A and B
    group_a = df[df['group'] == 'A']
    group_b = df[df['group'] == 'B']

    if len(group_a) == 0:
        raise ValueError("Variant A data not found in CSV")
    if len(group_b) == 0:
        raise ValueError("Variant B data not found in CSV")

    # Get first row for each group (in case of duplicates)
    success_a = int(group_a.iloc[0]['success'])
    total_a = int(group_a.iloc[0]['total'])
    success_b = int(group_b.iloc[0]['success'])
    total_b = int(group_b.iloc[0]['total'])

    # Validate data
    if success_a < 0 or success_b < 0:
        raise ValueError("Success counts cannot be negative")
    if total_a <= 0 or total_b <= 0:
        raise ValueError("Total counts must be positive")
    if success_a > total_a or success_b > total_b:
        raise ValueError("Success counts cannot exceed total counts")

    return success_a, total_a, success_b, total_b


def load_row_level_data(filepath: str) -> Tuple[int, int, int, int]:
    """
    Load row-level A/B test data from CSV and aggregate to counts.

    Expected CSV format:
        user_id,group,converted
        u1,A,0
        u2,B,1

    Args:
        filepath: Path to the CSV file

    Returns:
        Tuple of (success_a, total_a, success_b, total_b)

    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If data format is invalid
    """
    import pandas as pd

    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")

    # Validate required columns
    required_cols = ['user_id', 'group', 'converted']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    # Filter for variants A and B
    group_a = df[df['group'] == 'A']
    group_b = df[df['group'] == 'B']

    if len(group_a) == 0:
        raise ValueError("Variant A data not found in CSV")
    if len(group_b) == 0:
        raise ValueError("Variant B data not found in CSV")

    # Aggregate counts
    total_a = len(group_a)
    success_a = int(group_a['converted'].sum())
    total_b = len(group_b)
    success_b = int(group_b['converted'].sum())

    # Validate converted values are 0 or 1
    if not df['converted'].isin([0, 1]).all():
        raise ValueError("Converted column must contain only 0 or 1 values")

    return success_a, total_a, success_b, total_b
