# Git pull vs git fetch

`git fetch` downloads changes form the remote repo, but doesn't merge them. Once you're happy with the changes, and you want to incorporate them into your local repo, you 
need to `git merge`.

`git pull` does both of these steps in one: it fetches the changes form the remote and merges them into the repo in one move.

The tests in this repo test check that a local commit isn't going to overwrite remote changes by doing a `git fetch` and then a `git status`. If the words "branch is behind"
appear in the output from `git status` then the test fails (and local changes arn't committed, meaning that we won't overwrite the remote changes). It does the 
`git fetch` first to ensure that the we're comparing with the most recent version of the remote repo. 