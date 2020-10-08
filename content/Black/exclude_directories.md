# Excluding directories
Black [sometimes attempts](https://github.com/psf/black/issues/603) to format all the Python modules in the `/venv` virtual environment directory. This takes a long time and is unnecessary.

Use `black . --exclude venv/` to avoid this from happening.