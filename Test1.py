print("test")
print("this is only available from a second push")
"""
Basics of pushing something to github
Establish a local repository in the file that you're gonne push using
1. git init
2. git remote add "nickname for the remote repo" "url of the remote repo"
3. git branch -M main/branch name
These three create a git file, make sure its been previously navigated to the file we're using w commandline stuff
Then it establishes a connection between the local and remotes repos
Then it renames the branch to main or wtv we make it named
4. git add (file goes here)
5. git commit -m "commit message"
6. git push -u "nickname for remote repo" main/branch name
7. after you've used -u once you can just use git push

* can use git status to check situation for repo status
"""