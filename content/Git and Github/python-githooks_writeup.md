# Python-githooks

A [Python package](https://github.com/ygpedroso/python-githooks) that allows easy running of pre-commit hooks.A

## Usage:

Create a .githooks.ini file. This is the one for this repo:

```
[pre-commit]
command = pytest && black . --exclude venv/ && python create_readme.py && git add readme.md

[post-commit]
command = git push
```
If the `git commit` is successful (and there are changes to commit) then `git push` run automatically, making this a single 
operation to run the tests, run the Python script, commit the updated files and push it all to GitHub.


Run the `githooks` command from the terminal every time the .githooks.ini file changes.