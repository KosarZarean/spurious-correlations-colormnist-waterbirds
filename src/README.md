# Reproduction Scripts

These scripts reproduce all tables in the paper directly from the JSON files in `results/`.

## Scripts

| Script | Purpose | Output |
|---|---|---|
| `reproduce_all_tables.py` | Reproduces Tables 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15 | Console output |
| `reproduce_table1b.py` | Reproduces Table 1-b (color/label distribution) | Console output |
| `reproduce_table7.py` | Reproduces Table 7 (theory validation, 12/8 split) | Console output |
| `stats.py` | Reproduces p-values (Welch + Holm) and Cohen's d for Waterbirds | Console output |

## Usage

From the repository root:

```bash
python src/reproduce_all_tables.py
python src/stats.py
python src/reproduce_table1b.py
python src/reproduce_table7.py
