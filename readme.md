
# Today I Learned...

A collection of concise write-ups and code snippets on those small nuggets of information I'd otherwise forget.


So far, I have learned 11 things.

## Categories
- [Black](<#Black>)
- [Django](<#Django>)
- [Doh](<#Doh>)
- [Git and Github](<#Git-and-Github>)
- [Markdown](<#Markdown>)
- [Python built-ins](<#Python-built-ins>)
- [Python datatypes](<#Python-datatypes>)
- [Python standard library](<#Python-standard-library>)
----
### Black
- [Excluding directories](<./content/Black/exclude_directories.md>)

### Django
- [Setting up a new Django project](<./content/Django/django_new_proj_setup.md>)

### Doh
- [String comparisons - always consider case](<./content/Doh/string_search.md>)

### Git and Github
- [Git pull vs git fetch](<./content/Git and Github/git_pull_vs_fetch.md>)
- [Python-githooks](<./content/Git and Github/python-githooks_writeup.md>)

### Markdown
- [Internal links in Markdown docs](<./content/Markdown/internal_links.md>)

### Python built-ins
- [Divmod()](<./content/Python built-ins/divmod.md>)
- [Using zip() to combine iterables](<./content/Python built-ins/zip.md>)

### Python datatypes
- [Dictionary comprehension](<./content/Python datatypes/dict_comps.md>)
- [List Comprehensions to combine elements of multiple lists](<./content/Python datatypes/list_comp.md>)

### Python standard library
- [Getting the difference between two datetime objects](<./content/Python standard library/timedelta.md>)

## Usage
To create a new article:

1. Create a new .md file (and a new folder, if it's a new category).
1. The title of the new article will be the first level one heading in the file. Use '#', not 'H1'.
1. Once all new articles are have been staged in the local repo, commit the changes to git. Assuming `python-githooks` is installed and set up, this `readme.md` should be automatically regenerated (the test suite will also run, and Python files will be blackened). 
1. If edits are made directly in the GitHub editor **make sure to `git pull` the latest version** before committing any new articles to the repo locally. There's a test in the test suite to check that the local repo isn't behind the remote, so a commit should fail if there are remote changes not included locally.

## About
[Jim Anderson](https://github.com/jima80525) suggested that I build a "Today I Learned..." repo when I asked on the [Real Python](https://realpython.com/) Slack channel how people were storing their code snippets.
Jim's reward for this kindness was that I shamelessly copied [his own TIL](https://github.com/jima80525/til) (although I've added quite a lot of features since then). Thank you Jim, for the suggestion and inspiration!

## License
This repository is licensed under the MIT license. See `LICENSE` for details.
