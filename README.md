# Spurious Correlations in Colored MNIST and Waterbirds

**A Comprehensive Empirical Study on Detecting and Mitigating Spurious Correlations in Image Classification**

**Author:** Kosar Zarean

**Paper:** Detecting and Mitigating Spurious Correlations in Image Classification: A Comprehensive Empirical Study on Colored MNIST and Waterbirds

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Overview

This repository contains the code, raw data, and reproduction scripts for the paper. All numbers, tables, and figures in the paper are reproduced from the JSON files in `results/*/results.json`.

**Note:** This paper is an empirical study, not a new method. Its contribution is a systematic comparison of five debiasing methods across the full ρ spectrum and two Colored MNIST designs.

---

## Repository Structure

```
spurious-correlations-colormnist-waterbirds/
├── README.md                          # This file
├── REPRODUCIBILITY_REPORT.md          # Mapping: paper → JSON → notebook
├── CITATION.cff
├── LICENSE
├── .gitignore
├── requirements.txt
│
├── notebooks/                         # Colab notebooks
│   ├── README.md
│   ├── colored_mnist_project.ipynb     (CNN3, ρ=0.9, 3 seeds)
│   ├── colored_mnist_10colors.ipynb    (10-color version)
│   ├── paper_experiments.ipynb         (5-seed sweep)
│   ├── colored_mnist_mlp_rho09.ipynb   (MLP, ρ=0.9)
│   ├── colored_mnist_mlp_rho99.ipynb   (MLP, ρ=0.99)
│   ├── colored_mnist_minimal.ipynb     (CNN1, ρ=0.9)
│   ├── colored_mnist_light.ipynb       (CNN2, ρ=0.9)
│   ├── colored_mnist_rho099.ipynb      (CNN3, ρ=0.99)
│   └── waterbirds_experiment.ipynb     (Waterbirds)
│
├── results/                           # Raw data (JSON)
│   ├── project_results/results.json             (CNN3, ρ=0.9)
│   ├── results_10colors/results.json            (10-color version)
│   ├── paper_results/results.json               (5-seed sweep)
│   ├── project_mlp_rho09/results.json           (MLP, ρ=0.9)
│   ├── project_mlp_rho99/results.json           (MLP, ρ=0.99)
│   ├── project_minimal_results/results.json     (CNN1, ρ=0.9)
│   ├── project_light_results/results.json       (CNN2, ρ=0.9)
│   ├── project_rho099_results/results.json      (CNN3, ρ=0.99)
│   └── results_waterbirds/raw_results.json      (Waterbirds)
│
├── figures/                           # Paper figures
│   ├── fig0_dataset_samples.png
│   ├── fig1_baseline_training_curves.png
│   ├── fig3_saliency.png
│   ├── fig4_gradcam.png
│   ├── fig_acc_vs_rho.png
│   ├── fig_drop_vs_rho.png
│   ├── fig_dropout.png
│   ├── fig_color_effect.png
│   ├── fig_theory_check.png
│   ├── fig_confusion_ood2.png
│   ├── fig_integrated_gradients.png
│   ├── fig5_methods_comparison.png
│   └── fig6_training_dynamics.png
│
└── src/                               # Reproduction code
    ├── README.md
    ├── reproduce_all_tables.py
    ├── reproduce_table1b.py
    ├── reproduce_table7.py
    └── stats.py
```

---

## Notebook-to-Table Mapping

| # | Notebook | Architecture / Version | JSON Output | Paper Tables | Paper Figures |
|---|---|---|---|---|---|
| 1 | `colored_mnist_project.ipynb` | CNN3 (main paper) | `results/project_results/results.json` | 2, 3, 4, 9, 10 | 2, 3, 4 |
| 2 | `colored_mnist_10colors.ipynb` | 10-color version | `results/results_10colors/results.json` | 13, 15 | — |
| 3 | `paper_experiments.ipynb` | MLP/CNN3, 5-seed sweep | `results/paper_results/results.json` | 5, 6, 7, 8 | 5, 6, 7, 8, 9, 10, 11 |
| 4 | `colored_mnist_mlp_rho09.ipynb` | MLP, ρ=0.9 | `results/project_mlp_rho09/results.json` | 11 (MLP ρ=0.9 column) | — |
| 5 | `colored_mnist_mlp_rho99.ipynb` | MLP, ρ=0.99 | `results/project_mlp_rho99/results.json` | 11 (MLP ρ=0.99 column) | — |
| 6 | `colored_mnist_minimal.ipynb` | CNN1, ρ=0.9 | `results/project_minimal_results/results.json` | 11 (CNN1 column) | — |
| 7 | `colored_mnist_light.ipynb` | CNN2, ρ=0.9 | `results/project_light_results/results.json` | 11 (CNN2 column) | — |
| 8 | `colored_mnist_rho099.ipynb` | CNN3, ρ=0.99 | `results/project_rho099_results/results.json` | 11 (CNN3 ρ=0.99 column) | — |
| 9 | `waterbirds_experiment.ipynb` | Waterbirds | `results/results_waterbirds/raw_results.json` | 12 | — |

### Table Descriptions

| Table | Content | Source Notebook | Reproduction Script |
|---|---|---|---|
| Table 1-b | Color/label distribution | (from raw data) | `src/reproduce_table1b.py` |
| Table 2 | Baseline evaluation | `colored_mnist_project.ipynb` | `src/reproduce_all_tables.py` |
| Table 3 | Counterfactual tests | `colored_mnist_project.ipynb` | `src/reproduce_all_tables.py` |
| Table 4 | Misspecification tests | `colored_mnist_project.ipynb` | `src/reproduce_all_tables.py` |
| Table 5 | ID/OOD accuracy and gap | `paper_experiments.ipynb` (+ `project_*`) | `src/reproduce_all_tables.py` |
| Table 6 | Dropout effect | `paper_experiments.ipynb` | `src/reproduce_all_tables.py` |
| Table 7 | Theory validation (MAE) | `paper_experiments.ipynb` | `src/reproduce_table7.py` |
| Table 8 | Per-digit error | `paper_experiments.ipynb` | `src/reproduce_all_tables.py` |
| Table 9 | Methods (two-color) | `colored_mnist_project.ipynb` | `src/reproduce_all_tables.py` |
| Table 10 | Color profile (two-color) | `colored_mnist_project.ipynb` | `src/reproduce_all_tables.py` |
| Table 11 | Methods × architectures | (6 notebooks combined) | `src/reproduce_all_tables.py` |
| Table 12 | Waterbirds | `waterbirds_experiment.ipynb` | `src/reproduce_all_tables.py` |
| Table 13 | Methods (10-color) | `colored_mnist_10colors.ipynb` | `src/reproduce_all_tables.py` |
| Table 14 | Two-design comparison | (Tables 9 and 13 combined) | `src/reproduce_all_tables.py` |
| Table 15 | Color profile (10-color) | `colored_mnist_10colors.ipynb` | `src/reproduce_all_tables.py` |
| Table 16 | Comparison with prior work | (manual) | (fixed in paper) |

---

## Installation and Usage

### Requirements

- Python 3.10+
- pip

### Installation

```bash
git clone https://github.com/KosarZarean/spurious-correlations-colormnist-waterbirds.git
cd spurious-correlations-colormnist-waterbirds
pip install -r requirements.txt
```

### Reproduce All Tables

```bash
python src/reproduce_all_tables.py
python src/stats.py
python src/reproduce_table1b.py
python src/reproduce_table7.py
```

### Reproduce a Specific Table

```bash
# Table 1-b (color/label distribution)
python src/reproduce_table1b.py

# Table 7 (theory validation and MAE)
python src/reproduce_table7.py

# p-values and Cohen's d (Waterbirds)
python src/stats.py

# All other tables
python src/reproduce_all_tables.py
```

### Reproduce from Notebooks

If you want to reproduce from scratch:

1. Open each notebook in Colab (Runtime → GPU)
2. Run all cells (Run all)
3. Save the resulting `results.json` in the corresponding folder
4. Run the reproduction script

Approximate time on a T4 GPU: 40–60 minutes per notebook.

---

## Raw Data

All raw JSON files are in the `results/*/` folders:

| File | Description | Seeds |
|---|---|---|
| `results/project_results/results.json` | CNN3, ρ=0.9 | 3 |
| `results/results_10colors/results.json` | 10-color version | 3 |
| `results/paper_results/results.json` | MLP/CNN3 sweep | 5 |
| `results/project_mlp_rho09/results.json` | MLP, ρ=0.9 | 3 |
| `results/project_mlp_rho99/results.json` | MLP, ρ=0.99 | 3 |
| `results/project_minimal_results/results.json` | CNN1, ρ=0.9 | 3 |
| `results/project_light_results/results.json` | CNN2, ρ=0.9 | 3 |
| `results/project_rho099_results/results.json` | CNN3, ρ=0.99 | 3 |
| `results/results_waterbirds/raw_results.json` | Waterbirds | 3 |

### JSON Structure

For `paper_results/results.json`, keys have the form `"{arch}|{rho}|{dropout}|{seed}"`:

```json
{
  "MLP|0.5|0.5|0": {
    "train": 0.9969,
    "val": 0.9701,
    "id": 0.9731,
    "ood1": 0.9733,
    "ood2": 0.9745,
    "id_aligned": 0.9706,
    "id_conflict": 0.9756,
    "swap_acc": 0.9746,
    "color_effect": 0.0139,
    "conf_ood2": [[968, 0, 1, "..."]]
  }
}
```

For `project_results/results.json` and `results_10colors/results.json`, the structure is different:

```json
{
  "cfg": {},
  "RES": {
    "Baseline": {
      "0": {"train": "...", "val": "...", "id": "...", "ood1": "...", "ood2": "..."}
    }
  },
  "CUE": {
    "Baseline": {
      "0": {"original": {}, "A_swap": {}}
    }
  }
}
```

Accuracy values are in the range [0, 1] (multiply by 100 for percentages).

---

## Limitations

### 1. Table 1-b (Color Distribution)

`src/reproduce_table1b.py` reproduces this table from raw MNIST data. No need to rerun the notebook.

### 2. Tables 3 and 4 (Counterfactual and Misspecification)

These tables require trained models. If models are not saved (`models/*.pth` is in `.gitignore`), these tables can only be reproduced by rerunning the notebook. Recommendation: upload models to GitHub Releases, not to git.

### 3. Number of Seeds

- CNN3, CNN2, MLP, Waterbirds: 3 or 5 seeds (depending on the file)
- 10-color: 3 seeds

With n=3 (or 5), statistical power is low. Results are reported as preliminary evidence, not definitive proof.

### 4. Limited Settings

- Waterbirds: 15 epochs (vs. 300 epochs in the original paper) and untuned hyperparameters
- IRM was not run on Waterbirds
- Hyperparameters for the five methods were not tuned

Therefore, the method comparison in this paper is a preliminary study, not a final and fair comparison.

---

## Dependencies

`requirements.txt`:

```
torch>=2.0.0
torchvision>=0.15.0
numpy>=1.24.0
pandas>=2.0.0
scipy>=1.10.0
matplotlib>=3.7.0
scikit-learn>=1.2.0
jupyter>=1.0.0
```

---

## Citation

If you use this code or data, please cite the paper:

```bibtex
@article{zarean2026spurious,
  title   = {Spurious Correlations in Colored MNIST and Waterbirds:
             A Comprehensive Empirical Study},
  author  = {Zarean, Kosar},
  year    = {2026},
  url     = {https://github.com/KosarZarean/spurious-correlations-colormnist-waterbirds}
}
```

---

## Contact

For questions or bug reports, please use GitHub Issues:

https://github.com/KosarZarean/spurious-correlations-colormnist-waterbirds/issues

---

## License

MIT License — see [LICENSE](LICENSE).
