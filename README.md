# Machu Picchu Game
An adventure based game created as part of a project submission to Code Institute for the Diploma in Full Stack Software Development
(E-commerce Applications). The criteria for the submission were primarily that it be created using the Python coding language.  

The application can be viewed on the Code Institute mock terminal on [Heroku](https://decant09-machu-picchu-game.herokuapp.com/).

## Contents
- [User Experience](#user-experience)
    - [Initial Discussion](#initial-discussion)
    - [User Stories](#user-stories)
        - [First Time Visitor Goals](#first-time-visitor-goals)
        - [Returning Visitor Goals](#returning-visitor-goals)
        - [Frequent Visitor Goals](#frequent-visitor-goals)
    - [Design](#design)
        - [Mind Map](#mind-map)
- [Features](#features)
- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks](#frameworks)
- [Testing](#testing)
    - [PEP8 Python Validator](#pep8-python-validator)
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
The idea of an adventure based game appealed to me as I have fond memories of playing them. The story content was loosely based on an
experience I had with some friends travelling through South America.
### User Stories
#### First Time Visitor Goals
- I want to know what the application is about on first viewing.
- I want clear descriptions as to what my input options are at each point in the game.
- I want to know if I have entered the wrong value in the input area.
- I want to tailor the game to include my name.
- I want the text to be laid out in such a way that improves readability.
- I want to know if the game has ended and if I have won or lost.
- At the puzzle point of the game, I want to know what guesses I have made so far and how many attempts I have left.
- I want to be able to quit the game at any point. 
#### Returning Visitor Goals
- I want an option to be able to play the game again when I reach the end.
- I want variety in the game so that there are different outcomes based on choosing different options.
#### Frequent Visitor Goals
- I want variety in the puzzle games that are presented (future implementation).
### Design
The appearance of the game is simple. The default black background and white text appearance are used. I used appropriate spacing
in the text to improve readability as the game progresses. Simple ASCII artwork is used for the banner at the beginning of the game,
above the introduction. Artwork is also used for the win and lose screens. The terminal is cleared at each junction of the game to
improve the experience for the user.  
#### Mind Map
To better understand the flow of the game I created a mind map. This shows the direction each level of the game takes upon the user
choosing the available option at each step along the way.  
![](/docs/mind_map/mind_map.jpg)
#### ASCII Art
The art style chosen is called "pyramid". It was chosen as it mimics peaks which draws from the fact that the game is about hiking to
the summit of Machu Picchu. 
- Game banner
![](/docs/screenshots/ascii_art/game_banner_art.png)
- You win  
![](/docs/screenshots/ascii_art/game_over_win_art.png)
- You lose  
![](/docs/screenshots/ascii_art/game_over_lose_art.png)
## Features
- The game is first viewed with a game title art banner at the top of the terminal. The words of the game title, "Machu Picchu",
are embedded in the art. Below this, there is an introduction which briefly describes the game. This is followed by an opportunity for
the user to input their name.  
![](/docs/screenshots/intro.png)  
- The name entered must not have any spaces, be at least three characters long, and only contain letters. The user is shown an error
message if the name entered does not match this criteria. The message details what the requirements are and asks the user to enter
their name again if the entry is not valid.  
![](/docs/screenshots/username_input_error.png)  
- When the criteria for the name have been met, the name is  then capitalized and stored for use during the game. The terminal is then
cleared and the next area of the game is revealed where you are introduced to Miguel your tour guide. Here you are given the option of
continuing, with yes or no options presented. Inputting a valid option clears the terminal to display the next part of the game.  
![](/docs/screenshots/miguel.png)  
- No ("N") quits the game and a message is shown to the user to confirm this.  
![](/docs/screenshots/miguel_no.png)  
- Yes ("Y") advances the user to the next area of the game where they are asked if they would like to complete the hike in 3 or 5 days.
To progress the user should input "3" or "5". The user can also input "Q" to quit the game.  
![](/docs/screenshots/miguel_yes.png)  
- As the user then progresses through the different scenarios of the game they are presented with yes, no or quit options.  
![](/docs/screenshots/yes_no_quit.png)  
- If the user inputs an invalid value, they are informed of this and prompted to input a valid value. Both upper and lower case values
are accepted.  
![](/docs/screenshots/invalid_entry.png)  
- If the user navigates the game successfully they arrive at a puzzle section where they also receive a clue.  
![](/docs/screenshots/puzzle.png)  
- They must enter a password to open a door. They get 5 attempts to enter the correct password. The password entered must be exactly
5 characters long, can only contain letters, and not be a previous guess. If they enter an invalid value they are notified and
prompted to enter a valid value. They can also quit the game by entering "Q".  
![](/docs/screenshots/puzzle_invalid.png)  
- Incorrect guesses are stored and displayed to the user so that they know what passwords they have already attempted. The number of
attempts remaining is also displayed.  
![](/docs/screenshots/puzzle_attempts.png)  
- Once the correct password is entered the door opens and the user wins the game. A "you win" message is displayed.  
![](/docs/screenshots/you_win.png)  
- The user can lose the game at different points along the way by choosing an incorrect option or by entering the password incorrectly
5 times. They are then shown a "you lose" message.  
![](/docs/screenshots/you_lose.png)  
- At both the win and lose points the user is given the option of playing again or not. Opting to play again takes the user back to
the start of the game. Opting to not play again quits the game.  
##  Technologies Used
### Languages
- Python
### Frameworks
- Git
    - Used for version control by utilising the Codeanywhere terminal to commit to Git and push to GitHub.
- GitHub
    - Used to store the code of the project after being pushed from Git.
- Heroku
    - Used to deploy the application.
- [PEP8](https://pep8ci.herokuapp.com/)
    - Used to test the code for errors.
- Miro
    - Used to create the mind map.
- ASCII
    - Used patorjk.com, a website-based text to ASCII art generator, for the ASCII art.
## Testing
### PEP8 Python Validator
#### Python
- Result
    - All clear, no errors found  
    ![](/docs/testing/pep8.png)  
### Manual
- All input fields were tested and behave as intended.
    - The appropriate error message is displayed when an invalid entry is made.
    - The value input into the name field is capitalized and spaces are removed. This is stored and displayed correctly when used
    throughout the game.
    - The options that are available to the user, when input into the respective fields, take the user to the point that is intended
    by the game. Capitalized input is accepted and converted to lowercase as intended.
    - Valid puzzle guesses are stored and if incorrect are displayed to the user before they guess again. The attempts remaining value
    reduces by 1 each time an incorrect guess is made and this value is then displayed to the user correctly.
- I spellchecked the application and the readme using [Online Spellcheck](https://www.online-spellcheck.com/). I also used
[Webpage Spell-Check](https://chrome.google.com/webstore/detail/webpage-spell-check/mgdhaoimpabdhmacaclbbjddhngchjik),
a google chrome extension.
- I used [Grammarly](https://www.grammarly.com/) to check for grammatical errors.
### Testing User Stories from User Experience (UX) Section
#### First Time Visitor Goals
- I want to know what the application is about on first viewing.
    - On the main landing screen, there is a short introduction to what the application is, a game based on hiking to Machu Picchu.  
    ![](/docs/screenshots/intro_text.png)  
- I want clear descriptions as to what my input options are at each point in the game.
    - At each point in the game where there is an opportunity to input a value, there is a description as to what the options are.  
    ![](/docs/screenshots/options_1.png)  
    ![](/docs/screenshots/options_2.png)  
    ![](/docs/screenshots/options_3.png)  
    ![](/docs/screenshots/options_4.png)  
    ![](/docs/screenshots/options_5.png)  
- I want to know if I have entered the wrong value in the input area.
    - If an invalid value is input by the user, a message appears explaining what values are accepted as valid. This occurs at each
    point that there is an opportunity to input a value.  
    ![](/docs/screenshots/invalid_entry_msg_1.png)  
    ![](/docs/screenshots/invalid_entry_msg_2.png)  
    ![](/docs/screenshots/invalid_entry_msg_3.png)  
- I want to tailor the game to include my name.
    - There is an opportunity at the beginning of the game to enter your name.  
    ![](/docs/screenshots/name.png)  
    - This is stored and used at various points along the game to personalise the game experience.  
    ![](/docs/screenshots/name_personalised.png)  
- I want the text to be laid out in such a way that improves readability.
    - The screen is cleared at frequent points in the game. There is sufficient spacing between lines of text and messages that appear
    throughout the game as seen in the screenshots provided elsewhere within this section.
- I want to know if the game has ended and if I have won or lost.
    - You are shown the art displaying "you win" or "you lose" with a short message underneath it.  
    ![](/docs/screenshots/you_win_msg.png)  
    ![](/docs/screenshots/you_lose_msg.png)  
- At the puzzle point of the game, I want to know what guesses I have made so far and how many attempts I have left.
    - Each time you input a valid guess which is not correct it is stored and the guesses you have made so far are displayed to you
    before you attempt to guess again. The number of attempts left is also displayed.  
    ![](/docs/screenshots/puzzle_attempts_log.png)
- I want to be able to quit the game at any point.
    - At each opportunity to input a value, you are given the option of entering "Q" to quit the game (with the exception of the name
    input). This can be seen in the screenshots provided elsewhere within this section.
#### Returning Visitor Goals
- I want an option to be able to play the game again when I reach the end.
    - There is an option to play again when the user reaches the end of the game.  
    ![](/docs/screenshots/options_5.png)  
- I want variety in the game so that there are different outcomes based on choosing different options.
    - Each time a user is presented with a question in the game, the answer chosen by the user results in a different outcome.
#### Frequent Visitor Goals
- I want variety in the puzzle games that are presented (future implementation).
    - This is a future implementation whereby I would like to add a little more complexity to the game. I would add more puzzles,
    which would aim to encourage the user to visit the application frequently.  
### Bugs
#### Known
- No known bugs.
#### Solved
- When constructing the main() method I was having issues with methods within it being doubly called. This was because I was assigning
the return value of a method to a variable. I would then call that method. I realised that assigning the return value from a method to
a variable was in fact also calling that method. I removed the second call and this resolved the issue.
- After running the code through the PEP8 validator I rearranged the code to meet the 80 character limit requirements. This involved
rearranging an f-string by splitting it over two lines and using a "+" at the end of the first line. However, that caused "{username}"
to be displayed when the game was run and not the input value for username. This was because "{username}" was now on the newly
rearranged second line and not the first line which contained the "f". I moved the "f" from the first to the second line containing
"{username}" and this resolved the issue.
## Deployment & Local Development
### Deployment
The site was deployed to Heroku and the following steps were followed to do so:
1. Log in to heroku.com, click "New" and then “Create new app”.
2. Give the application a name, choose your region, and Click "Create app".
3. On the next page, within the "Settings" tab, click on the “Reveal Config Vars” button. In the "KEY" input box type PORT and the
"VALUE" input box type 8000. Then click on the "Add" button.
4. Next, click on the “Add buildpack” button. Select “python” and click “Save changes”. Repeat this process to add “nodejs”. It is
important to add them in this order, with Python on top and NodeJS underneath. If they are the other way around you can click and drag
to change the order.
6. When this step is complete select the “Deploy” tab at the top of the page.
7. In the deployment method section, you can connect with GitHub by selecting “GitHub”.
8. In the "connect to GitHub" section type the [repository](https://github.com/decant09/machu-picchu-game) name in, click “Search”,
and once located click “Connect”.
9. You can choose to deploy using either the automatic or manual option.
10. For automatic deploys select “main” for the “Choose a branch to deploy” option. Click “Enable Automatic Deploys” if desired. This
can be changed at a later date if needed.
11. To manually deploy select “main” for the “Choose a branch to deploy” option. Click “Deploy Branch”. A message appears saying
“Your app was successfully deployed” and a “View” button can be clicked to view the application on a new page.

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
5. Within this tab, there are "HTTPS", "SSH", or "GitHub CLI" tabs.
6. Click on the "HTTPS" tab and copy the link shown.
7. In your development environment open the terminal.
8. Change the current working directory to the location where you want the cloned directory to be.
9. Type "git clone" into the terminal, then paste the URL you copied in step 6.
10. Press **Enter** to create your local clone.

## Credits
### Code Used
- The code to clear the terminal was obtained from
[stackoverflow](https://stackoverflow.com/questions/2084508/clear-terminal-in-python).
- The ASCII art code used was generated on
[patorjk.com](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20).
### Resources
- To get an overview of how to code a Python text-based adventure game referred to the following tutorials:
    - Starting to code a Python Text Adventure Game on YouTube by
    [Jekyll&HydeTutorials](https://www.youtube.com/watch?v=pEfBKamHJew&t=1287s).
    - Writing a Text-Based Adventure Game in Python on YouTube by
    [Doug McNally](https://www.youtube.com/watch?v=miuHrP2O7Jw&t=1565s).
- For help on how to end a program in Python with a built-in quit() method referred to
[CodeBerry](https://codeberryschool.com/blog/en/how-to-end-a-program-in-python/).
- For error handling referred to Corey Schafer's tutorial on [YouTube](https://www.youtube.com/watch?v=NIWwJbo-9_8&t=72s):
    - Python Tutorial: Using Try/Except Blocks for Error Handling.
- For help with the puzzle method referred to
[stackoverflow](https://stackoverflow.com/questions/65054394/guessing-game-with-5-chances-in-python) and
[GeeksforGeeks](https://www.geeksforgeeks.org/python-program-for-word-guessing-game/).
- For help printing a list without brackets referred to
[javatpoint](https://www.javatpoint.com/how-to-print-a-list-without-brackets-in-python).
- For help with Python while loops referred to [Tools QA](https://www.toolsqa.com/python/python-while-loop/).
### Acknowledgements
- My Mentor Chris Quinn for continuous helpful feedback.
- Tutor support at Code Institute for their amazing support.
- Alan Bushell at Code Institute for guiding the class in our weekly stand-ups.