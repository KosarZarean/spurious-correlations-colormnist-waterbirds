# Data

This directory is for local data only. It is excluded from version control
via `.gitignore`.

## What Goes Here

- MNIST raw files (downloaded automatically by `torchvision`)
- Waterbirds dataset (download from the official source)

## MNIST

The notebooks and `src/reproduce_table1b.py` download MNIST automatically
to `./data/`. No manual download is required.

## Waterbirds

The Waterbirds dataset is not included in this repository due to its size
and licensing. To obtain it, follow the instructions in the original paper:

> Sagawa, S., Koh, P. W., Hashimoto, T. B., Liang, P.
> Distributionally Robust Neural Networks. ICLR 2020.
> https://arxiv.org/abs/1911.08731

After downloading, place the data in `data/waterbirds/` and update the path
in `notebooks/waterbirds_experiment.ipynb` accordingly.

## Reproducibility

The JSON outputs in `results/` were produced from these raw data files.
If you want to retrain the models from scratch, you must first download
the data as described above.
