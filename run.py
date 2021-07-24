from random import randint
import os


def main_menu():
    while True:
        print("1: Single Player Game")
        print("2: Multiplayer Game")
        print("3: Rules\n")
        user_choice = int(input("Enter choice: "))

        if(user_choice == 1 or user_choice == 2):
            break
        else:
            print("Value must be 1 or 2, please try again")

    if user_choice == 1:
        os.system('clear')
        start_game()
    elif user_choice == 2:
        high_scores()
        os.system('clear')


def high_scores():
    print("Stagnating")


def start_game():
    board = []
    for x in range(0, 5):
        board.append(["O"] * 5)

    def print_board(board):
        for i in board:
            print(" ".join(i))

    print("Good Luck!")
    print_board(board)
    print("\n")

    ask_for_choices(board)


def ask_for_choices(board):
    attemps = 5
    comp_row = randint(0, len(board) - 1)
    comp_col = randint(0, len(board[0]) - 1)

    while True:
        print(f"Attempts left: {attemps}")
        # print(comp_row)
        # print(comp_col)

        guess_row = input("Guess a row: ")
        guess_col = input("Guess a column: ")
        print("\n")

        if validate_data(guess_row, guess_col, board):
            if attemps == 1:
                os.system('clear')
                print("Game Over")
                break
            elif int(guess_row) == comp_row and int(guess_col) == comp_col:
                os.system('clear')
                print("Congratulations! You sunk the ship!")
                break
            else:
                if board[int(guess_row)][int(guess_col)] == "X":
                    os.system('clear')
                    print("This point has already been guessed")
                    add_board(board)
                else:
                    os.system('clear')
                    print("You missed the ship")
                    attemps -= 1
                    update_board(board, guess_row, guess_col)


def validate_data(guess_row, guess_col, board):
    try:
        int(guess_col)
        int(guess_row)
        if int(guess_row) > 4 or int(guess_col) > 4:
            raise ValueError("out of bounds")
    except ValueError as e:
        os.system('clear')
        print(f"Invalid data: {e}, input must be numbers within range")
        print(input("Press any key to continue"))
        os.system('clear')
        add_board(board)
        return False
    return True


def update_board(board, guess_row, guess_col):
    board[int(guess_row)][int(guess_col)] = "X"
    for i in board:
        print(" ".join(i))
    print("\n")


def add_board(board):
    print("board")
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
