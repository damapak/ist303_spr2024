# Week 2

## Github
- create [github](https://github.com) account
- create a test repository
- find repository url for use in git (green clone/code button)
- find email address for use in pushing to remote repo (user settings -> email)

## Git
- Install: \
[github guide](https://github.com/git-guides/install-git) or \
[git-scm guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Explore: \
[Git cheatsheet](https://www.git-tower.com/blog/git-cheat-sheet/) \
[Git guide @ github.com](https://github.com/git-guides) \
[Simple guide](https://rogerdudler.github.io/git-guide/) 
- <details><summary> OPTIONAL Powershell Integration for windows friends</summary>

  - POSH-GIT: PowerShell module that integrates Git and PowerShell by providing Git status summary information that can be displayed in the PowerShell prompt
  - check that powershell version is 5.0+: `$PSVersionTable.PSVersion`
  - check script execution policy: `Get-ExecutionPolicy`
  - if not Unrestricted or RemoteSigned, set to RemoteSigned: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Confirm`
  - Install: `PowerShellGet\Install-Module posh-git -Scope CurrentUser`
  - Import: `Import-Module posh-git`
  - Add to all hosts (to avoid having to import module each time):`Add-PoshGitToProfile -AllHosts`
  - [Read more here](https://papercutsoftware.github.io/git-from-powershell/#:~:text=Installing%20and%20configuring%20Git%20on%20Windows,-Personally%20I%20prefer&text=Can%20also%20use%20PowerShell%20Module,present%20the%20standard%20CLI%20experience)

  </details>

#### Test out your Git install in the Terminal:
  ```
  git --version
  mkdir test_dir
  cd test_dir
  git init
  git status
  ```
## Additional Configuration (Terminal)
- User name and email to appear on commits
- credential manager (login authentication)
- default branch name

### User name and email
Each commit includes not only the code changes, but also information about who made the commit. This sets up the name and email that will be used when your local machine makes changes (this is unrelated to your github username and email). 

You can set these _globally_, for all commits from your computer, or _locally_ for just a single project. To set globally, use the `--global` option.

#### user name (single repo, no `--global` option):
```
git config user.name "Leonardo"
```
#### email address (global example): 
```
git config --global user.email "myemail@hotmail.com"
```
#### Verify they are set:
```
git config user.name
git config user.email
```

_Note that you can use the noreply github email address structured as:_ \
  **githubUserName**@users.noreply.github.com


### Credential Manager
Used to authenticate communication between your local repository and remote repository (log in to Github from Git).
- Check if installed (can choose to install when you install Git): \
`git credential-manager --version`
- If not installed, can download (any OS) installers [here](https://github.com/git-ecosystem/git-credential-manager/releases/tag/v2.4.1)

### Set your default branch name
Github now uses the name "Main" for the initial branch name (used to be "Master").

It is cognitively a little easier if you set your local default branch name to "Main". Can set this using: \
`git config --global init.defaultBranch main`

## [Git test drive](week02_04_slide_firstCommit)

![power drift](http://forgifs.com/gallery/d/186158-5/Kid-power-wheels-drifting.gif)

## Flask
### What is [Flask](https://flask.palletsprojects.com/en/3.0.x/)? 
Flask is a basic web app framework. 

From wikipedia: \
_Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions._

Web framework
: software that provides a standard way to build & deploy web applications. Designed to assist with templating and boilerplate code that is then modified for use in a specific application. 

Third-party libraries
: software that is not a part of the codebase (here Flask) but that it utilizes and relies on for functionality (i.e. it must also be installed).

Database extraction layer
: functionality that standardizes communication between an application and databases

Resources
- [Pythonbasics.org intro to Flask](https://pythonbasics.org/what-is-flask-python/)

Flask Exercises
- Based off the following: \
[Flask Tutorial](https://flask.palletsprojects.com/en/2.3.x/tutorial/)
- Flask App Part 1: demo app
- Flask App part 2: login
- Flask App part 3: blog

#### Other web frameworks
- [Django](https://www.djangoproject.com/) (full-featured)
  - [ORM: object-relational mapper](https://docs.djangoproject.com/en/5.0/topics/db/models/)
- [Pyramid](https://trypyramid.com/) (MVC)
- [Falcon](https://falcon.readthedocs.io/en/stable/) (REST)
- [Tornado](https://www.tornadoweb.org/en/stable/) (non-blocking, async)
- [FastAPI](https://fastapi.tiangolo.com/) (async, API-based)

## Software Development
### [Pilone & Miles](week02_05_slide_PM1-4.md)


