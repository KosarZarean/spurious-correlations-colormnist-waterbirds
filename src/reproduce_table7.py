"""
Reproduce Table 7: validation of Eq. (1) and (2) with 12/8 split.

Usage:
    python src/reproduce_table7.py
"""

import json
import numpy as np
from pathlib import Path

RESULTS_DIR = Path(__file__).parent.parent / "results"


def load_json(rel_path: str) -> dict:
    path = RESULTS_DIR / rel_path
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_metric(data, arch, rho, metric):
    """Average a metric over seeds for a given (arch, rho)."""
    key_prefix = f"{arch}|{rho}|0.5|"
    seeds = [k for k in data if k.startswith(key_prefix)]
    if not seeds:
        return None
    return float(np.mean([data[k][metric] for k in seeds]))


def compute_mae(data, configs):
    """Compute MAE of Eq. (1) over a list of (arch, rho) configs."""
    errors = []
    for arch, rho in configs:
        a = get_metric(data, arch, rho, "id_aligned")
        c = get_metric(data, arch, rho, "id_conflict")
        ood2 = get_metric(data, arch, rho, "ood2")
        if a is None or c is None or ood2 is None:
            continue
        pred = 0.1 * a + 0.9 * c
        errors.append(abs(ood2 - pred))
    return np.mean(errors) * 100 if errors else None, errors


def table7():
    data = load_json("paper_results/results.json")

    train_cfgs = [(a, r) for a in ["CNN1", "CNN2", "CNN3"]
                  for r in [0.5, 0.7, 0.9, 0.95]]
    test_cfgs = ([("MLP", r) for r in [0.5, 0.7, 0.9, 0.95, 0.99]]
                 + [(a, 0.99) for a in ["CNN1", "CNN2", "CNN3"]])

    print("\n=== Table 7: Theory validation ===")
    mae_train, errs_train = compute_mae(data, train_cfgs)
    mae_test, errs_test = compute_mae(data, test_cfgs)

    print(f"In-sample (12 configs):    MAE = {mae_train:.2f}  (max = {max(errs_train)*100:.2f})")
    print(f"Out-of-sample (8 configs): MAE = {mae_test:.2f}  (max = {max(errs_test)*100:.2f})")


if __name__ == "__main__":
    table7()
