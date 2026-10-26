# Contributing

Thank you for your interest in this repository.

## Reporting Issues

If you find a bug or a discrepancy between the paper and the code, please
open an issue on GitHub with the following information:

1. The table or figure where the discrepancy occurs.
2. The expected value (from the paper).
3. The actual value (from the JSON file).
4. The command you ran to reproduce the value.

## Submitting Changes

If you want to submit a fix:

1. Fork the repository.
2. Create a new branch (`git checkout -b fix/description`).
3. Make your changes.
4. Test the reproduction scripts (`python src/reproduce_all_tables.py`).
5. Submit a pull request with a clear description of the change.

## Code Style

- Follow PEP 8 for Python code.
- Use descriptive variable names.
- Add docstrings to all public functions.
- Keep functions focused on a single task.

## Data and Models

- Do not commit large files (models, raw data) to the repository.
- Use GitHub Releases for model weights.
- Use `.gitignore` to exclude local data directories.
