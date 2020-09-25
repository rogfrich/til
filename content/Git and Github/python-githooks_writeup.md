# Python-githooks

A [Python package](https://github.com/ygpedroso/python-githooks) that allows easy running of pre-commit hooks.A

## Usage:

Create a .githooks.ini file. This is the one for this repo:

```
[pre-commit]
command = pytest && python create_readme.py && black . --exclude venv/
```

Run the `githooks` command from the terminal every time the .githooks.ini file changes.