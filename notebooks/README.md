# Notebooks

Each notebook trains models and saves results to `results/<name>/results.json`.

## Order of Execution

Run in this order (each depends on the previous):

| # | Notebook | Output JSON | Purpose |
|---|---|---|---|
| 1 | `colored_mnist_project.ipynb` | `results/project_results/results.json` | CNN3, ρ=0.9, 3 seeds (Tables 9, 10, 11) |
| 2 | `colored_mnist_10colors.ipynb` | `results/results_10colors/results.json` | 10-color version (Tables 13, 15) |
| 3 | `paper_experiments.ipynb` | `results/paper_results/results.json` | MLP/CNN3 sweep, 5 seeds (Tables 5, 6, 7, 8) |
| 4 | `colored_mnist_mlp_rho09.ipynb` | `results/project_mlp_rho09/results.json` | MLP, ρ=0.9 (Table 11) |
| 5 | `colored_mnist_mlp_rho99.ipynb` | `results/project_mlp_rho99/results.json` | MLP, ρ=0.99 (Table 11) |
| 6 | `colored_mnist_minimal.ipynb` | `results/project_minimal_results/results.json` | CNN1, ρ=0.9 (Table 11) |
| 7 | `colored_mnist_light.ipynb` | `results/project_light_results/results.json` | CNN2, ρ=0.9 (Table 11) |
| 8 | `colored_mnist_rho099.ipynb` | `results/project_rho099_results/results.json` | CNN3, ρ=0.99 (Table 11) |
| 9 | `waterbirds_experiment.ipynb` | `results/results_waterbirds/raw_results.json` | Waterbirds (Table 12) |

## GPU Requirements

- Colored MNIST notebooks: approximately 1 GPU (e.g., Colab T4), 30–60 minutes each.
- Waterbirds notebook: approximately 1 GPU, 2–3 hours.
- Total: 6–8 hours on a single GPU.

## Reproduction

If you only want to reproduce the tables (not retrain), you can skip the notebooks and use the pre-computed JSON files in `results/`. See `src/reproduce_all_tables.py`.
