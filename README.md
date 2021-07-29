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

