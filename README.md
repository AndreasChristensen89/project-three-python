add lucidchart for code logic

When installing pip I got the follow error-message:
WARNING: You are using pip version 21.1.3; however, version 21.2.1 is available.
You should consider upgrading via the '/home/gitpod/.pyenv/versions/3.8.11/bin/python3 -m pip install --upgrade pip' command.

This has not been installed yet

Link to Google sheet:
https://docs.google.com/spreadsheets/d/1VDhR8UUuAHAOBzgp_l9Ok1cZ5mcHgM7KnZ9ZBYMuL3M/edit?usp=sharing


# Battleship

The idea behind this project is to create a single-player game of battleships where the player should be able to play solo against the computer on different difficulties, being able to upload results, and seing other players' results.
The target group is anyone who enjoys a simple game that is a mix of chance and logic. The game requires a basic grasp of the rules and can be won either with pure luck, or more likely with a bit of strategy. However, the simple layout would be suited for people who are not interested in visual styling and only wants the pure game mechanics. The game has to be played in a terminal and can be played on modern browsers.

The aim of the game is to sink the ships with as few attempts as possible.

## Lucid Chart for overview of functionality

![Lucid Chart](/assets/images/readme-pictures/navigation-bar.webp)

## Features

### Existing features:
* __Menu data validation__
    * Data input in all menus is validated through a function, and in case of fail it prints an error message:
        * In case of number wrong: "Invaid data: Choice not valid, input must be numbers within range", followed by input field "Press any key to continue"
        * In case of character input: "Invalid data: invalid literal for int() with base 10: 'CHARACTERS', input must be numbers within rang

![Menu data validation](/assets/images/readme-pictures/navigation-bar.webp)

* __Main menu__
    * The main menu has four print statements that lists the options for the player, followed by an input field that reads: "Enter choice: ".
    * The player can choose between the following (screen is cleared for every choice):
        * Start game - this starts the game and redirects to set-difficulty screen
        * Rules - prints the objectives of the game and how to play
        * High score - redirects to high score lists
        * Exit game - exits the application
    * Data is validated through function


![Main menu](/assets/images/readme-pictures/navigation-bar.webp)

* __Rules__
    * Has 12 print statements that explain the rules and the objective, separated into three sections.
    * On top there is a heading "The rules of Battleship" followed by an empty line.
    * First section has five lines and explains the objective.
    * Second second has three lines and explains how to play.
    * Third section has three lines and explain the visual presentation and how to understand them, followed by empty line.
    * Below is an input field with the text "Press 'Enter' / any key to return to menu". Player can press enter, or any key + enter to return to main menu

![Rules](/assets/images/readme-pictures/landing-page.webp)

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

* __High score lists__
    * Each list has a similar appearance
    * Content is extracted from a Google Sheet and comes out as a list. List runs through function and is printed as desired:
        * At the top "Name" and "Misses" are printed, separated by spaces to leave room for content below. Next line is empty.
        * Scores are sorted so the fewest misses are printed on top (best result), with the correct name to the left.
        * Names are followed by spacing calculated from the length of the name -> all scores will be printed on the same "column"
    * Below is an input field with the text "Press 'Enter' / any key to return to menu". Player can press enter, or any key + enter to return to main menu.

![High Score](/assets/images/readme-pictures/introduction.webp)

* __Set difficulty__
    * Shows the different difficulty levels the player can choose. Choice is passed through a function that generates ship of random lenght (2-4) and random vertical/horizontal, and passes the coordinates into a list. When the corrent number of ships is in the list it is passed on, and the actual game starts.
    * Heading reads "Set the difficulty", followed by empty line
    * Three print statements:
        * 1: One ship
        * 2: Two ships
        * 3: Three ships
    * Last is an input field with the text "Enter choice: ". 
    * Data is validated through function

![Set difficulty](/assets/images/readme-pictures/main-game-screen.webp)

* __Game screen__
    * Board is printed, which is eight lists printed out with a " " separating them.
        * Top list represents the columns. First item is blank as this is simply an unused corner, which makes sure the columns are directly over the "coordinates" below.
        * The next seven lists each start with an uppercase letter of the alphabet, which goes one up ("A", "B",..."G") for each list, followed by seven "-" which represents untouched coordinates.
    * Below are empty lines, then text which tells the player how many attempts there are left. The number is a variable and will decrease when incorrect guesses are made.
    * In the bottom is an input field "Guess a row and a number: (e.g. C5)"
    * Data is validated through different function than the menus:
        * In case of wrong characters/order: "Error: invalid literal for int() with base 10: 's', must be letter and number within range" - new line - "Press any key to continue"
        * In case of letter/number out of range: "Error: out of bounds, must be letter and number within range" - new line - "Press any key to continue"
    * If data validated then board and hit count/attempts are updated:
        * Board will use input-coordinates to find list and index.
            * If this point exists in ship list then the index will be changed to "O", and then print "You hit the ship".
                * Hit count will add this coordinate to its list.
            * If the point doesn't exist the index will change to "X", and then print "You missed the ship"
                * Attempts variable will decrease by one
    * If attempts reach 0 the screen is cleared, and game over screen is printed.
    * If hit count list matches the ship list the screen is cleared and the game is won. Win screen is printed.

![Game Screen](/assets/images/readme-pictures/losing-screen.webp)

* __Game over screen__
    * A simple message of "Game Over" is printed, follwed by an empty line
    * Below two choices are printed:
        * 1: Return to the main menu - clears screen and returns to the main menu
        * 2: Exit - exits the application
    * In the bottom is an input field "Enter Choice: "
    * Data is validated through function

![Game over screen](/assets/images/readme-pictures/draw-screen.webp)
    
* __Win screen__
    * A congratulatory message is printed "Congratulations! You sank all the battleships", followed by empty line.
    * Three choices are printed:
        * 1: Register your score - redirects to register score
        * 2: Return to main menu - returns player to main menu with no records of score
        * 3: Exit game - exits application
    * Data is validated through function
    * Screen is cleared after every choice

![Win screen](/assets/images/readme-pictures/win-screen.webp)

* __Register score__
    * Input field is printed "Enter your name: (Max 10 letters)"
    * Data is validated, but only for length     

![Register score](/assets/images/readme-pictures/game-over-screen.webp)

* __Updating high score__
    * Screen is cleared and then it prints "Updating highscore list...". Once it the scores have been added it prints "List updated successfully".
    * It prints options for the player:
        * 1: Return to main menu - returns to the main menu
        * 2: Exit - Exits the application
    * In the bottom is an input field "Enter choice: "
    * Data is validated through function

![Updating high score](/assets/images/readme-pictures/victory-screen.webp)


### Future features to implement
* Add multiplayer option
* Multiplayer does not need to be live, but can grab a random set of coordinates given by a player at any moment. Players will know result from lists (Add search function to find outcome)
* Possibility for the player to add ships to play against the computer
* Possibility for the player to select board size.

## Testing
* Gitpod workspace was used to test functionality for both game and API
* After deployment, Heroku deployment terminal was used to test functionality for both game and API
* Data validation was tested with a large number of different input. Letters, characters, lengths, reverse, capital, lowecase.

__Breakpoints__
There are not breakpoints set for this project


### Browser testing 
* Test on Firefox, Edge, Chrome, and Safari
* Tested on my own phone, Samsung Galaxy S9 using Chrome and Firefox, no issues.
* Media query tested on my own tablet, Ipad pro 2018 11" using Safari+Chrome, no issues.
* General testing with my own laptop, Asus 13 inch using Chrome, no issues.

There are no links in this project.

### Bugs discovered during testing:
* I had a number of issues with creating ships as I was initially returning a dictionary with key:value pairs. The problem was that each key had to be different, so letters could not repeat, but they had to when it came to horizontal values, e.g. F2, F3, F4... Due to this, I chose to return a list instead.
    * In the beginning I wanted to return a list per ship, but I found it much easier to return a single list, which is really just a set of coordinates
* Clear screen issue: In my working environment on Gitpod I initially used the os.system('clear') command for clearing the terminal, thus giving a more visually pleasing transitioning. However, this didn't work on Heroku, and the next prints would simply be printed underneath with the 'old' text still visible. I tried different solutions with a function determining the operating system, and then calling the appropriate command:

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

Also:

    import os
    os.system('cls' if os.name == 'nt' else 'clear')c

However, it didn't work on the deployed version on Heroku, so instead I replaced the command with a print statement that prints 24 new lines: 
    print("\n"*24)
24 because of the 24 lines on the Heroku display

### Unfixed bugs
*


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
* To to deploy section -> Select "GitHub" -> confirm connection
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
### Icons
I imported the following:
* from random import randint - randint was to generate random numbers when generating lists of coordinates
* from operator import itemgetter - itemgetter was used to sort the lists extracted from Google sheet in order to bring lowest values first.
* import gspread & from google.oauth2.service_account import Credentials - used for the API setup

### Hosting and Development
GitHub was used to host the repository, GitPot was used for development and version control, and Heroku was used to deploy site.

## Credits:
### Pictures
Images for readme were obtained using Windows snipping tool, size lowered via https://tinypng.com/
Afterwards they were converted to webp using https://cloudconvert.com/png-to-webp.


### Text content
Content was all formulated by myself, as I have played the game many times in my life I didn't need to look up the rules or get inspiration for formulating.

### Coding help
* For help with varius challenges with Python I often resorted to the Material by Code Institute and https://stackoverflow.com/
* For help with syntax reminders I often used the material by Code Institute, as well as https://www.w3schools.com/ 
* For general best practice I used Code Institute's Slack community.

### Design
* For design of the different pages I didn't use other sources of information, but I did take inspiration from video games I have played throughout my life.
* Lucidchart was created using https://www.lucidchart.com/pages/

## User Stories:

### The User
* What are the goals for a first-time visitor
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
        * On the game screen there is input text which explains that the player should pick a letter and a number, and gives an example of input.
   * Understand how to advance after a hit/miss
        * There is a counter for attempts, which is meant to signal that the game is still ongoing, and the player should therefore continue as before
    * Understand where to find high scores, and how they are measured
        * Navigation is clearly displayed, in the high score menu the heading says "Select a list/difficulty to view", which tells the players that high scores are separated by difficulty.
        * In the high score lists a top remark tells the players "The fewer misses the better", which aims to make the player understand the hierarchy of scores, and explains why the lowest are on top.

* What are the goals for a returning visitor
   * Instantly/easily remember how to navigate the content
        * I estimate this to be intuitive
   * Easily remember how to play the game
        * Hint is given when pressing play, and navigation to the rules page is easy
   * Easily be able to contact the developer with questions, feedback, any other inquiries
        * Navigation to contact page is easy via hamburger, and contact form is simple to use with few input fields

## Strategy
The purpose of this site is to create a simple to play game that entertains visually, and which does not require strategy to play. The goal for design was to create a simple play-interface as well as making it easy to access information with simple and clear design.

## Scope
The scope is within beginner boundaries. Features are limited but should be smooth and completely functional. No more than three pages: game, rules, and contact.

## Structure
The features have been laid out previously. The flow of the website is simple and should be intuitive for most anyone. Game, rules, contact. Players are guides through the game with animated/colored elements that signal to press them. When accesing the webpage the user lands directly on the game page and can start immediately. In case there is some confusion / if the player wishes to know more about the background or rules of the game / wishes to contact the developer the navigation bar makes it simple to access all pages from anywhere and from any stage of the game. A restart button is also available when the game has started.


## Surface

### Design choices
* Overview: The aim is to provide easy-to-navigate pages that make it easy and clear to navigate around. 
* The game should be easy for the eyes, meaning that there should be no overlapping animations that confuse players.
* It should be clear to the player what should be clicked in order to advance.
* Losses/wins/draws should be clear to understand and should have animations that demonstrate what happened.
* Information should not be detailed but fast to read and understand, and straight to the point.

### Color Scheme 
Colors are chosen to represent a generally bright cartoony world, which aims to give users a positive and light-hearted feeling.
In all stages of the game, and on all pages, there is always a play between green and blue. Blue is the general color while green is always present but more scarcely found, and it used to represent something positive/progression. There is at all times at least one green element on the screen, which is meant to attract the users' eyes. 

Color names are found via https://www.htmlcsscolor.com/hex/749EAD.

* Background picture:
    * Main blue of window: rgb(114 217 237) - Turquoise Blue
    * Darkest building: rgb(113 175 188) - Glacier
    * Lighter building: rgb(129 193 206) - Seagull
    * Lightest building: rgb(146 212 225) - Anakiwa
    * Window bars: rgb(123 137 138) - Oslo Grey
    * Bottom and top bars: rgb(84 76 73) - Saddle
    * Floor: rgb(116 158 173) - Bali Hai
    * Bonsai box: rgb(120 73 46) - Cape Palliser
    * Bonsai box-lines: rgb(45 27 17) - Wood Bark
    * Bonsai bottom-pot: rgb(189 137 109) - Brandy Rose
    * Bonsai top-pot: rgb(168 116 86) - Sante Fe
    * Bonsai top-pot-circle: rgb(147 91 59) - Rope
    * Dirt: rgb(99 55 29) - Baker's Chocolate
    * Tree: rgb(128 81 55) - Cigar
    * Leaves: rgb(58 148 50) - La Palma
* **White**
    * All text on all pages
    * Background color of hamburger icon
* **rgb(116 158 173)** Bali Hai
    * Background color: this is the same color as the background picture's floor, allowing for extensions of the picture.
* **rgb(58 148 50)** La Palma - Green color of bonsai tree
    * Play button
    * Start button
    * Go-button
    * Health-meter
    * Try again button
    * H2 headings on rules page
    * Clear and send buttons on contact page
* **#455d66** San Juan - Dark grey
    * H1 on landing page 
    * H1 rules page
    * H1 contact page
* **#68acb9** Fountain blue
    * H2 landing page 
    * Text-box on intro-screen
    * Text-box on win screen
    * Text-box on victory screen
    * Intro text-box on rules page
    * Divs on rules page
    * Larger text boxes on rules page
    * Form color on contact page
* **#77acb2** Neptune
    * Opponent title
* **#ea8426** Carrot orange
    * Color when health drops below 75
* **#c7be33** Old Gold
    * Color when health drops below 50
* **#d01414** Free speech red
    * Color when color drops below 25
* **#989191** Nobel - grey
    * Color of corner restart button

### Choice of text
I found Lato to work quite well with all text. I think it complements the cartoony style.

### Pictures/characters:
Bright and colorful colors are chosen to give a positive feeling. It's meant for the user to think of it as light-hearted. The background was designed to be spacy, simple, and with only a few major variations of colors. The characters were drawn as simple and with a hint of humour - they're meant to be stereotypical Japanese office workers as depicted in manga/movies.

The background is designed and set to repeat in order to allow for stretching of the image.

### Languages used
* HTML
* CSS
* JavaScript
* Markdown language for readme file

### Accessibility
All non-text elements are marked with aria-labels, and the contrast between background and foreground colors were implemented in color scheme.

### Additional comments on setup
* CSS was split into two files due to a design choice of having no scrolling on the main page which affected the other pages. Styling for the hamburger navigation was also separated due to both pages needing CSS from it (no-repeat), and also to separate it from the other CSS as much of the styling comes from a site I used.
* JavaScript was split into two files (game-script and hamburger-navigation) due to eventlistener on load in one sheet that gives an error in the other, and also to separate as the hamburger code is not completely my own.
* Aria-labels turned out a bit tricky since elements come, go, and change during the game. Therefore, I implemented functions to add appropiate labels in JavaScript. 


