# Module 1 — Git & GitHub

**Student:** Tamsi, Luis Miguel
**Date:** September 26, 2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

git is version control it tracks all your changes in your folder or files. Think of it like using google docs for your school project, the tradtional word documents does not track your changes. It saves line by line what you added, changes and deleted, who change it and why. if you accidentally delete portion of your document while also not being being aware that you deleted it, you dont have way to undo or revert from the past changes and need to redo it all again. Github, on the otherhand is where you save all your files romotely. Github is like Google Drive, you put your project or documents there online, that means you can access it anywhere you want. It also allows you to share with other people without having giving them the physical document.  
---

## Key vocabulary (in your own words)

- repository: Folder you want to track the changes
- commit: a checkpoint or snapshot of your changes with message at specific point of time
- branch: its a copy of your project on a safe and isolated workspace, where you can build or test your project without worrying that it might break your main branch
- push / pull: Push is uplaoding your local change into remote repository like GitGub. Pull is downloading the latest change in your remote repo (Github) down to your local computer so you're up to date
- pull request: Is way of asking someone to review, give feedback or approve your changes before merging to the main branch
- merge conflict: its an error that occuring then two people edi the same file or line of code, making you manually choose what version you want to keep before saving

---

## Walking through what I did

- Create and switch to new branch: Created new branch AboutMe 
- Add changes and put them into staging stage: I added new files, edited them for about me feature, then after editing i prepare every file to be commited.
- commit all the changes, i save all my changes and add a descriptive message on what i did
- pushed the branch to github, i uplaod my local change to github
- go to github and create a pull request to review all my changes and merge to main
  
```
git switch -c AboutMe

git add .

git commit -m "Create aboutme page"

git push -u origin AboutMe

```

---

## A mistake I made (or one I want to avoid)

[What tripped you up? A confusing error message, committing to the wrong branch, a merge conflict — explain it so a classmate reading this avoids the same mistake.]

Commiting directly to main branch, its easy to edit files and forget to create your branch. at first i always commiting directly to main and hope for the best. how to avoid it, always check you branch using git branch, if you are in main branch create new branch using git switch -c <Branch name>

---

## How this connects to something else


[Optional: how does version control relate to anything else you've learned or used before?]
