"""
Reproduce Table 1-b: color/label distribution and empirical correlation rate.

Requires MNIST data. Will download it automatically.

Usage:
    python src/reproduce_table1b.py
"""

import numpy as np
from torchvision import datasets


def make_colors(y, rho, seed):
    """Reconstruct the coloring function used in the notebooks."""
    rng = np.random.RandomState(seed)
    keep = rng.rand(len(y)) < rho
    wrong = (y + rng.randint(1, 10, len(y))) % 10
    return np.where(keep, y, wrong)


def table1b():
    mn_tr = datasets.MNIST('./data', train=True, download=True)
    Y_tr = mn_tr.targets.numpy()

    seeds = [0, 1, 2, 3, 4]
    print("\n=== Table 1-b: Color/label distribution (5 seeds) ===")
    print(f"{'Set':15s} {'rho':5s} {'Empirical':>12s} {'Aligned':>12s} {'Conflicting':>14s}")

    for rho in [0.9, 0.99, 1.0]:
        for set_name, y in [("train", Y_tr)]:
            aligned_counts = []
            for seed in seeds:
                c = make_colors(y, rho, seed)
                aligned_counts.append(int((c == y).sum()))
            n = len(y)
            emp = np.mean(aligned_counts) / n
            emp_std = np.std(aligned_counts, ddof=1) / n
            print(f"{set_name:15s} {rho:<5.2f} {emp:.3f}+/-{emp_std:.3f} "
                  f"{np.mean(aligned_counts):8.0f}+/-{np.std(aligned_counts, ddof=1):.0f} "
                  f"{n - np.mean(aligned_counts):8.0f}+/-{np.std(aligned_counts, ddof=1):.0f}")


if __name__ == "__main__":
    table1b()
