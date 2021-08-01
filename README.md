When installing pip I got the follow error-message:
WARNING: You are using pip version 21.1.3; however, version 21.2.1 is available.
You should consider upgrading via the '/home/gitpod/.pyenv/versions/3.8.11/bin/python3 -m pip install --upgrade pip' command.

This has not been installed yet




# Battleship

The idea behind this project is to create a single-player game of battleships where the player should be able to play solo against the computer on different difficulties, being able to upload results, and seeing other players' results.
The target group is anyone who enjoys a simple game that is a mix of chance and logic. The game requires a basic grasp of the rules and can be won either with pure luck, or more likely with a bit of strategy. However, the simple layout would be suited for people who are not interested in visual styling and only wants the pure game mechanics. The game has to be played in a terminal and can be played on modern browsers.

The aim of the game is to sink the ships with as few attempts as possible.

## Lucid Chart for overview of functionality

![Lucid Chart](/assets/readme-pictures/lucid-chart.png)

## Features

### Existing features:
* __Menu data validation__
    * Data input in all menus is validated through a function, and in case of fail it prints an error message:
        * In case of number wrong: "Invalid data: Choice not valid, input must be numbers within range", followed by input field "Press 'Enter' to continue"
        * In case of character input: "Invalid data: invalid literal for int() with base 10: 'CHARACTERS', input must be numbers within rang

![Menu data validation](/assets/assets/readme-pictures/menu-data-validation.png)

* __Main menu__
    * The main menu has four print statements that lists the options for the player, followed by an input field that reads: "Enter choice: ".
    * The player can choose between the following (screen is cleared for every choice):
        * Start game - this starts the game and redirects to set-difficulty screen
        * Rules - prints the objectives of the game and how to play
        * High score - redirects to high score lists
        * Exit game - exits the application
    * Data is validated through function


![Main menu](/assets/assets/readme-pictures/main-menu.png)

* __Rules__
    * Has 12 print statements that explain the rules and the objective, separated into three sections.
    * On top there is a heading "The rules of Battleship" followed by an empty line.
    * First section has five lines and explains the objective.
    * Second section has three lines and explains how to play.
    * Third section has three lines and explain the visual presentation and how to understand them, followed by empty line.
    * Below is an input field with the text "Press 'Enter' / any key to return to menu". Player can press enter, or any key + enter to return to main menu

![Rules](/assets/assets/readme-pictures/rules-page.png)

* __High Score__
    * Shows the player the different lists that are available, they are separated into difficulty. Each choice clears the screen.
    * Heading reads "Select a list to view", next is empty line.
    * Four print statements that lists options for the player
        * 1: One ship
        * 2: Two ships
        * 3: Three ships
        * 4: Return to main menu
    * Last is an input field with the text "Enter choice: ". 
    * Data is validated through function

![High score](/assets/assets/readme-pictures/high-score.png)

* __High score lists__
    * Each list has a similar appearance
    * Content is extracted from a Google Sheet and comes out as a list. List runs through function and is printed as desired:
        * At the top "Name" and "Missed Shots" are printed, separated by spaces to leave room for content below. Next line is empty.
        * Scores are sorted so the fewest misses are printed on top (best result), with the correct name to the left.
        * Names are followed by spacing calculated from the length of the name -> all scores will be printed on the same "column"
    * Below is an input field with the text "Press 'Enter' to return to menu". Player can press enter, or any key + enter to return to main menu.

![High Score lists](/assets/assets/readme-pictures/high-score-lists)

* __Set difficulty__
    * Shows the different difficulty levels the player can choose. Choice is passed through a function that generates ship of random length (2-4) and random vertical/horizontal and passes the coordinates into a list. When the correct number of ships is in the list it is passed on, and the actual game starts.
    * Heading reads "Set the difficulty", followed by empty line
    * Four print statements:
        * 1: One ship - passes 1 to generate ship function
        * 2: Two ships - passes 2 to generate ship function
        * 3: Three ships -passes 3 to generate ship function
        * 4: Return to menu - returns player to menu
    * Last is an input field with the text "Enter choice: ". 
    * Data is validated through function

![Set difficulty](/assets/assets/readme-pictures/set-difficulty.png)

* __Game screen__
    * Board is printed, which consists of eight lists printed out with a " " separating each item.
        * Top list represents the columns. First item is blank as this is simply an unused corner, which makes sure the following numbers 1-7, or columns, are directly over the "coordinates" below.
        * The next seven lists each start with an uppercase letter of the alphabet, which goes one up ("A", "B",..."G") for each list, followed by seven "-" which represents untouched coordinates.
    * Below is an empty line, followed by a teasing text: "I dare you to pick {random}{random}". The two variables generate a random coordinate that has little chance of being correct. Underneath comes is an empty line and then text which tells the player how many attempts there are left. The number is a variable and will decrease when incorrect guesses are made.
    * In the bottom is an input field "Guess a row and a number: (e.g., C5)"
    * Data is validated through a different function from the menus:
        * In case of wrong characters/order: "Error: invalid literal for int() with base 10: 's', must be letter and number within range" - new line - "Press any key to continue"
        * In case of letter/number out of range: "Error: out of bounds, must be letter and number within range" - new line - "Press any key to continue"
    * If data is validated then board and hit count/attempts are updated:
        * Board will use input-coordinates to find list and index.
            * If this point exists in ship list, then the index will be changed to "O", and then print "You hit the ship".
                * Hit count will add this coordinate to its list.
            * If the point doesn't exist the index will change to "X", and then print "You missed the ship"
                * Attempts variable will decrease by one
    * If attempts reach 0 the screen is cleared, and game over screen is printed.
    * If hit count list matches the ship list the screen is cleared and the game is won. Win screen is printed.

![Game Screen](/assets/assets/readme-pictures/game-screen-error.png)
![Game Screen](/assets/assets/readme-pictures/game-screen-miss.png)
![Game Screen](/assets/assets/readme-pictures/game-screen-start.png)

* __Game over screen__
    * A simple message of "Game Over" is printed, followed by an empty line
    * Below two choices are printed:
        * 1: Return to the main menu - clears screen and returns to the main menu
        * 2: Exit - exits the application
    * In the bottom is an input field "Enter Choice: "
    * Data is validated through function

![Game over screen](/assets/assets/readme-pictures/game-over.png)
    
* __Win screen__
    * A congratulatory message is printed "Congratulations! You sank all the battleships", followed by empty line.
    * Three choices are printed:
        * 1: Register your score - redirects to register score
        * 2: Return to main menu - returns player to main menu with no records of score
        * 3: Exit game - exits application
    * Data is validated through function
    * Screen is cleared after every choice

![Win screen](/assets/assets/readme-pictures/win-screen.png)

* __Register score__
    * Input field is printed "Enter your name: (Max 10 letters)"
    * Data is validated, but only for length     

![Register score](/assets/assets/readme-pictures/enter-name.png)

* __Updating high score__
    * Screen is cleared and then it prints "Updating highscore list...". Once it the scores have been added it prints "List updated successfully".
    * It prints options for the player:
        * 1: Return to main menu - returns to the main menu
        * 2: Exit - Exits the application
    * In the bottom is an input field "Enter choice: "
    * Data is validated through function

![Updating high score](/assets/assets/readme-pictures/high-score-updated.png)


### Future features to implement
* Add multiplayer option
* Multiplayer does not need to be live but can grab a random set of coordinates given by a player at any moment. Players will know result from lists (Add search function to find outcome)
* Possibility for the player to add ships to play against the computer
* Possibility for the player to select board size.

## Testing
* Gitpod workspace was used to test functionality for both game and API
* After deployment, Heroku deployment terminal was used to test functionality for both game and API
* Data validation was tested with a large number of different inputs. Letters, characters, lengths, reverse, capital, lowercase.

__Breakpoints__
There are not breakpoints set for this project


### Browser testing 
* Test on Firefox, Edge, Chrome, and Safari
* Tested on my own phone, Samsung Galaxy S9 using Chrome and Firefox, no issues.
* Media query tested on my own tablet, iPad pro 2018 11" using Safari and Chrome, no issues.
* General testing with my own laptop, Asus 13 inch using Chrome, no issues.

There are no links in this project.

### Bugs discovered during testing:
* I had a number of issues with creating ships as I was initially returning a dictionary with key: value pairs. The problem was that each key had to be different, so letters could not repeat, but they had to when it came to horizontal values, e.g. F2, F3, F4... Due to this, I chose to return a list instead.
    * In the beginning I wanted to return a list per ship, but I found it much easier to return a single list, which is really just a set of coordinates
* Clear screen issue: In my working environment on Gitpod I initially used the os.system('clear') command for clearing the terminal, thus giving a more visually pleasing transitioning. However, this didn't work on Heroku, and the next prints would simply be printed underneath with the 'old' text still visible. I tried different solutions with a function determining the operating system, and then calling the appropriate command:

One attempt:

    from os import system, name
    
    define our clear function
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    clear()

Another attempt:

    import os
    os.system('cls' if os.name == 'nt' else 'clear')c

However, it didn't work on the deployed version on Heroku, so instead I replaced the command with a print statement that prints 24 new lines: 
    print("\n"*24)
24 because of the 24 lines on the Heroku display

### Unfixed bugs
* Clear screen issue was resolved with an alternative solution, but I am still not happy with how the visuals work on Heroku when clearing screen.


### Validator testing:
* Python code passed linter PEP8 with no issues. Website: http://pep8online.com/

## Deployment
### Deployment to Heroku
The project was deployed to Heroku
The site was deployed to GitHub Pages, and goes as follows:

Before deploying: Every input code field should end with \n due to a quirk in the software used to create the mock terminal

* In Gitpod install Pip3 freeze > requirements.txt - this is to install dependencies (for this project: gspread and google-auth), will be listed in the requirements.txt
* Log in to Heroku and create new app
* Go to settings -> "Reveal Config Vars": here you should put sensitive data (for this project the json.creds file to connect to the API), as it is not synchonized with Github (in the gitignore file).
    * In "Key" put in name of file (CREDS), and in "VALUE" copy content of creds.json file. -> press "Add"
* Select "Add buildpack" below config vars -> click "Python" then save -> add again and select "nodejs" then save. (Python should be first)
* Go to deploy section -> Select "GitHub" -> confirm connection
* In the bottom search for your repository, use name in GitHub -> search and connect
* Below you can now deploy, either automatically or manually.
* Once done press "View" to open deployed project

The live link can be found here - https://battleship-project.herokuapp.com/


### Create a local clone
1.	Open GitHub and navigate to repository here (https://github.com/AndreasChristensen89/janken-bossu).
2.	Click the Code drop-down menu.
3.	Options:
•	Download the ZIP file, unpack locally and open with IDE.
•	Copy git URL from HTTPS dialogue box.
4.	Open your chosen IDE and open the terminal in a directory.
5.	Use the "git clone" command with the copied git URL after.
6.	Clone of the project is created locally on your machine.

## Technologies used
### Python extensions
I imported the following:
* from random import randint - randint was to generate random numbers when generating lists of coordinates
* from operator import itemgetter - itemgetter was used to sort the lists extracted from Google sheet in order to bring lowest values first.
* import gspread & from google.oauth2.service_account import Credentials - used for the API setup

### Hosting and Development
GitHub was used to host the repository, Gitpod was used for development and version control, and Heroku was used to deploy site.

## Setting up API
Battleship is connected to a Google Sheet. From here players can extract data, and after a win they are able to upload data to it.

### How to set up the API
IMPORTANT: Information below may not be relevant due to possible future updates from Google
* Create a Google Sheet with your personal Google account
* Go to Google Cloud Platform: https://console.cloud.google.com/
* Press "Create new project" -> give it a name -> create -> Select "Select project"
* Go to Libraries in APIs & Services -> Search for Google Drive -> Enable Google Drive
* Create credentials -> select Google Drive API -> Select "Application data" -> Select "No" to the question of whether you will use it with Computer Engine etc.
* Click "Next" -> Add any service name, and press "Create"
* In role select Basic -> Editor then continue
* Press "done" without filling in other options
* Click your Service Account -> keys -> add key -> select JSON and "create" -> file will download
* Back to libraries - search for Google Sheet -> enable
* Go to your repository -> add drop your downloaded file -> rename to creds.json
* In creds.json file copy the client_email without the "" -> in your Google Sheet select "Share", paste in the email, have editor selected, untick "Notify People" -> share
* Head to gitignore file in repository and add creds.json
* In the run.py file install 'pip3 install gspread google-auth'
* After install 'import gspread' in run.py and afterwards 'google.oauth2.service_account import Credentials'
* Insert following scope underneath:

    SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open('name-of-google-spreadsheet')

* From here we have access to the file and can access data like this:

    worksheet = SHEET.worksheet('name_of_worksheet')
    data = worksheet.get_all_values()

Link to Google sheet:
https://docs.google.com/spreadsheets/d/1VDhR8UUuAHAOBzgp_l9Ok1cZ5mcHgM7KnZ9ZBYMuL3M/edit?usp=sharing

## Credits:
### Pictures
Images for readme were obtained using Windows snipping tool, size lowered via https://tinypng.com/
Afterwards they were converted to webp using https://cloudconvert.com/png-to-webp.


### Text content
Content was all formulated by myself, as I have played the original battleship game many times in my life, I didn't need to look up the rules or get inspiration for formulating.

### Coding help
* For help with various challenges with Python I often resorted to the Material by Code Institute and https://stackoverflow.com/
* For help with syntax reminders I often used the material by Code Institute, as well as https://www.w3schools.com/ 
* For general best practice I used Code Institute's Slack community.

### Design
* For design of the different pages I didn't use other sources of information, but I did take inspiration from video games I have played throughout my life.
* Lucidchart was created using https://www.lucidchart.com/pages/

## User Stories:

### The User
* What are the goals for a first-time visitor?
   * Quickly understand that this is a game and how to start it
        * This is indicated by the "Start game" option, also "Enter Choice: " in the bottom tells the player what to do.
   * Quickly understand where to look
        * Background is black, and text is white. There are no other distractions.
   * Be able to navigate effortless through the pages
        * It is always clear what each command does, and there is always the possibility to return to the menu.
   * Easily reach the rules page and understand how to play the game
        * Navigation is easy, and the rules and objectives are explained right away.
   * Easily understand the goal of the game
        * Rules are written simple and separated into sections for easier readability.
   * Understand how to make the initial guess in the game
        * On the game screen there is input text which explains that the player should pick a letter and a number and gives an example of input.
   * Understand how to advance after a hit/miss
        * There is a counter for attempts, which is meant to signal that the game is still ongoing, and the player should therefore continue as before
    * Understand where to find high scores, and how they are measured
        * Navigation is clearly displayed, in the high score menu the heading says "Select a list/difficulty to view" which tells the players that high scores are separated by difficulty.
        * In the high score lists a top remark tells the players "The fewer misses the better", which aims to make the player understand the hierarchy of scores and explains why the lowest are on top.

* What are the goals for a returning visitor?
   * Instantly/easily remember how to navigate the content
        * I estimate this to be intuitive
   * Easily remember how to navigate play the game
        * The rules are straightforward, I estimate navigation to pages to be easy. For playing game the rules are easy to reach, and there is an example of input on game screen.

## Strategy
The purpose of this site is to create a simple-to-play game that requires a bit of logic, and which has the option of setting difficulties, and comparing to other players. The goal for design was to create a simple play-interface as well as making it easy to access information with simple and clear communication.

## Scope
The scope is within beginner boundaries. Features are limited but should be smooth and completely functional. Maximum three choices per screen, excluding return option.

## Structure
The features have been laid out previously. The flow of the website is simple and should be intuitive for most anyone. Game, rules, high scores. Players are guided through the game with supporting text that helps them understand what is happening. When starting the application, the player is immediately in the menu. In case there is some confusion / if the player wishes to know more about the rules of the game the navigation menu makes it simple to return. The structure is limited, so the menu should not make player feel lost.


## Surface

### Design choices
* Overview: The aim is to provide easy-to-navigate pages that make it easy and clear to navigate around. 
* The game should be easy for the eyes, meaning that there should be no text out of bounds/ not in line that confuse players.
* It should be clear to the player what should be done in order to advance.
* Losses/wins should be clear to understand and should have text that explains what happened.
* Information should not be detailed but fast to read and understand, and straight to the point.


### Languages used
* Python
* Markdown language for readme file


### Additional comments on setup
*  


