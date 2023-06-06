# Machu Picchu Game
An adventure based game created for a project submission to Code Institute for the Diploma in Full Stack Software Development
(E-commerce Applications). The criteria for the submission were primarily that it be created using the Python coding language.

## Contents
- [User Experience](#user-experience)
    - [Initial Discussion](#initial-discussion)
    - [User Stories](#user-stories)
        - [First Time Visitor Goals](#first-time-visitor-goals)
        - [Returning Visitor Goals](#returning-visitor-goals)
        - [Frequent Visitor Goals](#frequent-visitor-goals)
    - [Design](#design)
        - [Mind Map](#mind-map)
        - [Wireframes](#wireframes)
- [Features](#features)
- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks](#frameworks)
- [Testing](#testing)
    - [PEP8 Linter](#pep8-linter)
        - [Python](#python)
    - [Manual](#manual)
    - [Testing User Stories from User Experience (UX) Section](#testing-user-stories-from-user-experience-ux-section)
        - [First Time Visitor Goals](#first-time-visitor-goals-1)
        - [Returning Visitor Goals](#returning-visitor-goals-1)
        - [Frequent Visitor Goals](#frequent-visitor-goals-1)
    - [Bugs](#bugs)
        - [Known](#known)
        - [Solved](#solved)
- [Deployment & Local Development](#deployment--local-development)
    - [Deployment](#deployment)
    - [Local Development](#local-development)
        - [How to Fork](#how-to-fork)
        - [How to Clone](#how-to-clone)
- [Credits](#credits)
    - [Code Used](#code-used)
    - [Resources](#resources)
    - [Acknowledgements](#acknowledgements)
## User Experience

### Initial Discussion
### User Stories
#### First Time Visitor Goals
#### Returning Visitor Goals
#### Frequent Visitor Goals
### Design
### Mind Map
This is the mind map.  
![](/docs/mind_map/mind_map.jpg)  

#### Wireframes


## Features


##  Technologies Used
### Languages
- Python
### Frameworks
- Git
    - Used for version control by utilising the Codeanywhere terminal to commit to Git and push to GitHub.
- GitHub
    - Used to store the code of the project after being pushed from Git.
- Heroku
    - Used to deploy the appliaction.
- [PEP8](https://pep8ci.herokuapp.com/) used to test the code for errors.
## Testing
### PEP8 Linter  
#### Python
- Result
    - All clear, no errors found  
    ![](/docs/testing/pep8_linter.png)
### Manual
- I spellchecked the website and the readme using [Online Spellcheck](https://www.online-spellcheck.com/). I also used
[Webpage Spell-Check](https://chrome.google.com/webstore/detail/webpage-spell-check/mgdhaoimpabdhmacaclbbjddhngchjik), a google chrome extension.
- I used [Grammarly](https://www.grammarly.com/) to check for grammatical errors.

### Testing User Stories from User Experience (UX) Section
#### First Time Visitor Goals
 
#### Returning Visitor Goals
  
#### Frequent Visitor Goals

### Bugs
#### Known
#### Solved
- When the user opted to play the game again, the introduction text would load but the game wouldn't run as expected. This is
because the username varaible is not an empty string anymore once the game is played once. To address this I introduced a pass
statement to the intro() method. This allows the program to pass on to the miguel() method of the game if the username variable
is not an empty string.
- After running the code through the PEP8 linter I rearranged the code to meet the 80 character limit requirements. This involved
rearranging an f-string by splitting it over two lines and using a '+' at the end of the first line. However that caused '{username}'
to be displayed when the game was run and not the input value for username. This was because '{username}' was now on the new
rearranged second line and not the first line which contained the 'f'. I moved the 'f' from the first to the second line containing
'{username}' and this resolved the issue.
## Deployment & Local Development
### Deployment
The site was deployed to Heroku and the following steps were followed to do so:
1. Log in to heroku.com, click "New" and then “Create new app”.
2. Give the application a name, choose your region, and Click "Create app".
3. On the next page, within the "Settings" tab, click on the “Reveal Config Vars” button. In the "KEY" input box type PORT and in the "VALUE" input box type 8000. Then click on the "Add" button.
4. Next click on the “Add buildpack” button. Select “python” and click “Save changes”. Repeat this process to add “nodejs”. It is
important to add them in this order, with Python on top and NodeJS underneath. If they are the other way around you can click and drag
to change the order.
6. When this step is complete select the “Deploy” tab at the top of the page.
7. In the deployment method section you can connect with GitHub by selecting “GitHub”.
8. In the "connect to GitHub" section type the [repository](https://github.com/decant09/machu-picchu-game) name in, click “Search”,
and once located click “Connect”.
9. You can choose to deploy using either the automatic or manual option.
10. For automatic deploys select “main” for the “Choose a branch to deploy” option. Click “Enable Automatic Deploys” if desired. This
can be changed at a later date if needed.
11. To manually deploy select “main” for the “Choose a branch to deploy” option. Click “Deploy Branch”. A message appears saying
“Your app was successfully deployed” and a “View” button which can be clicked to view the application in a new page.

### Local Development
The steps below describe how to fork or clone the repository if desired.
#### How to Fork
1. Log in to GitHub.
2. Navigate to the [repository](https://github.com/decant09/machu-picchu-game) for this website.
3. Click the "Fork" button in the top right corner.
4. You will be brought to a new page with a short form to be completed.
5. Upon completing, click on the "Create fork" button and this will create a fork of the repository in your personal account.

#### How to Clone
1. Log in to GitHub.
2. Navigate to the [repository](https://github.com/decant09/machu-picchu-game) for this website.
3. Click on the "Code" button and a modal will appear.
4. Within this modal select the "local" tab.
5. Within this tab there are "HTTPS", "SSH", or "GitHub CLI" tabs.
6. Click on the "HTTPS" tab and copy the link shown.
7. In your development environment open the terminal.
8. Change the current working directory to the location where you want the cloned directory to be.
9. Type "git clone" into the terminal, then paste the URL you copied in step 6.
10. Press **Enter** to create your local clone.

## Credits
### Code Used
- The code to clear the terminal was obtained from
[stackoverflow](https://stackoverflow.com/questions/2084508/clear-terminal-in-python).
### Resources
- To get an overview of how to code a python text-based adventure game referred to the following tutorials:
    - Starting to code a Python Text Adventure Game on YouTube by
    [Jekyll&HydeTutorials](https://www.youtube.com/watch?v=pEfBKamHJew&t=1287s).
    - Writing a Text-Based Adventure Game in Python on YouTube by
    [Doug McNally](https://www.youtube.com/watch?v=miuHrP2O7Jw&t=1565s).
- For help on how to end a program in Python with built in quit() method referred to
[CodeBerry](https://codeberryschool.com/blog/en/how-to-end-a-program-in-python/).
- For error handling referred to Corey Schafer's tutorial on [YouTube](https://www.youtube.com/watch?v=NIWwJbo-9_8&t=72s):
    - Python Tutorial: Using Try/Except Blocks for Error Handling.
- For help with puzzle function referred to
[stackoverflow](https://stackoverflow.com/questions/65054394/guessing-game-with-5-chances-in-python) and
[GeeksforGeeks](https://www.geeksforgeeks.org/python-program-for-word-guessing-game/).
- For help printing a list without brackets referred to
[javatpoint](https://www.javatpoint.com/how-to-print-a-list-without-brackets-in-python).
- For help with python while loops referred to [Tools QA](https://www.toolsqa.com/python/python-while-loop/).
### Acknowledgements
- My Mentor Chris Quinn for continuous helpful feedback.
- Tutor support at Code Institute for their amazing support.
- Alan Bushell at Code Institute for guiding the class in our weekly stand-ups.