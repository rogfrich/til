# Git pull vs git fetch

`git fetch` downloads changes form the remote repo, but doesn't merge them. Once you're happy with the changes, and you want to incorporate them into your local repo, you 
need to `git merge`.

`git pull` does both of these steps in one: it fetches the changes form the remote and merges them into the repo in one move.
