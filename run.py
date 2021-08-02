from random import randint
from operator import itemgetter
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Battleship Highscores')


def main_menu():
    """
    Prints choices and takes int input. Validates data, redirects with choice.
    1: set_difficulty - 2: rules - 3: show_high_score - 4: exits application
    """
    while True:
        print("\n"*24)
        print("1: Start game")
        print("2: Rules")
        print("3: High scores")
        print("4: Exit game\n")
        user_choice = input("Enter choice: \n")

        if(menu_data_validation(user_choice, 4)):
            if user_choice == "1":
                print("\n"*24)
                set_difficulty()
                break
            elif user_choice == "2":
                rules()
                break
            elif user_choice == "3":
                show_high_scores()
                break
            elif user_choice == "4":
                print("\n"*24)
                print("Ciao")
                break


def set_difficulty():
    """
    Prints four choices and takes int input.
    Validates data and redirects according to choice
    1-3 calls start_game with input parameter to set number of ships/difficulty
    4: return to menu
    """
    while True:
        print("\n"*24)
        print("Set the difficulty\n")
        print("1: One ship")
        print("2: Two ships")
        print("3: Three ships")
        print("4: Return to menu\n")
        difficulty_choice = input("Enter choice: \n")

        if(menu_data_validation(difficulty_choice, 4)):
            if difficulty_choice == "4":
                main_menu()
                break
            else:
                start_game(int(difficulty_choice))
                break


def menu_data_validation(choice, num_of_choices):
    """
    Takes two parameters: input given and the max range of int to be accepted
    Attempts to convert choice parameter to int to provoke error
    Checks if choice is within range
    Calls out ValueErrors and prints a message to user
    Returns boolean value
    """
    try:
        int(choice)
        if int(choice) > num_of_choices or int(choice) < 1:
            raise ValueError("Choice not valid")
    except ValueError as e:
        print("\n"*24)
        print(f"Invalid data: {e}, input must be numbers within range")
        print(input("Press 'Enter' to continue\n"))
        print("\n"*24)
        return False
    return True


def rules():
    """
    Prints the rules, takes any input to return to main menu
    """
    print("\n"*24)
    print("The rules of Battleship: \n")
    print("You have limited attempts to sink the ships.")
    print("You decide how many ships there will be,")
    print("but you don't know how big they are or where they are placed.")
    print("The maximum number of points is 4, and the minimum is 2.")
    print("You need to hit all points of a ship in order to sink it.\n")
    print("Enter your coordinates to strike a point:")
    print("- One letter between A-H")
    print("- One number between 1-9")
    print("- For example: C4\n")
    print("If you miss the point will be marked with an 'X'.")
    print("If you hit a ship the point will be marked with a 'O'.\n")
    print(input("Press 'Enter' to return to menu\n"))
    main_menu()


def show_high_scores():
    """
    Prints choices of lists, takes input, validates and prints specifc list
    Gets all values from sheet, sorts them via itemgetter by second value
    Prints column headings separated by long space
    Prints the now sorted rows, added space calculated by length to align
    Takes any input to return to main menu
    """
    print("\n"*24)
    while True:
        print("Select a list/difficulty to view\n")
        print("1: One ship")
        print("2: Two ships")
        print("3: Three ships")
        print("4: Return to main menu\n")
        list_choice = input("Enter choice: \n")

        if(menu_data_validation(list_choice, 4)):
            if list_choice == "4":
                main_menu()
                break
            else:
                print("\n"*24)
                print("The fewer misses the better\n")
                dif_two = SHEET.worksheet(f'Difficulty {list_choice}')
                data = dif_two.get_all_values()
                data_sorted = sorted(data, key=itemgetter(1))
                print(data_sorted[-1][0]+"         " + data_sorted[-1][1]+"\n")
                for i in data_sorted[0:-1]:
                    space = " " * (13 - len(i[0]))
                    print(space.join(i))
                print(input("\nPress 'Enter' to return to menu\n"))
                main_menu()
                break
            break


def start_game(difficulty_choice):
    """
    Construct board with initial number-list, 1st is blank for corner value.
    For loop to append lists that take increasing letters as first index(rows).
    Board is passed and printed via add_board().
    Ship-generator called, difficulty level passed to know number of ships.
    Ask_for_choices() is called, board and ships generated are passed.
    """
    print("\n"*24)
    board = [[' ', '1', '2', '3', '4', '5', '6', '7']]
    board_rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    for x in range(0, 7):
        board.append([board_rows[x], "-", "-", "-", "-", "-", "-", "-"])

    add_board(board)

    ship = generate_ships(difficulty_choice)

    dare_letter = chr(randint(ord('A'), ord('G')))
    dare_number = randint(1, 7)
    print("")
    print(f"I dare you to pick {dare_letter}{dare_number}")

    ask_for_choices(board, ship, difficulty_choice)


def ask_for_choices(board, ship, difficulty_choice):
    """
    Attempts variable is created, decreases with loss and gameover if 0.
    Hit count list is created, right guesses (coordinates) are added.
    if hit count == ship list then win.
    Asks for input, validates data via validate_data(), checks for outcome.
    Right guess updates board with 'O', wrong with 'X', error if repeat guess.
    Checks if coordinate is repeated guess and prints message in case
    """
    attempts_left = 10

    hit_count = []

    while True:
        if attempts_left == 0:
            print("\n"*24)
            print("Game Over\n")
            end_of_game()
            break
        elif sorted(hit_count) == sorted(ship):
            print("\n"*24)
            win_game(attempts_left, difficulty_choice)
            break
        print(f"Attempts left: {attempts_left}")

        guess = input("Guess a row and a number: (e.g. C5) \n")

        if validate_data(guess, board):
            char_one = int(ord(guess[:1].lower())-96)
            char_two = int(guess[1:2])
            coordinate = board[char_one][char_two]

            if coordinate == "X" or coordinate == "O":
                print("\n"*24)
                add_board(board)
                print("")
                print("This point has already been guessed")
            elif guess.upper() in ship:
                print("\n"*24)
                hit_count.append(guess.upper())
                update_board(board, guess, "O")
            else:
                print("\n"*24)
                attempts_left -= 1
                update_board(board, guess, "X")


def generate_ships(number_of_ships):
    """
    Returns a list with ship coordinates.
    Uses while loop: randomizes vertical/horizontal and length.
    Calculates max letter (vertical) and max number (horizontal) using ship
    length ship to avoid out of bounds.
    For loop generates coodinates, result checked for duplicates -> +1 count
    When ship count == requested number of ships -> break loop -> returns list
    """
    ship_coordinates = []

    ship_count = 0

    while True:
        vertical_horizontal = randint(1, 2)
        ship_lenght = randint(2, 4)

        max_letter = chr(ord('H') - ship_lenght)
        random_row = chr(randint(ord('A'), ord(max_letter)))
        char_two = str(randint(1, 7))

        char_one = chr(randint(ord('A'), ord('G')))
        random_column = randint(1, (7-ship_lenght))

        add_ship = []
        for i in range(ship_lenght):
            if vertical_horizontal == 1:
                char_one = chr(ord(random_row) + i)
                add_ship.append(char_one+char_two)
            elif vertical_horizontal == 2:
                number_two = str(random_column + i)
                add_ship.append(char_one+number_two)

        if not any(item in ship_coordinates for item in add_ship):
            for i in add_ship:
                ship_coordinates.append(i)
            ship_count += 1
        if ship_count == number_of_ships:
            break
    return ship_coordinates


def validate_data(guess, board):
    """
    Attemps to convert second char of input to an int,
    Creates boolean value, creates for loop and attempts to find guess
    in lists, if not then False.
    Validates range of letter and number.
    If not ok raises valueerror, and reprints the board as it was before error
    """
    try:
        int(guess[1:2])
        test_letter = False
        for i in board:
            if i[0] == guess[:1].upper():
                test_letter = True
        test_len = len(guess)
        if int(guess[1:2]) > 7 or int(ord(guess[:1].lower())-96) > 7:
            raise ValueError("out of bounds")
        elif not test_letter or not test_len == 2:
            raise ValueError("invalid input")
    except ValueError as e:
        print("\n"*24)
        print(f"Error: {e}, must be letter and number within range")
        print(input("Press any key to continue"))
        print("\n"*24)
        add_board(board)
        print("")
        return False
    return True


def update_board(board, guess, mark):
    """
    For loop: Uses first char of player guess to find the right list,
    uses second char to locate right index to change to mark-parameter.
    Board is printed with mark value added, and message of miss/hit
    """
    for i in board:
        if i[0] == guess[:1].upper():
            i[int(guess[1:2])] = f"{mark}"
    for i in board:
        print(" ".join(i))
    print("\n")
    if mark == "X":
        print("You missed the ship")
    elif mark == "O":
        print("You hit the ship")


def add_board(board):
    """
    Prints out current board. Board defined in start_game().
    For loop prints out all items in list separated by " " using join().
    Board not defined here in order to be able to reprint current board,
    which is printed after error messages.
    """
    for i in board:
        print(" ".join(i))
    print("")


def win_game(attempts, difficulty_choice):
    """
    Gives user three choices; register score, main menu, or exit.
    Validates input.
    Register - calls register_high_score, passes difficulty and attempts used
    Return calls main_menu(), and exit ends application
    """
    while True:
        print("Congratulations! You sank all the battleships\n")
        print("1: Register your score")
        print("2: Return to main menu")
        print("3: Exit game\n")
        choice = input("Enter choice: \n")

        if(menu_data_validation(choice, 3)):
            if choice == "1":
                print("\n"*24)
                register_high_score(attempts, difficulty_choice)
                break
            elif choice == "2":
                print("\n"*24)
                main_menu()
                break
            elif choice == "3":
                print("\n"*24)
                print("Ciao")
                break
            break


def register_high_score(attempts, difficulty_choice):
    """
    Asks user to enter name
    Checks if length of name is within 1-10 characters
    Calls update function and passes name, attempts, and difficulty choice
    """
    while True:
        name = input("Enter your name: (Max 10 letters) \n")
        print("\n"*24)
        if len(name) <= 10 and len(name) > 0:
            update_high_score(name, attempts, difficulty_choice)
            break
        else:
            print("Name must be between 1-10 characters")


def update_high_score(name, attempts, difficulty_choice):
    """
    Creates list to append with name provided and calculated missed shots.
    Accesses specific worksheet by using difficulty choice.
    Updates worksheet, prints statement when done.
    """
    print("Updating high score list...")
    list_to_append = [name, 10-attempts]
    diff_worksheet = SHEET.worksheet(f'Difficulty {difficulty_choice}')
    diff_worksheet.append_row(list_to_append)
    print("List updated successfully\n")
    end_of_game()


def end_of_game():
    """
    Gives users two options and validates data.
    1: main_menu - 2: exit
    """
    while True:
        print("1: Return to main menu")
        print("2: Exit\n")
        choice = input("Enter choice: \n")

        if menu_data_validation(choice, 2):
            if choice == "1":
                print("\n"*24)
                main_menu()
                break
            elif choice == "2":
                print("\n"*24)
                print("Ciao")
                break
            break


print("Welcome to Battleships\n")
main_menu()
