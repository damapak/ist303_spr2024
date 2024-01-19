---
marp: true
theme: gaia
#size: 4:3
#_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
---

# Introduction to Git and Github
![bg right:40% 90%](rsc/xkcd_git.png)

---

## Git Flow Simplified
![bg right:65% 90%](rsc/complicated_git.svg)

---
**What is Git?**
A version control system. A system for methodically tracking and managing changes to a codebase (repository). Can communicate changes made locally to remote code storage locations and vice versa.

**Where do you access Git?**  
_In the terminal_ . . . . . .![w:60](rsc/terminal.png)

**What is Github?**
A place to remotely store a codebase where you and others can access and manipulate it with Git.

---
## CAMP =

## REMOTE REPOSITORY (Github, Gitlab, Bitbucket, etc.)
![bg left:50% 90%](rsc/tent.jpg)

<style scoped>
{font-size: 22px;}
</style>

_*This is a special tent with one magical property: with the push of a button you can copy all the tent's contents into your backpack (`git clone`)_

---
<style scoped>
{font-size: 26px;}
</style>

## BACKPACK =

## LOCAL REPOSITORY (your computer files)
![bg right:40% 80%](rsc/hike_pack.jpg)

Your backpack consists of 3 parts:
- Existing contents (_working directory_)
- Notepad to track what you will add (_Index_) `git add`
- Original contents plus those you have tracked and then add (_Head_) `git commit`

---
<style scoped>
{font-size: 24px;}
</style>
##### While at camp, your team realizes you forgot some items and you need to go out and gather the following:

- Food
- Medicine
- Fire supplies (wood, kindling, striking rock)

You and 2 of your teammates push the magic button, creating identical copies of all tent contents in your packs. The 3 of you then head out in separate directions, with a 4th team member remaining at camp.

<==![w:100](rsc/hike_pack.jpg)---- ![w:100](rsc/hike_pack.jpg)-||--- ![w:100](rsc/hike_pack.jpg)==> 

![bg right:30%](rsc/tent.jpg)

---
You have been assigned to provide medicine for your team and embark on your expedition.
![h:260](rsc/med.jpg)
As you explore, you observe several potential medicinal plants. You pull out your notebook and begin to write down those you plan to harvest (`git add`)
-- ![h:100](rsc/notebook.jpg)---

---
<style scoped>
{font-size: 32px;}
</style>
Having noted a number of plants, you now go back and harvest them. You try some of them on a red irritated area of your skin, and it relieves the itching. You are confident what you have collected will fit the needs of camp and *you place them in your backpack* (`git commit`) ![h:70](rsc/hike_pack.jpg)

You head back towards camp, and remember that while the mesquite tree has medicinal uses, the pods are also edible. You want to check back with camp to see if anyone has brought back mesquite as a food source. You radio camp and find out that there have been no changes to the tent's supplies (`git fetch`)

---
<style scoped>
{font-size: 32px;}
</style>
You hasten back towards camp and deliver all of the new medicinal capabilities stored in your backpack to your camp (`git push`) ![bg right:20%](rsc/tent.jpg)

Shortly after, the other team members also radio back to camp (`git fetch`) and see what you have delivered. 

They wish to have the contents you have added to the tent in their backpacks too, and they radio camp to have drones deliver copies of these new items so that their packs are up-to-date with camp (`git pull`)

---
![h:575](rsc/git_smry.jpg)

---
<style scoped>
{font-size: 30px;}
</style>

### Local Only:
- _`add`: instruct Git to locally track changes to a file (or files)_
- _`commit`: prepare local changes ("stage") to be sent to a remote repo_
### Local ---> Remote
- _`push`: send changes from local repo to remote repo (github)_
### Remote ---> Local:
- _`pull`: copy new changes from a remote repo (github) to your local repo. Equivalent to fetch + merge._
- _`clone`: copy all contents of a remote repo_

---
Another way to visualize it:
![w:700](rsc/gitflow.png) 

---

[installation and setup](week02_02_src.md)



