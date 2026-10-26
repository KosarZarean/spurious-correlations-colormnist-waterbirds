# Changelog

All notable changes to this repository will be documented in this file.

## [1.0.0] - 2026-10-26

### Added
- Initial release of the code, data, and reproduction scripts.
- 9 Jupyter notebooks covering all experiments.
- 9 JSON result files for all configurations.
- 13 figures used in the paper.
- Reproduction scripts (`reproduce_all_tables.py`, `reproduce_table1b.py`,
  `reproduce_table7.py`, `stats.py`).
- `REPRODUCIBILITY_REPORT.md` with a full mapping from paper numbers to JSON keys.
- `CITATION.cff` and `LICENSE` (MIT).

### Known Issues
- CNN1 and CNN2 for rho != 0.9 are not included (see `REPRODUCIBILITY_REPORT.md`).
- The p-value for ERM vs Reweighting in Waterbirds may differ slightly
  depending on the t-test implementation (see `src/stats.py`).
- The "follow rate" column in Table 15 needs to be mapped to the exact
  JSON key (see `REPRODUCIBILITY_REPORT.md`).
