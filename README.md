add lucidchart for code logic

Remember to add \n to input messages for deployment

When installing pip I got the follow error-message:
WARNING: You are using pip version 21.1.3; however, version 21.2.1 is available.
You should consider upgrading via the '/home/gitpod/.pyenv/versions/3.8.11/bin/python3 -m pip install --upgrade pip' command.

This has not been installed yet

Remember to remove print statements from ask_for_choices elif

Link to Google sheet:
https://docs.google.com/spreadsheets/d/1VDhR8UUuAHAOBzgp_l9Ok1cZ5mcHgM7KnZ9ZBYMuL3M/edit?usp=sharing

Clear screen issue:
In my working environment on Gitpod I initially used the os.system('clear') command for clearing the terminal, thus giving a more visually pleasing transitioning. However, this didn't work on Heroku, and the following prints would simply be printed underneath with the 'old' text still visible. I tried different solutions with a function determining the operating system, and then calling the appropriate command:

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
os.system('cls' if os.name == 'nt' else 'clear')

However, it didn't work on the deployed version on Heroku, so instead I replaced the command with a print statement that prints 24 new lines: 

print("\n"*24)
24 because of the 24 lines on the Heroku display


# Battleship

The idea behind this project is to create a single-player game of battleships where the player should be able to play solo against the computer on different difficulties, being able to upload results, and seing other players' results.
The target group is anyone who enjoys a simple game that is a mix of chance and logic. The game requires a basic grasp of the rules and can be won either with pure luck, or more likely with a bit of strategy. However, the simple layout would be suited for people who are not interested in visual styling and only wants the pure game mechanics. The game has to be played in a terminal and can be played on modern browsers.

The aim of the game is to play sink the ships with as new attempts as possible.

## Features

### Existing features:
* __Main menu__
    * The navigation bar is on all pages. It has links to the Home page, the Rules page, and the Contact page.
    Visually, it is identical on each page but with a bottom border under the current page. It is a hamburger-style bar and appears and dissapears when clicking the round icon. It appears by sliding down from the top and covers a small area in the left side of the page and dissapears by sliding up.
    * This section allows the user to always be able to navigate to all parts of the website without going back to the home page or scrolling to the top. The hamburger style allows the bar to be hidden in the top corner when not opened, thus creating more space for the game.

![Main menu](/assets/images/readme-pictures/navigation-bar.webp)

* __Rules__
    * The landing page has a centered heading with the title of the game at the top. Underneath is a centered sub-heading which acts as the subtitle. Finally, underneath the subtitle is the play button which has an animation on it to scale the size up and down. The background is a cartoony bright colored open office space with a bonsai tree close to the window. The windows show buildings outside.
    * The titles and play button are shown to indicate that this is the start of the game. The play button animation is used to indicate that this button should be noticed and interacted with. The background is displayed to show the setting of the game,

![Rules](/assets/images/readme-pictures/landing-page.webp)

* __High Score__
    * This section appears after clicking play. It has a centered textbox with a quick tutorial of how to play, and underneath is a centered green start button.
    * The quick tutorial gives players the information they need to play the game. The start button is green and animated and sticks out to invite users to click it to start the game.

![High Score](/assets/images/readme-pictures/introduction.webp)

* __Set difficulty__
    * At the top of the screen the name of the current opponent is displayed as a title. 
    * Underneath is a green oval-shaped element with "100" written in it - this is the health meter. 
    * Underneath the health meter are five buttons with pictures of the different choices players can make.
    * Under the buttons is the opponent element with a picture of the current opponent - if this is the first opponent then the element is not animated, but if it isn't the opponent is animated with an opacity going from 0.0 to 1.0 over a second.
    * When a button is clicked the player choice appears in the middle of the screen, meaning that the picture of the button is copied to this new element. The new element is animated to scale up and down and a green "go" button is generated and appears under the player choice.
    * Lastly, in the right corner is a now a restart button.
    * The opponent title changes according to the opponent and tells the players who they are versing. The green health meter changes numbers and colors according to how much health is left (green, orange, yellow, and red). The color code helps players easily understand how close they are to a loss. The five buttons clearly show the hand signals that are attached to them, and they scale up when a mouse hovers over them and scale down when mouse is off. The player choice animation signals to the player that this displayed hand is ready to be played. The opponent element is animated to appear in order to draw attention to the new opponent.

![Set difficulty](/assets/images/readme-pictures/main-game-screen.webp)

* __Game screen__
    * When a loss is registered the computer choice is displayed in a new element. The computer hand is animated to scale up a lot, and then scales down to land underneath a newly generated grey textbox which gives players a short comment on the loss.
    * The player choice animation from before is set to stop.
    * The health bar is animated to blink red and black, and the health number drops while the color changes according to the value.
    * The hand-buttons are animated to scale up and down, which stops when a hand is clicked.
    * The computer winning hand is scaled up in order to give the player a sense of defeat. It also draws their attention to the hand that beat them. The comments in the text box are randomly picked and they are encouraging and energetic which signals to the players to have another go. The health bar blinks in order to signal that damage has been taken. The hand-buttons start to scale in order to let players know that they should be interacted with in order to continue.

![Game Screen](/assets/images/readme-pictures/losing-screen.webp)

* __Game over screen__
    * When a draw is registered the computer choice is generated and inserted underneath the player choice. Underneath the computer choice a grey textbox is also generated with the message of "Draw! Try again". The computer choice and player choice elements are animated to bump against each other two times.
    * The hand-buttons are animated to scale up and down, which stops when a hand is clicked.
    * The animation signals that the two hands are evenly matched. The message is short and clear and should not easily be misunderstood. Similar to the losing screen, the hand animations signals to player to interact with them to continue.

![Game over screen](/assets/images/readme-pictures/draw-screen.webp)
    
* __Win screen__
    * Buttons, player choice and go button are removed, and the winning hand choice is shown in an animated element that scales up and down. To the right of the winning hand is the computer losing hand which is animated going back and forth from opacity 1.0 to 0.1. Underneath is a text box with text that declares that you beat the current opponent and tells you to get ready for the next opponent. The current opponent name and name of next opponent are variables and change according to the stage of the game. Under the next box is a green "next opponent" button, which is animated to scale up and down with a slower pace than the winning hand.
    * The winning hand is animated to scale up and down to signal victory. The other opacity animation solidifies the sensation of victory. The winning message is short and clear, and the green button signals users to click on it via the animation.

![Win screen](/assets/images/readme-pictures/win-screen.webp)

* __Register score__
    * All previous game elements are removed, and a large black text box is inserted at the top center with the text "Game Over!". This box is animated to scale up and down.
    * Underneath is a centered grey text box with text that explains that the player lost, and which also encourages the player to try again.
    * Underneath is a green round button with the text "Try again"
    * The black color of the game over text is a clear opposite to all previous colors, which are light a bright, which is meant to invoke a negative sensation. The animation is there in order to draw the player's eyes to it. The losing message from the grey box is not harsh but instead reminds the player that this is game of chance "Looks like the odds were against you". It also encourages players to try again. The "try again" button is large and clear, and the green color is meant to give a "go" feeling similar to the play button and the start button.                                                                                                                       

![Register score](/assets/images/readme-pictures/game-over-screen.webp)

* __Updating high score__
    * A green centered textbox with the content "You Win!" is at the top. It scales up and down continuously. 
    * Underneath is a light-blue textbox that declares that the player managed to rise to the top and has won the game.
    * Underneath is a green button restart button, which is also used in the game over screen.
    * The scaling of the win title draws the users' eyes to it, which aims to make sure that what is going on is clear. The green color gives a positive feeling. The text-box underneath is in a light color with congratulative text, which is most often expected after winning a game. Lastly, the try again button is similar in style to the one on the gameover screen, but with the text "restart" instead of "try again", which differs in tone.

![Updating high score](/assets/images/readme-pictures/victory-screen.webp)

* __See high score__
    * Dark heading in the center with the text "how to play"
    * Underneath short introduction of the game in a grey-blue background textbox.
    * Underneath a green textbox with the title "What beats what?"
    * Underneath is five boxes side by side. Each has the name of a hand that players can choose, and underneath each is a picture of how the hand looks. Below the picture are two statements about what the hand in question beats in a game.
    * Below is a title similar in style to "what beats what", with the content "Setting of the game".
    * Underneath is a larger text box with an explanation of how the game Janken works in Japanese culture. Same color as the boxes further up.
    * Underneath is another large text box with an explanation of the back-story/setting of the game on this webpage. Same color as above.
    * There are three main colors - dark at the top, green for h2 titles, and lighter blue/gray for text. They are chosen to fit with the background blue, and the bonsai tree. 
    * The introduction is valuable as players may not be familiar with the extended version of rock paper scissors.
    * Explanation of what beats what is valuable as players want to be clear about the rules. The pictures complement well since people may not know all the hand signals, and that they only have the visual representation when playing the game.
    * Explanation of how rock paper scissors work on Japanese culture is valuable as it adds some context to why a Japanese setting was chosen.
    * Setting of the game is valuable as it may not be clear to the player in the beginning what the bigger purpose of the game is. Also, it adds a slight humorous twist.

![See high score](/assets/images/readme-pictures/rules.webp)

* __Contact Page__
    * Dark centered heading with "contact" written. Same style as on rules page.
    * Underneath is a box with four input fields: First name, Last name, Email Address, and Message. The message field is larger that the other fields.
    * Below the fields are two green buttons: "clear" and "send". They both individually change to white when hovering over them.
    * The colors chosen are in line with the other pages.
    * It is valuable for the player to be able to contact the developers. The setup is simple and straight to the point.

![Contact page](/assets/images/readme-pictures/contact-page.webp)


### Future features to implement
* Add multiplayer option
* Multiplayer does not need to be live, but can grab a random set of coordinates given by a player at any moment. Players will know result from lists (Add search function to find outcome)
* On the game screen the opponent should have stats: Health and HP damage - this would change the game so that a single win would not necesarily be enough to beat the current opponent
* A 10% chance of a critical hit/power up (e.g., double damage) could be implemented - this would only work if opponent stats are implemented
* Add potions/special moves: e.g. coffee that boosts health, HR department that works as shield, ability that allow players one more chance to get it right etc.
* Add weaknesses and strenghts for each opponent

## Testing
* Chrome Developer Tools was used for testing all media queries down to width 280px to fit the smallest device available on the Google device list.
Also, Developer Tools was used to manipulate CSS to see direct outcomes. All pages have been tested with chrome developer tools to verify that text, pictures, and boxes all adapt well to the breakpoints for different screens. 

__Breakpoints are set to the following and are all tested to work:__

* __Max width 800px__
   * **Start screen:** 
        * Background-size is changed from contain to cover in order to avoid picture strething with floor too long. X and Y coordinates are set differently to adapt to new setting. 
        * Margins of the h1 and h2 are changed.
   * **Introduction screen:** 
        * P element's width, font-size, and padding are lowered. 
        * Font-size and width of start button lowered.
   * **Game screen:** 
        * Opponent-title's font-size and width lowered.
        * Margin for buttons changed.
        * Opponent-picture's height lowered, width increased. Top% increased, right% lowered.
        * Go-button margin lowered.
   * **Loosing screen**
        * Computer hand's margins changed.
   * **Draw screen** 
        * The "draw" message's margin is set to 0 auto.
   * **Win screen**
        * Player pick's margins changed, width lowered.
        * Computer losing hand's width lowered, margins changed.
        * Result text-box's margins lowered.
        * Next button's margins lowered.

* __Max width 600px__
   * **Start screen:** 
        * widths and font-sizes of h1 and h2 are lowered
        * Width and height of hamburger icon increased. Font-size increased.
   * **Introduction screen:** 
        * P element's width and font-size are lowered.
   * **Game screen:** 
        * Opponent-title's font-size and width lowered.
        * Hand-buttons widths increased, margins changed.
        * Opponent-picture's top% increased. Height lowered, width increased.
        * Player-choice margins changed.
        * Restart button's width, height, and font-size increased.
   * **Loosing screen**
        * Lose-message's font-size and width are lowered, margins changed.
        * Computer hand's margins increased.
   * **Win screen**
        * Result text-box's margins, line-height, width, font-size lowered, 
        * Result text-box's margins increased.
        * Game-area's height lowered
   * **Victory screen**
        * Win-title's width and font-size lowered.
        * Win-text's width and font-size lowered.
        * Restart button's font-size lowered.
   * **Game over screen**
        * Game over title's width and font-size lowered.
        * Game over text's width and font-size lowered.

* __Max width 320px__
   * **Game screen:** 
        * Opponent-title's width lowered.
        * Hand-buttons height and width lowered, margins changed.
        * Opponent-picture's top% increased.

* __Max height 400px, Max width 700px - meant for phones in landscape mode__
    * **Game screen**
        * Hand-buttons margins changed.
        * Player-choice margins changed.
    * **Lose screen**
        * Lose-message margin lowered, width increased.
        * Computer hand's margins lowered.
    * **Win screen**
        * Player pick margins lowered
        * Computer losing hand's margin lowered.
        * Result text-box's margins lowered.
        * Game-area's height lowered
    * **Victory screen**
        * Win-text's width increased, margins lowered.
    * **Game over screen**
        * Game over title's width increased.
        * Game over text's margins lowered, width increased.


### Browser testing 
* Test on Firefox, no problems detected.
* Microsoft Edge, no problems detected.
* Media query tested on my own phone, Samsung Galaxy S9 using Chrome and Firefox, no issues.
* Media query tested on my own tablet, Ipad pro 2018 11" using Safari+Chrome, no issues.
* General testing with my own laptop, Asus 13 inch using Chrome, no issues.

All links were tested. There are no external links, but all internal links work. 

### Bugs discovered during testing:
* I found the Google Developer Tool to not be stable in showing if the website responded correctly to different screensizes, particularly the phone settings as my own phone would show a smaller outcome.
* JShint gave an error (Functions declared within loops referencing an outer scoped variable may lead to confusing semantics. (choice)) regarding a function where a loop sets an eventlistener to trigger a function. This was just a warning, and after consulting with my mentor I was told to let it be. A similar usage is also used in the Love Maths learning project.
* During the first Jshint testing there were many warnings regarding template literals. This was unnecesarily used by me many times so I corrected them, e.g. "xx = `${variable}`;" would be corrected to xx = variable;
* As I wanted a game page that didn't allow scrolling I had many issues with setting up the right CSS to have the opponent picture staying on the floor of the background. Initially I set up many breakpoints, however this turned out to be too extensive. In the end I changed the height and width of the elements to correspond to the height of the screen, which worked across devices, and was miles shorter to code. This was only used for the game, for the other pages I resorted to "normal" breakpoints which had set values for each breakpoint.
* With the game CSS setup it was very difficult to fit it to phones in landscape mode, so I ended up using a different media query section using two inputs; max-height and max-width.

### Unfixed bugs
* "Interest-Cohort Error" on console after deployment. I was not able to fix this error, and I can understand that it's a recent feature where Github blocks FLoC https://www.techradar.com/uk/news/github-is-blocking-floc.


### Validator testing:
* W3 Markup Validation Service completed for all HTML pages with no errors.
* Jigsaw test for all CSS files completed with no errors.
* Jshint completed with one warning, but as described in "bugs discovered during testing" it could be ignored.

## Deployment
### Deployment to GitHub Pages
The site was deployed to GitHub Pages, and goes as follows:
In the GitHub repository, go to the Settings tab
From the source section drop-down menu, select the Master Branch
After selecting the master branch, the page will automatically be refreshed with a ribbon display to indicate the successful deployment.
The live link can be found here - https://andreaschristensen89.github.io/janken-bossu/

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
Icons and script were taken from https://fontawesome.com/, as well as Google's fonts: https://fonts.google.com/icons?selected=Material+Icons.

### Hosting and Development
GitHub was used to host the repository, GitPot was used for development and version control, and GitHub Pages was used to deploy site.

## Credits:
### Pictures
Images were compressed using the webpage https://tinypng.com/
Afterwards they were converted to webp using https://cloudconvert.com/png-to-webp
All characters, hands, and backgrounds were drawn by myself in Adobe Illustrator.


### Text content
Content was all formulated by myself, but I took inspiration from video/board games I have played throughout my life, comic books I have read, as well as my own experiences living in Japan.

### Coding help
* For help with varius issues with animations, css background manipulation etc. I often resorted to https://stackoverflow.com/
* For help with syntax reminders I often used https://www.w3schools.com/ 
* For general best practice I used Code Institute's Slack community.
* For hamburger nagivation I took inspiration from the code from this site, but I changed the location, animation/CSS, names, parts of the JS code, and the contents to fit my site:
https://dev.to/ljcdev/easy-hamburger-menu-with-js-2do0
* General comments from family and peers for what CSS looked the best, and what was most intuitive for the JS game design.

### Design
* For design of the different pages I didn't use other sources of information. For hand-buttons, parts of the background, and tattoos of one character I took inspiration from https://www.pinterest.com/ - only tattoos are partly copies.
* No wireframes were used

## User Stories:

### The User
* What are the goals for a first-time visitor
   * Quickly understand that this is a game and how to start it
        * This is indicated by the play button, which is animated to attract attention
   * Be captivated by the content and the imagery
        * Bright positive colors are used with contrast
   * Be able to navigate effortless through the pages
        * Hamburger navigation is always available, and there are only three pages.
   * Easily reach the rules page and understand how to play the game
        * Navigation is easy, and rules are explained right away.
   * Easily understand the goal of the game
        * Rules are written simple and with visuals to help. Introduction also gives additional help.
   * Understand how to advance after a loss/defeat/draw
        * Buttons are set to animate to attract the user
   * Have the game work on all devices, both horizontally and vertically
        * The website works on all devices
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


