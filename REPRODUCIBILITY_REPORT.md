# Reproducibility Report

This report maps every number in the paper to its source JSON file and the exact key used to extract it.

**Principle:** The JSON files in `results/` are the single source of truth. Every number in the paper is directly extractable from them. If a number in the paper cannot be reproduced from the JSONs, it is marked as a discrepancy below.

---

## 1. Table 5 — All Architectures × ρ (5 seeds)

**Source:** `results/paper_results/results.json` (for MLP and CNN3 across all ρ), plus:
- `results/project_mlp_rho09/results.json` (MLP, ρ=0.9, 3 seeds)
- `results/project_mlp_rho99/results.json` (MLP, ρ=0.99, 3 seeds)
- `results/project_minimal_results/results.json` (CNN1, ρ=0.9, 3 seeds)
- `results/project_light_results/results.json` (CNN2, ρ=0.9, 3 seeds)
- `results/project_results/results.json` (CNN3, ρ=0.9, 3 seeds)
- `results/project_rho099_results/results.json` (CNN3, ρ=0.99, 3 seeds)

**Extraction:** For each configuration `ARCH|ρ|0.5|seed`, compute `id - ood2` and average over seeds.

| Architecture | ρ | ID | OOD-1 | OOD-2 | Gap | JSON Key |
|---|---|---|---|---|---|---|
| MLP | 0.5 | 97.48 | 97.47 | 97.49 | −0.03 | `MLP\|0.5\|0.5\|{0,1,2,3,4}` |
| MLP | 0.7 | 97.58 | 97.20 | 96.56 | 1.02 | `MLP\|0.7\|0.5\|{0,1,2,3,4}` |
| MLP | 0.9 | 97.96 | 95.31 | 92.83 | 5.13 | `MLP\|0.9\|0.5\|{0,1,2,3,4}` |
| MLP | 0.95 | 98.23 | 93.38 | 89.29 | 8.94 | `MLP\|0.95\|0.5\|{0,1,2,3,4}` |
| MLP | 0.99 | 98.65 | 79.69 | 64.35 | 34.31 | `MLP\|0.99\|0.5\|{0,1,2,3,4}` |
| CNN1 | 0.5 | 98.77 | 98.78 | 98.79 | −0.02 | (no JSON) |
| CNN1 | 0.7 | 98.79 | 98.58 | 98.27 | 0.52 | (no JSON) |
| CNN1 | 0.9 | 98.91 | 97.76 | 96.58 | 2.33 | `Baseline\|{0,1,2}` in `project_minimal_results` |
| CNN1 | 0.95 | 99.07 | 96.88 | 94.92 | 4.15 | (no JSON) |
| CNN1 | 0.99 | 99.18 | 90.12 | 82.82 | 16.36 | (no JSON) |
| CNN2 | 0.5 | 99.18 | 99.18 | 99.18 | 0.00 | (no JSON) |
| CNN2 | 0.7 | 99.18 | 99.07 | 98.88 | 0.30 | (no JSON) |
| CNN2 | 0.9 | 99.31 | 98.59 | 97.87 | 1.43 | `Baseline\|{0,1,2}` in `project_light_results` |
| CNN2 | 0.95 | 99.39 | 97.91 | 96.59 | 2.80 | (no JSON) |
| CNN2 | 0.99 | 99.50 | 93.04 | 87.85 | 11.66 | (no JSON) |
| CNN3 | 0.5 | 99.16 | 99.16 | 99.20 | −0.04 | `CNN3\|0.5\|0.5\|{0,1,2,3,4}` |
| CNN3 | 0.7 | 99.13 | 99.07 | 98.92 | 0.21 | `CNN3\|0.7\|0.5\|{0,1,2,3,4}` |
| CNN3 | 0.9 | 99.32 | 98.65 | 97.92 | 1.41 | `CNN3\|0.9\|0.5\|{0,1,2,3,4}` |
| CNN3 | 0.95 | 99.36 | 98.07 | 96.99 | 2.37 | `CNN3\|0.95\|0.5\|{0,1,2,3,4}` |
| CNN3 | 0.99 | 99.46 | 93.63 | 88.90 | 10.56 | `CNN3\|0.99\|0.5\|{0,1,2,3,4}` |

**Discrepancies:**

1. CNN1 and CNN2 for ρ=0.5, 0.7, 0.95, 0.99: No JSON files are available in this repository. The paper reports these numbers, but they cannot be reproduced from the current data. Action required: either upload the missing JSONs or remove these rows from the paper.
2. CNN3 ρ=0.99: The paper reports 10.56 (5 seeds). The 3-seed mean from `project_rho099_results` is 8.90. The 5-seed mean from `paper_results` is 10.16, not 10.56. Action required: correct the paper to 10.16 (5 seeds) or 8.90 (3 seeds).
3. MLP ρ=0.99: The paper reports 34.31 (5 seeds). The 3-seed mean from `project_mlp_rho99` is 27.07. The 5-seed mean from `paper_results` is 32.42, not 34.31. Action required: correct the paper to 32.42 (5 seeds) or 27.07 (3 seeds).

---

## 2. Table 6 — Dropout Effect (5 seeds)

**Source:** `results/paper_results/results.json`

**Extraction:** For each configuration `ARCH|ρ|dropout|seed`, compute `id - ood2` and average over seeds.

| Architecture | ρ | Dropout | ID | OOD-2 | Gap | JSON Key |
|---|---|---|---|---|---|---|
| CNN3 | 0.9 | 0.0 | 99.21 | 97.93 | 1.28 | `CNN3\|0.9\|0.0\|{0,1,2,3,4}` |
| CNN3 | 0.9 | 0.2 | 99.23 | 97.82 | 1.41 | `CNN3\|0.9\|0.2\|{0,1,2,3,4}` |
| CNN3 | 0.9 | 0.5 | 99.32 | 97.92 | 1.41 | `CNN3\|0.9\|0.5\|{0,1,2,3,4}` |
| CNN3 | 0.9 | 0.7 | 99.36 | 98.02 | 1.34 | `CNN3\|0.9\|0.7\|{0,1,2,3,4}` |
| CNN3 | 0.99 | 0.0 | 99.43 | 90.94 | 8.48 | `CNN3\|0.99\|0.0\|{0,1,2,3,4}` |
| CNN3 | 0.99 | 0.2 | 99.37 | 88.69 | 10.68 | `CNN3\|0.99\|0.2\|{0,1,2,3,4}` |
| CNN3 | 0.99 | 0.5 | 99.46 | 88.90 | 10.56 | `CNN3\|0.99\|0.5\|{0,1,2,3,4}` |
| CNN3 | 0.99 | 0.7 | 99.52 | 90.07 | 9.45 | `CNN3\|0.99\|0.7\|{0,1,2,3,4}` |
| MLP | 0.9 | 0.0 | 97.75 | 93.05 | 4.70 | `MLP\|0.9\|0.0\|{0,1,2,3,4}` |
| MLP | 0.9 | 0.2 | 97.85 | 92.85 | 5.00 | `MLP\|0.9\|0.2\|{0,1,2,3,4}` |
| MLP | 0.9 | 0.5 | 97.96 | 92.83 | 5.13 | `MLP\|0.9\|0.5\|{0,1,2,3,4}` |
| MLP | 0.9 | 0.7 | 97.69 | 91.09 | 6.60 | `MLP\|0.9\|0.7\|{0,1,2,3,4}` |
| MLP | 0.99 | 0.0 | 98.58 | 70.03 | 28.55 | `MLP\|0.99\|0.0\|{0,1,2,3,4}` |
| MLP | 0.99 | 0.2 | 98.56 | 69.29 | 29.26 | `MLP\|0.99\|0.2\|{0,1,2,3,4}` |
| MLP | 0.99 | 0.5 | 98.65 | 64.35 | 34.31 | `MLP\|0.99\|0.5\|{0,1,2,3,4}` |
| MLP | 0.99 | 0.7 | 98.41 | 59.19 | 39.22 | `MLP\|0.99\|0.7\|{0,1,2,3,4}` |

**Note:** The Dropout=0.5 rows are identical to Table 5 (same configurations). The paper correctly uses these as the default rows.

---

## 3. Table 9 — Methods (two-color, CNN3, ρ=0.9, 3 seeds)

**Source:** `results/project_results/results.json`

| Method | ID | OOD-1 | OOD-2 | ID−OOD1 | ID−OOD2 | JSON Key |
|---|---|---|---|---|---|---|
| Baseline | 99.30 | 98.59 | 97.92 | 0.71 | 1.38 | `Baseline\|{0,1,2}` |
| Augmentation | 99.33 | 98.87 | 98.49 | 0.46 | 0.84 | `M1_Augmentation\|{0,1,2}` |
| Reweighting | 99.10 | 98.89 | 98.72 | 0.21 | 0.38 | `M2_Reweighting\|{0,1,2}` |
| Group DRO | 99.24 | 98.82 | 98.43 | 0.42 | 0.82 | `M3_GroupDRO\|{0,1,2}` |
| LfF | 98.46 | 97.74 | 97.03 | 0.72 | 1.43 | `M4_LfF\|{0,1,2}` |
| IRM | 98.84 | 98.66 | 98.40 | 0.18 | 0.44 | `M5_IRM\|{0,1,2}` |

All values match the paper exactly.

---

## 4. Table 12 — Waterbirds (3 seeds)

**Source:** `results/results_waterbirds/raw_results.json`

| Method | worst-group | mean-group | sample-acc | JSON Key |
|---|---|---|---|---|
| ERM | 68.07 ± 0.56 | 84.77 ± 0.56 | 86.69 ± 0.85 | `ERM\|{0,1,2}` → `test.worst`, `test.mean_group`, `test.sample_acc` |
| Reweighting | 85.25 ± 1.25 | 90.60 ± 0.23 | 92.28 ± 0.88 | `Reweighting\|{0,1,2}` |
| GroupDRO | 82.04 ± 4.70 | 90.86 ± 0.90 | 92.14 ± 0.48 | `GroupDRO\|{0,1,2}` |

**Discrepancy:**

- The paper reports std of 1.40, 3.13, 11.70 for the three methods. The JSON gives 0.56, 1.25, 4.70. Action required: either (a) correct the paper to use the JSON std (0.56, 1.25, 4.70), or (b) document in the paper that the std was computed from a different source (e.g., 5 seeds, or ddof=0).
- The mean values (68.07, 85.25, 82.04) match exactly.

**p-values (Welch + Holm):**

The paper reports:
- ERM vs Reweighting: p=0.0004, p_holm=0.0012
- ERM vs GroupDRO: p=0.0343, p_holm=0.0686
- Reweighting vs GroupDRO: p=0.3584, p_holm=0.3584

To reproduce these, run `python src/stats.py`. The exact values depend on the t-test implementation (Welch vs Student) and the Holm correction. See `src/stats.py` for the implementation.

- ERM vs GroupDRO p-value matches exactly (0.0343).
- ERM vs Reweighting p-value: the JSON-based calculation gives a smaller p-value (approximately 0.00004) than the paper (0.0004). Action required: document the exact t-test implementation in the paper, or update the paper to the computed value.

---

## 5. Table 13 — Methods (10-color, CNN3, ρ=0.9, 3 seeds)

**Source:** `results/results_10colors/results.json`

| Method | ID | OOD-1 | OOD-2 | ID−OOD1 | ID−OOD2 | JSON Key |
|---|---|---|---|---|---|---|
| Baseline | 99.65 | 97.61 | 97.33 | 2.04 | 2.32 | `Baseline\|{0,1,2}` |
| Augmentation | 99.54 | 97.98 | 97.75 | 1.56 | 1.79 | `M1_Augmentation\|{0,1,2}` |
| Reweighting | 99.23 | 98.61 | 98.54 | 0.62 | 0.69 | `M2_Reweighting\|{0,1,2}` |
| Group DRO | 99.55 | 98.06 | 97.70 | 1.49 | 1.85 | `M3_GroupDRO\|{0,1,2}` |
| LfF | 98.91 | 97.34 | 97.16 | 1.57 | 1.75 | `M4_LfF\|{0,1,2}` |
| IRM | 99.01 | 97.22 | 97.13 | 1.79 | 1.88 | `M5_IRM\|{0,1,2}` |

All values match the paper exactly.

---

## 6. Table 15 — Color Profile (10-color, 3 seeds)

**Source:** `results/results_10colors/results.json`

| Method | A_swap.acc | B_gray_sum.acc | M_shape_shuffle.follow | JSON Key |
|---|---|---|---|---|
| Baseline | 97.0 | 96.8 | 25.9 | `CUE.Baseline.{0,1,2}` |
| Augmentation | 97.7 | 97.6 | 20.8 | `CUE.M1_Augmentation.{0,1,2}` |
| Reweighting | 98.3 | 98.0 | 14.6 | `CUE.M2_Reweighting.{0,1,2}` |
| GroupDRO | 97.3 | 97.6 | 23.3 | `CUE.M3_GroupDRO.{0,1,2}` |
| LfF | 97.2 | 96.2 | 17.8 | `CUE.M4_LfF.{0,1,2}` |
| IRM | 97.0 | 96.7 | 21.3 | `CUE.M5_IRM.{0,1,2}` |

**Discrepancy:**

- The paper reports `M_shape_shuffle.follow` values of 25.9, 20.8, 14.6, 23.3, 17.8, 21.3.
- The JSON gives `M_shape_shuffle.follow` values of 24.2, 65.0, 63.4, 71.1, 65.4, 54.2 (from `results_10colors`).
- The JSON also has `M_color_swap.follow` values of 12.2, 11.6, 10.8, 11.9, 14.1, 11.4 (these are close to the paper's numbers, but not exact).

Action required: the paper's "color-following rate after shape corruption" must be mapped to the exact JSON key. If the paper used `M_color_swap.follow` (not `M_shape_shuffle.follow`), update the label in the paper. If the paper used a different definition, document it.

---

## 7. Reproducing All Tables

```bash
python src/reproduce_all_tables.py
python src/stats.py
python src/reproduce_table1b.py
python src/reproduce_table7.py
```

See `src/README.md` for details.

---

## Summary of Discrepancies

| # | Location | Paper | JSON | Action |
|---|---|---|---|---|
| 1 | Table 5, CNN3 ρ=0.99 | 10.56 | 10.16 (5 seeds) / 8.90 (3 seeds) | Correct to 10.16 or 8.90 |
| 2 | Table 5, MLP ρ=0.99 | 34.31 | 32.42 (5 seeds) / 27.07 (3 seeds) | Correct to 32.42 or 27.07 |
| 3 | Table 5, CNN1/CNN2 (ρ=0.5, 0.7, 0.95, 0.99) | reported | missing | Upload JSONs or remove rows |
| 4 | Table 12, std | 1.40 / 3.13 / 11.70 | 0.56 / 1.25 / 4.70 | Correct std, or document source |
| 5 | Table 12, ERM vs RW p-value | 0.0004 | approximately 0.00004 | Document t-test, or correct |
| 6 | Table 15, follow column | 25.9 / 20.8 / 14.6 ... | 24.2 / 65.0 / 63.4 ... | Clarify metric, or correct |

---

## Notes

- Seed mismatch: For MLP and CNN3 at ρ=0.99, there are two independent runs: a 5-seed run (Table 5) and a 3-seed run (Table 9 / Table 11). The difference is due to seeds 3 and 4, which are only present in the 5-seed run. This is documented in Table 3-d.
- NaN handling: In ρ=1.0 configurations, `id_conflict` is NaN (no conflicting samples exist). This is expected and handled in all analyses.
- Missing JSONs: CNN1 and CNN2 for ρ≠0.9 are not available. If you want to include them in the paper, you must either run the missing experiments or remove those rows from Table 5.
