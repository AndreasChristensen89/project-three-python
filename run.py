from random import randint
# import os
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

# clear = lambda: system('clear')


# cls = lambda: system('cls')


def main_menu():
    """
    """
    while True:
        print("\n"*24)
        print("1: Start game")
        print("2: Rules")
        print("3: High scores")
        print("4: Exit game\n")
        user_choice = input("Enter choice: \n")

        if(validate_choice(user_choice, 4)):
            if user_choice == "1":
                print("\n"*24)
                set_difficulty()
                break
            elif user_choice == "2":
                rules()
                print("\n"*24)
                break
            elif user_choice == "3":
                show_high_scores()
                break
            elif user_choice == "4":
                print("\n"*24)
                print("Ciao")
                break


def set_difficulty():
    while True:
        print("\n"*24)
        print("Set the difficulty\n")
        print("1: One ship")
        print("2: Two ships")
        print("3: Three ships\n")
        difficulty_choice = input("Enter choice: \n")

        if(validate_choice(difficulty_choice, 3)):
            start_game(int(difficulty_choice))
            break


def validate_choice(choice, num_of_choices):
    """
    """
    try:
        int(choice)
        if int(choice) > num_of_choices or int(choice) < 1:
            raise ValueError("Choice not valid")
    except ValueError as e:
        print("\n"*24)
        print(f"Invalid data: {e}, input must be numbers within range")
        print(input("Press any key to continue\n"))
        print("\n"*24)
        return False
    return True


def rules():
    """
    """
    print("\n"*24)
    print("The rules of Battleship: \n")
    print("You have limited attempts to sink the ships.")
    print("You decide how many ships there will be,")
    print("but you don't know how big they are or where they are placed.")
    print("The maximum size is 4, and the minimum is 2.\n")
    print("Enter your coordinates to strike a point:")
    print("- One letter between A-H")
    print("- One number between 1-9")
    print("- For example: C4\n")
    print("If you miss the point will be marked with an 'X'.")
    print("If you hit a ship the point will be marked with a 'O'.")
    print("You need to hit all points of a ship in order to sink it.\n")
    print(input("Press 'Enter' to return to the main menu\n"))
    main_menu()


def show_high_scores():
    """
    """
    print("\n"*24)
    while True:
        print("Select a list to view\n")
        print("1: One ship")
        print("2: Two ships")
        print("3: Three ships")
        print("4: Return to main menu\n")
        list_choice = input("Enter choice: \n")

        if(validate_choice(list_choice, 4)):
            if list_choice == "4":
                main_menu()
                break
            else:
                print("\n"*24)
                dif_two = SHEET.worksheet(f'Difficulty {list_choice}')
                data = dif_two.get_all_values()
                data_sorted = sorted(data, key=itemgetter(1))
                print(data_sorted[-1][0]+"         " + data_sorted[-1][1]+"\n")
                for i in data_sorted[0:-1]:
                    space = " " * (13 - len(i[0]))
                    print(space.join(i))
                print(input("\nPress 'Enter', or any key, to return\n"))
                main_menu()
                break
            break


def start_game(difficulty_choice):
    """
    Construct board with initial number-list, 1st is blank for corner value.
    Followed by lists that take increasing letters as first index (rows).
    Board is passed and printed via add_board().
    Ships are generated, difficulty level passed to know number of ships.
    Ask_for_choices() is called, board and ships generated are passed.
    """
    print("\n"*24)
    board = []
    board_rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    board.append([' ', '1', '2', '3', '4', '5', '6', '7'])
    for x in range(0, 7):
        board.append([board_rows[x], "-", "-", "-", "-", "-", "-", "-"])

    add_board(board)

    ship = generate_computer_ship(difficulty_choice)

    ask_for_choices(board, ship, difficulty_choice)


def ask_for_choices(board, ship, difficulty_choice):
    """
    Attempts variable is created, decreases with loss and gameover if 0.
    Hit count list is created, right guesses (coordinates) are added,
    if hit count == ship list then win.
    Asks for input, validates data via validate_data(), checks for outcome.
    Right guess update board with 'O', wrong with 'X', error if repeat guess.
    """
    attempts = 10

    print(ship)
    hit_count = []

    while True:
        if attempts == 0:
            print("\n"*24)
            print("Game Over\n")
            end_of_game()
            break
        elif sorted(hit_count) == sorted(ship):
            print("\n"*24)
            win_game(attempts, difficulty_choice)
            break
        print(f"Attempts left: {attempts}")

        guess = input("Guess a row and a number: (e.g. D8) \n")

        if validate_data(guess, board):
            char_one = int(ord(guess[:1].lower())-96)
            char_two = int(guess[1:2])
            coordinate = board[char_one][char_two]

            if coordinate == "X" or coordinate == "O":
                print("\n"*24)
                add_board(board)
                print("This point has already been guessed")
            elif guess.upper() in ship:
                print("\n"*24)
                hit_count.append(guess.upper())
                update_board(board, guess, "O")
                # print(hit_count)
                # print(ship)
            else:
                print("\n"*24)
                attempts -= 1
                update_board(board, guess, "X")


def generate_computer_ship(number_of_ships):
    """
    Returns a list with ship coordinates.
    Uses while loops: adds ships of random size and random vertical/horizontal.
    Calculates max letter and max number for vertical/horizontal ship.
    Checks new ships with return list to avoid overlaps/duplicate coordinates.
    While loop stops when added ships == number of ships requested
    """

    ship_points = []

    ship_count = 0

    while True:
        vertical_horizontal = randint(1, 2)
        if vertical_horizontal == 1:
            while True:
                ship_lenght = randint(2, 4)
                max_letter = chr(ord('H') - ship_lenght)
                random_row = chr(randint(ord('A'), ord(max_letter)))
                char_two = str(randint(1, 7))

                vert_ship = []
                for i in range(ship_lenght):
                    char_one = chr(ord(random_row) + i)
                    vert_ship.append(char_one+char_two)

                if not any(item in ship_points for item in vert_ship):
                    for i in vert_ship:
                        ship_points.append(i)
                    ship_count += 1
                    break
        elif vertical_horizontal == 2:
            while True:
                ship_lenght = randint(2, 4)
                char_one = chr(randint(ord('A'), ord('G')))
                hori_col = randint(1, (7-ship_lenght))

                hori_ship = []
                for i in range(ship_lenght):
                    char_two = str(hori_col + i)
                    hori_ship.append(char_one+char_two)
                if not any(item in ship_points for item in hori_ship):
                    for i in hori_ship:
                        ship_points.append(i)
                    ship_count += 1
                    break
        if ship_count == number_of_ships:
            break
    return ship_points


def validate_data(guess, board):
    """
    Attemps to convert second char of input to an int,
    tests if first char is a string, and tests length.
    Validates range of letter and number
    Raises valueerror, and reprints the board as it was before error
    """
    try:
        int(guess[1:2])
        test_str = isinstance(guess[:1], str)
        test_len = len(guess)
        if int(guess[1:2]) > 7 or int(ord(guess[:1].lower())-96) > 7:
            raise ValueError("out of bounds")
        elif not test_str or not test_len == 2:
            raise ValueError("invalid input")
    except ValueError as e:
        print("\n"*24)
        print(f"Error: {e}, must be letter and number within range")
        print(input("Press any key to continue"))
        print("\n"*24)
        add_board(board)
        return False
    return True


def update_board(board, guess, mark):
    """
    Uses first char of player guess to find the right list,
    then uses second char to locate right index to change to mark-parameter.
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
    print("\n")


def win_game(attempts, difficulty_choice):
    """
    Gives user three choices; register score, main menu, or exit
    Validates input
    Register calls register_high_score and passes difficulty and attempts
    Return calls main_menu, and exit ends application
    """
    while True:
        print("Congratulations! You sank all the battleships\n")
        print("1: Register your score")
        print("2: Return to main menu")
        print("3: Exit game\n")
        choice = input("Enter choice: \n")

        if(validate_choice(choice, 3)):
            if choice == "1":
                print("\n"*24)
                register_high_score(attempts, difficulty_choice)
                break
            elif choice == "2":
                print("\n"*24)
                main_menu()
                break
            elif choice == "3":
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
    Accesses specific worksheet by using difficulty choice
    Updates worksheet, by creating list to add to new row with the parameters
    """
    print("Updating highscore list...")
    list_to_append = [name, 10-attempts]
    diff_worksheet = SHEET.worksheet(f'Difficulty {difficulty_choice}')
    diff_worksheet.append_row(list_to_append)
    print("List updated successfully\n")
    end_of_game()


def end_of_game():
    while True:
        print("1: Return to main menu")
        print("2: Exit\n")
        choice = input("Enter choice: \n")

        if validate_choice(choice, 2):
            if choice == "1":
                print("\n"*24)
                main_menu()
                break
            elif choice == "2":
                break
            break


def main():
    """
    Main function to set in motion the other functions
    """
    main_menu()


print("Welcome to Battleships\n")
main()
