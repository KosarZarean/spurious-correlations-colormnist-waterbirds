
"""
Reproduce p-values (Welch + Holm) and Cohen's d for Waterbirds.

Usage:
    python src/stats.py
"""

import json
import numpy as np
from scipy import stats
from pathlib import Path

RESULTS_DIR = Path(__file__).parent.parent / "results"


def load_json(rel_path: str) -> dict:
    path = RESULTS_DIR / rel_path
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def welch_ttest(a, b):
    """Welch t-test (unequal variances)."""
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    t, p = stats.ttest_ind(a, b, equal_var=False)
    return t, p


def cohens_d(a, b):
    """Cohen's d for independent samples."""
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    n1, n2 = len(a), len(b)
    s1, s2 = np.var(a, ddof=1), np.var(b, ddof=1)
    s_pooled = np.sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))
    return (np.mean(a) - np.mean(b)) / s_pooled


def holm_correction(p_values):
    """Holm-Bonferroni correction."""
    p = np.array(p_values, dtype=float)
    n = len(p)
    sorted_idx = np.argsort(p)
    sorted_p = p[sorted_idx]
    adjusted = np.minimum.accumulate(sorted_p * (n - np.arange(n)))
    adjusted = np.minimum(adjusted, 1.0)
    result = np.empty_like(adjusted)
    result[sorted_idx] = adjusted
    return result


def waterbirds_pvalues():
    data = load_json("results_waterbirds/raw_results.json")
    erm = [data[f"ERM|{s}"]["test"]["worst"] for s in [0, 1, 2]]
    rw = [data[f"Reweighting|{s}"]["test"]["worst"] for s in [0, 1, 2]]
    dro = [data[f"GroupDRO|{s}"]["test"]["worst"] for s in [0, 1, 2]]

    comparisons = [
        ("ERM vs Reweighting", erm, rw),
        ("ERM vs GroupDRO", erm, dro),
        ("Reweighting vs GroupDRO", rw, dro),
    ]

    raw_ps = []
    print("\n=== Waterbirds: Welch t-test + Holm correction ===")
    for name, a, b in comparisons:
        t, p = welch_ttest(a, b)
        d = cohens_d(a, b)
        raw_ps.append(p)
        print(f"{name:30s} t={t:7.4f}  p={p:.6f}  d={d:.4f}")

    adjusted = holm_correction(raw_ps)
    print("\nAfter Holm correction:")
    for (name, _, _), p_adj in zip(comparisons, adjusted):
        print(f"{name:30s} p_holm={p_adj:.6f}")


if __name__ == "__main__":
    waterbirds_pvalues()
