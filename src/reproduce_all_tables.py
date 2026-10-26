"""
Reproduce all tables from the paper using the JSON files in results/.

Usage:
    python src/reproduce_all_tables.py
"""

import json
import numpy as np
from pathlib import Path

RESULTS_DIR = Path(__file__).parent.parent / "results"


def load_json(rel_path: str) -> dict:
    """Load a JSON file from results/."""
    path = RESULTS_DIR / rel_path
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def mean_std(values, ddof=1):
    """Return (mean, std) in percent."""
    arr = np.array(values, dtype=float) * 100.0
    m = arr.mean()
    s = arr.std(ddof=ddof) if len(arr) > 1 else 0.0
    return m, s


# ---------------------------------------------------------------------------
# Table 5: All architectures x rho (5 seeds, from paper_results)
# ---------------------------------------------------------------------------

def reproduce_table5():
    data = load_json("paper_results/results.json")
    print("\n=== Table 5: All architectures x rho (5 seeds) ===")
    print(f"{'Arch':6s} {'rho':5s} {'ID':>10s} {'OOD-1':>10s} {'OOD-2':>10s} {'Gap':>10s}")

    for arch in ["MLP", "CNN1", "CNN2", "CNN3"]:
        for rho in [0.5, 0.7, 0.9, 0.95, 0.99]:
            key_prefix = f"{arch}|{rho}|0.5|"
            seeds = [k for k in data if k.startswith(key_prefix)]
            if not seeds:
                print(f"{arch:6s} {rho:<5.2f} {'(no data)':>40s}")
                continue
            ids = [data[k]["id"] for k in seeds]
            ood1 = [data[k]["ood1"] for k in seeds]
            ood2 = [data[k]["ood2"] for k in seeds]
            gaps = [data[k]["id"] - data[k]["ood2"] for k in seeds]
            id_m, id_s = mean_std(ids)
            o1_m, o1_s = mean_std(ood1)
            o2_m, o2_s = mean_std(ood2)
            g_m, g_s = mean_std(gaps)
            print(f"{arch:6s} {rho:<5.2f} {id_m:6.2f}+/-{id_s:.2f} "
                  f"{o1_m:6.2f}+/-{o1_s:.2f} {o2_m:6.2f}+/-{o2_s:.2f} "
                  f"{g_m:6.2f}+/-{g_s:.2f}")


# ---------------------------------------------------------------------------
# Table 9: Methods (two-color, CNN3, rho=0.9, 3 seeds)
# ---------------------------------------------------------------------------

def reproduce_table9():
    data = load_json("project_results/results.json")
    print("\n=== Table 9: Methods (two-color, CNN3, rho=0.9, 3 seeds) ===")
    print(f"{'Method':20s} {'ID':>10s} {'OOD-1':>10s} {'OOD-2':>10s} {'ID-OOD2':>10s}")

    methods = ["Baseline", "M1_Augmentation", "M2_Reweighting",
               "M3_GroupDRO", "M4_LfF", "M5_IRM"]
    for m in methods:
        seeds = list(data["RES"][m].keys())
        ids = [data["RES"][m][s]["id"] for s in seeds]
        ood1 = [data["RES"][m][s]["ood1"] for s in seeds]
        ood2 = [data["RES"][m][s]["ood2"] for s in seeds]
        gaps = [data["RES"][m][s]["id"] - data["RES"][m][s]["ood2"] for s in seeds]
        id_m, id_s = mean_std(ids)
        o1_m, o1_s = mean_std(ood1)
        o2_m, o2_s = mean_std(ood2)
        g_m, g_s = mean_std(gaps)
        print(f"{m:20s} {id_m:6.2f}+/-{id_s:.2f} {o1_m:6.2f}+/-{o1_s:.2f} "
              f"{o2_m:6.2f}+/-{o2_s:.2f} {g_m:6.2f}+/-{g_s:.2f}")


# ---------------------------------------------------------------------------
# Table 12: Waterbirds (3 seeds)
# ---------------------------------------------------------------------------

def reproduce_table12():
    data = load_json("results_waterbirds/raw_results.json")
    print("\n=== Table 12: Waterbirds (3 seeds) ===")
    print(f"{'Method':15s} {'worst-group':>15s} {'mean-group':>15s} {'sample-acc':>15s}")

    for m in ["ERM", "Reweighting", "GroupDRO"]:
        seeds = [k for k in data if k.startswith(f"{m}|")]
        worsts = [data[k]["test"]["worst"] for k in seeds]
        means = [data[k]["test"]["mean_group"] for k in seeds]
        samples = [data[k]["test"]["sample_acc"] for k in seeds]
        w_m, w_s = mean_std(worsts)
        m_m, m_s = mean_std(means)
        s_m, s_s = mean_std(samples)
        print(f"{m:15s} {w_m:6.2f}+/-{w_s:.2f} {m_m:6.2f}+/-{m_s:.2f} {s_m:6.2f}+/-{s_s:.2f}")


# ---------------------------------------------------------------------------
# Table 13: Methods (10-color, CNN3, rho=0.9, 3 seeds)
# ---------------------------------------------------------------------------

def reproduce_table13():
    data = load_json("results_10colors/results.json")
    print("\n=== Table 13: Methods (10-color, CNN3, rho=0.9, 3 seeds) ===")
    print(f"{'Method':20s} {'ID':>10s} {'OOD-1':>10s} {'OOD-2':>10s} {'ID-OOD2':>10s}")

    methods = ["Baseline", "M1_Augmentation", "M2_Reweighting",
               "M3_GroupDRO", "M4_LfF", "M5_IRM"]
    for m in methods:
        seeds = list(data["RES"][m].keys())
        ids = [data["RES"][m][s]["id"] for s in seeds]
        ood1 = [data["RES"][m][s]["ood1"] for s in seeds]
        ood2 = [data["RES"][m][s]["ood2"] for s in seeds]
        gaps = [data["RES"][m][s]["id"] - data["RES"][m][s]["ood2"] for s in seeds]
        id_m, id_s = mean_std(ids)
        o1_m, o1_s = mean_std(ood1)
        o2_m, o2_s = mean_std(ood2)
        g_m, g_s = mean_std(gaps)
        print(f"{m:20s} {id_m:6.2f}+/-{id_s:.2f} {o1_m:6.2f}+/-{o1_s:.2f} "
              f"{o2_m:6.2f}+/-{o2_s:.2f} {g_m:6.2f}+/-{g_s:.2f}")


# ---------------------------------------------------------------------------
# Table 8: Per-digit error on OOD-2 (MLP and CNN3, rho=0.99)
# ---------------------------------------------------------------------------

def reproduce_table8():
    data = load_json("paper_results/results.json")
    print("\n=== Table 8: Per-digit error on OOD-2 (MLP vs CNN3, rho=0.99) ===")

    for arch in ["MLP", "CNN3"]:
        key_prefix = f"{arch}|0.99|0.5|"
        seeds = [k for k in data if k.startswith(key_prefix)]
        conf = np.zeros((10, 10))
        for k in seeds:
            conf += np.array(data[k]["conf_ood2"])
        row_sums = conf.sum(axis=1, keepdims=True)
        conf_norm = conf / row_sums
        errors = (1 - np.diag(conf_norm)) * 100
        print(f"{arch:5s} per-digit error:", " ".join(f"{e:.1f}" for e in errors))
        print(f"{arch:5s} mean error: {errors.mean():.1f}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    reproduce_table5()
    reproduce_table9()
    reproduce_table12()
    reproduce_table13()
    reproduce_table8()
    print("\nDone.")
