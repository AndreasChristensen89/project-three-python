from random import randint


def main_menu():
    while True:
        print("1: Single Player Game")
        print("2: Multiplayer Game\n")
        user_choice = int(input("Enter choice: "))

        if(user_choice == 1 or user_choice == 2):
            break
        else:
            print("Value must be 1 or 2, please try again")

    if user_choice == 1:
        start_game()
    elif user_choice == 2:
        high_scores()


def high_scores():
    print("Stagnating")


def start_game():
    print("\n")
    board = []
    for x in range(0, 5):
        board.append(["O"] * 5)

    def print_board(board):
        for i in board:
            print(" ".join(i))

    print("Board")
    print_board(board)
    print("\n")

    ask_for_choices(board)


def ask_for_choices(board):
    attemps_left = 4

    while True:
        comp_row = randint(0, len(board) - 1)
        comp_col = randint(0, len(board[0]) - 1)

        print(f"Attempts left: {attemps_left}")
        print(comp_row)
        print(comp_col)

        guess_row = int(input("Guess a row: "))
        guess_col = int(input("Guess a column: "))

        if attemps_left == 0:
            print("Game Over")
            break
        elif guess_row == comp_row and guess_col == comp_col:
            print("Congratulations! You sunk the ship!")
            break
        else:
            if guess_row > 5 or guess_col > 5:
                print("Guess is out of bounds")
            elif board[guess_row][guess_col] == "X":
                print("This has already been guessed")
            else:
                print("You missed the ship")
                attemps_left -= 1
                update_board(board, guess_row, guess_col)


def update_board(board, guess_row, guess_col):
    board[guess_row][guess_col] = "X"
    for i in board:
        print(" ".join(i))


def main():
    """
    Main function to set in motion the other functions
    """
    main_menu()


print("Welcome to Battleships")
main()
