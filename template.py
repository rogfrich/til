HEADER = """
# Today I Learned...

A collection of concise write-ups and code snippets on those small nuggets of information I'd otherwise forget.\n\n
"""

FOOTER = """
## Usage
To create a new article:\n
1. Create a new .md file (and a new folder, if it's a new category).
1. The title of the new article will be the first level one heading in the file. Use '#', not 'H1'.
1. When all new articles have been added, run `create_readme.py`.
1. If edits are made directly in the GitHub editor **make sure to `git pull` the latest version before running `create_readme.py`**.

## About
[Jim Anderson](https://github.com/jima80525) suggested that I build a "Today I Learned..." repo when I asked on the [Real Python](https://realpython.com/) Slack channel how people were storing their code snippets.
Jim's reward for this kindness was that I shamelessly copied [his own TIL](https://github.com/jima80525/til). Thank you Jim, for the suggestion and inspiration!

## License
This repository is licensed under the MIT license. See `LICENSE` for details.
"""