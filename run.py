from random import randint
import os


def main_menu():
    """
    """
    while True:
        os.system('clear')
        print("1: Start game")
        print("2: Rules")
        user_choice = input("Enter choice: ")

        if(validate_choice(user_choice)):
            if int(user_choice) == 1:
                os.system('clear')
                set_difficulty()
            elif int(user_choice) == 2:
                rules()
                os.system('clear')
            break


def set_difficulty():
    while True:
        os.system('clear')
        print("Set the difficulty")
        print("1: One ship")
        print("2: Two ships")
        print("3: Three ships")
        difficulty_choice = int(input("Enter choice: "))

        if(validate_choice(difficulty_choice)):
            start_game(difficulty_choice)


def validate_choice(choice):
    """
    """
    try:
        int(choice)
        if int(choice) > 3 or int(choice) < 1:
            raise ValueError("Choice not valid")
    except ValueError as e:
        os.system('clear')
        print(f"Invalid data: {e}, input must be numbers within range")
        print(input("Press any key to continue"))
        os.system('clear')
        return False
    return True


def rules():
    """
    """
    os.system('clear')
    print("The rules of Battleship: \n")
    print("You have limited attempts to sink the ships.")
    print("You decide how many ships there will be,")
    print("but you don't know how big they are or where they are placed.")
    print("The maximum size is 4, and the minimum is 2.\n")
    print("Enter your coordinates to strike the point:")
    print("- One letter between A-H")
    print("- One number between 1-9")
    print("- For example: C4\n")
    print("If you miss the point will be marked with an 'X'.")
    print("If you hit a ship the point will be marked with a 'O'.")
    print("You need to hit all points of a ship in order to sink it.\n")
    print(input("Press 'Enter' to return to the main menu"))
    main_menu()


def start_game(difficulty_choice):
    """
    Construct board with initial number-list, 1st is blank for corner value.
    Followed by lists that take increasing letters as first index (rows).
    Board is passed and printed via add_board().
    Ships are generated, difficulty level passed to know number of ships.
    Ask_for_choices() is called, board and ships generated are passed.
    """
    os.system('clear')
    board = []
    board_rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    board.append([' ', '1', '2', '3', '4', '5', '6', '7'])
    for x in range(0, 7):
        board.append([board_rows[x], "-", "-", "-", "-", "-", "-", "-"])

    add_board(board)

    ship = generate_computer_ship(difficulty_choice)

    ask_for_choices(board, ship)


def ask_for_choices(board, ship):
    """
    Attempts variable is created, decreass with loss and gameover if 0.
    Hit count list is created, right guesses (coordinates) are added,
    if hit count == ship list then win.
    Asks for input, validates data via validate_data(), checks for outcome.
    Right guess update board with 'O', wrong with 'X', error if repeat guess.
    """
    attempts = 10

    print(ship)
    hit_count = []

    while True:
        if attempts == 1:
            os.system('clear')
            print("Game Over")
            break
        elif sorted(hit_count) == sorted(ship):
            os.system('clear')
            print("Congratulations! You sank all the battleships")
            break
        print(f"Attempts left: {attempts}")

        guess = input("Guess a row and a number: (e.g. D8) \n")

        if validate_data(guess, board):
            number_one = int(ord(guess[:1].lower())-96)
            print(number_one)
            number_two = int(guess[1:2])

            if guess in ship:
                os.system('clear')
                hit_count.append(guess)
                # print(hit_count)
                update_board(board, guess, "O")
            elif board[number_one][number_two] == "X":
                os.system('clear')
                add_board(board)
                print("This point has already been guessed")
            else:
                os.system('clear')
                attempts -= 1
                update_board(board, guess, "X")


def generate_computer_ship(number_of_ships):
    """
    Returns a list with ship coordinates.
    Uses while loops: adds ships of random size and random vertical/horizontal.
    Calculates max letter and max number for verti/horiz ship.
    Matches new ships with return list to avoid overlaps/duplicates
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
        os.system('clear')
        print(f"Error: {e}, must be letter and number within range")
        print(input("Press any key to continue"))
        os.system('clear')
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
        if i[0] == guess[:1]:
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
    Not defined here in order to be able to reprint current board,
    which will print after error messages.
    """
    for i in board:
        print(" ".join(i))
    print("\n")


def main():
    """
    Main function to set in motion the other functions
    """
    main_menu()


print("Welcome to Battleships")
main()
