# Introduction to get the environment running on your computer and some basic git/github

First install Python 3.11.6 from https://www.python.org/downloads/release/python-3116/ After that, restart your device

1. Get the remote repository (main branch on github) onto your local repository (your own computer), using the command
   'git clone https://github.com/DaniBoi2/DCM.git'.
   You now have a local repository. Now in any IDE/Text editor, from the terminal, go to the directory of your cloned repository
   and follow the rest of the instructions

2. Next create a virtual environment (ve) by using the command, 'python -m venv myenv' in the project directory, where myenv is the name
   of the virtual environment. Then activate the virtual environment using 'myenv/scripts/activate', once you have activated a venv, run
   'pip install -r requirements.txt', this installs all the packages within the myenv folder.
   Note: requirements.txt is empty for now since I have not added any external packages
   IMPORTANT: if your ve is named 'myenv', not to worry as I already added it to gitignore but if it is named something else like 'dan_env', then add it to the gitignore so git ignores that folder, you don't want git to track 1000's of potential files and certainly not push it onto github.

3. To switch to a new branch, do 'git checkout -b branch-name', this will create a copy of the 'main' branch and you
   are automatically switched to this new 'branch-name'. You can confirm this my running the command, 'git branch -a'.
   If there is a '\*' next to the 'branch-name' that is where you currently are. Note that your newly created branch is local only
   , you have not pushed it to github, next steps allow that. use a meaningful branch name, like if you are working on a registeration
   feature, name it 'registeration'.

4. Once you are on a new branch, add files, write code etc. Once you add a working feature, use the following commands

   a) 'git add <file1> <file2>', where file1 and file2 are the newly added files or they could be existing files that got modified.

   b) next use 'git commit -m "some message regarding changes"' to take a snapshot of the changes you want.

   c) use 'git push origin branch-name' which will push the local branch onto the remote branch

   d) once done, then submit a pull request on github, stating that you want to merge 'branch-name' into 'main' in otherwords updating
   the 'main' branch with the changes you made on 'branch-name'.

   e) Github will see if there are any conflicts, if there aren't any, you are free to complete the merge. Then get delete your old
   branch (option on github), and create a new branch for you next feature

This should setup your repository locally and give you an idea on how to use git/github

## What to do everytime after the above steps

Next time you want to make changes/add new code etc. Always follow these steps

1. Create a new branch and switch to it.
2. do a 'git pull origin main' this takes the main repository in github and merges it into your local repository (in other words
   it updates your branch with the latest changes in the main repository)
3. once you make your changes/code do the steps
   a) git add filename.py
   b) git commit -m "fixed bug"
   c) git push origin your-branch-name
   d) make a PR (pull request) which means that you want to merge your branch into the main one (you can do this in github)
   e) Once your merge request is approved, and merged by me, delete the branch (you can do this in github)
4. repeat the steps 1-3 everytime

## Resources

Git and Github
https://education.github.com/git-cheat-sheet-education.pdf

Tkinter
https://www.youtube.com/watch?v=ibf5cx221hk
