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
        board.append([board_rows[x], "o", "o", "o", "o", "o", "o", "o", "o"])

    def print_board(board):
        for i in board:
            print(" ".join(i))

    print_board(board)
    print("\n")

    ask_for_choices(board)


def generate_computer_ship():
    """
    """
    # dict_board = {
    #     "A": [1, 2, 3, 4, 5, 6, 7, 8],
    #     "B": [1, 2, 3, 4, 5, 6, 7, 8],
    #     "C": [1, 2, 3, 4, 5, 6, 7, 8],
    #     "D": [1, 2, 3, 4, 5, 6, 7, 8],
    #     "E": [1, 2, 3, 4, 5, 6, 7, 8],
    #     "F": [1, 2, 3, 4, 5, 6, 7, 8],
    #     "G": [1, 2, 3, 4, 5, 6, 7, 8],
    #     "H": [1, 2, 3, 4, 5, 6, 7, 8]
    # }

    vertical_horizontal = randint(1, 2)

    ship_lenght = randint(1, 3)

    if vertical_horizontal == 1:
        row_max_letter = chr(ord('I') - ship_lenght)
        vert_row = chr(randint(ord('A'), ord(row_max_letter)))
        column = randint(1, 8)

        vert_rows = []
        for i in range(ship_lenght):
            vert_rows.append(chr(ord(vert_row) + i))

        return [vert_rows, column]
    elif vertical_horizontal == 2:
        hor_row = chr(randint(ord('A'), ord('H')))
        hor_col = randint(1, (8-ship_lenght))

        hor_cols = []
        for i in range(ship_lenght):
            hor_cols.append(hor_col + i)

        return hor_row, hor_cols


def ask_for_choices(board):
    """
    """
    attemps = 10
    computer_choice = generate_computer_ship()
    print(computer_choice)

    while True:
        print(f"Attempts left: {attemps}")

        guess_row = input("Guess a row: ")
        guess_col = input("Guess a column: ")
        print("\n")

        print(guess_col)

        print(guess_row in computer_choice[0])
        print(int(guess_col) in computer_choice)

        # if validate_data(guess_row, guess_col, board):
        if attemps == 1:
            os.system('clear')
            print("Game Over")
            break
        elif (guess_row in computer_choice[0] and
                int(guess_col) in computer_choice):
            os.system('clear')
            print("Nice! You hit the ship!")
            break
        # else:
        #     # if board[int(guess_row)][int(guess_col)] == "X":
        #     #     os.system('clear')
        #     #     print("This point has already been guessed")
        #     #     add_board(board)
        #     # else:
        #     # os.system('clear')
        #     # print("You missed the ship")
        #     # attemps -= 1
        #     # update_board(board, guess_row, guess_col)


def validate_data(guess_row, guess_col, board):
    """
    """
    try:
        int(guess_col)
        guess_row.lower()
        if int(guess_col) > 9:
            raise ValueError("out of bounds")
        elif not isinstance(guess_row, str):
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
        if guess_row in board[i]:
            board[i][guess_col] = "x"
    # board[int(guess_row)][int(guess_col)] = "X"
    for i in board:
        print(" ".join(i))
    print("\n")


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

