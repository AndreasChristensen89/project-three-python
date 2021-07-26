from random import randint
import os


def main_menu():
    """
    """
    while True:
        print("1: Single Player Game")
        print("2: Multiplayer Game")
        print("3: Rules\n")
        user_choice = input("Enter choice: ")

        if(validate_choice(user_choice)):
            if int(user_choice) == 1:
                os.system('clear')
                start_game()
            elif int(user_choice) == 2:
                high_scores()
                os.system('clear')
            break


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


def high_scores():
    """
    """
    print("Stagnating")


def start_game():
    """
    """
    board = []
    board_rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    board.append([' ', '1', '2', '3', '4', '5', '6', '7', '8'])
    for x in range(0, 8):
        board.append([board_rows[x], "-", "-", "-", "-", "-", "-", "-", "-"])

    def print_board(board):
        for i in board:
            print(" ".join(i))

    print_board(board)
    print("\n")

    ask_for_choices(board)


def ask_for_choices(board):
    """
    """
    attempts = 10

    # Generating computer ship
    verti_or_hori = randint(1, 2)
    ship = generate_computer_ship(verti_or_hori)
    print(ship)

    while True:
        print(f"Attempts left: {attempts}")

        guess_row = input("Guess a row: ")
        guess_col = input("Guess a column: ")
        print("\n")

        if attempts == 1:
            os.system('clear')
            print("Game Over")
            break

        # if validate_data(guess_row, guess_col, board):
        if guess_row in ship:
            if int(ship[guess_row]) == int(guess_col):
                os.system('clear')
                print("You hit the ship!")
                break
            else:
                os.system('clear')
                attempts -= 1
                update_board(board, guess_row, guess_col)
        else:
            os.system('clear')
            attempts -= 1
            update_board(board, guess_row, guess_col)

        # else:
        #     if board[int(guess_row)][int(guess_col)] == "X":
        #         os.system('clear')
        #         print("This point has already been guessed")
        #         add_board(board)


def generate_computer_ship(vertical_horizontal):
    """
    """

    ship_lenght = randint(2, 4)

    if vertical_horizontal == 1:
        max_letter = chr(ord('I') - ship_lenght)
        random_row = chr(randint(ord('A'), ord(max_letter)))
        column = randint(1, 8)

        vert_ship = {}
        for i in range(ship_lenght):
            key = chr(ord(random_row) + i)
            vert_ship.update({key: column})

        return vert_ship
    elif vertical_horizontal == 2:
        hori_row = chr(randint(ord('A'), ord('H')))
        hori_col = randint(1, (8-ship_lenght))

        hori_ship = {}
        for i in range(ship_lenght):
            value = hori_col + i
            hori_ship.update({hori_row: value})

        return hori_ship


def validate_data(guess_row, guess_col, board):
    """
    """
    try:
        test_int = isinstance(guess_col, int)
        test_str = isinstance(guess_row, str)
        print(test_int, test_str)
        if int(guess_col) > 9:
            raise ValueError("out of bounds")
        elif not test_str or not test_int:
            raise ValueError("invalid input")
    except ValueError as e:
        os.system('clear')
        print(f"Invalid data: {e}, row must be letter, column must be number")
        print(input("Press any key to continue"))
        os.system('clear')
        add_board(board)
        return False
    return True


def update_board(board, guess_row, guess_col):
    """
    """
    for i in board:
        if i[0] == guess_row:
            i[int(guess_col)] = "x"
    for i in board:
        print(" ".join(i))
    print("\n")
    print("You missed the ship")


def add_board(board):
    """
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
