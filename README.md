# demo_repo

Welcome. Practice clone, push, pulls, merges. Just go with it.

Getting started:

- Install Git Bash on your desktop.
- Clone the repo: "git clone https://github.com/sir-omoreno/demo_repo.git"
- Practice!



**USEFUL GIT COMMANDS:**

**Configure credentials to be used with your commits**

``
git config --global user.name "My Name"
git config --global user.email email-addy@email.com
``

**Create a new local repository**
`
git init
`

**Check out a repository	Create a working copy of a local repository:**	

` git clone /path/to/repository
`

**Add files to staging (index):**

``
git add <filename>
git add * 
``

**Commit changes (but not yet to the remote/master repository):**

``
git commit -m "commit message"	
git commit -a
``

**Push/send changes to the master branch of your remote repository:**

`
git push origin master
`

**List the files you've changed and those you still need to add or commit:**

`
git status
`

**Branches	Create a new branch and switch to it:**

`
git checkout -b <branchname>
`

**Switch from one branch to another:**

`
git checkout <branchname>
`

**List all the branches in your repo**

`
git branch
`

**Delete the feature branch:**	

`
git branch -d <branchname>
`

**Push the branch to your remote repository.**	

``
git push origin <branchname>
git push --all origin
``

**Update from the remote repository,	fetch and merge changes on the remote server to your working directory:**

`
git pull
`

**To merge a different branch into your active branch:**	

`
git merge <branchname>
`
