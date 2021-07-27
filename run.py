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
    ship = generate_computer_ship(2)
    print(ship)
    hit_count = []

    while True:
        if attempts == 1:
            os.system('clear')
            print("Game Over")
            break
        elif sorted(hit_count) == sorted(ship):
            os.system('clear')
            print("Congratulations! You sank the battleship")
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
    """
    vertical_horizontal = randint(1, 2)

    ship_points = []

    ship_count = 0

    if vertical_horizontal == 1:
        while True:
            ship_lenght = randint(2, 4)
            max_letter = chr(ord('I') - ship_lenght)
            random_row = chr(randint(ord('A'), ord(max_letter)))
            char_two = str(randint(1, 8))

            vert_ship = []
            for i in range(ship_lenght):
                char_one = chr(ord(random_row) + i)
                vert_ship.append(char_one+char_two)

            if not any(item in ship_points for item in vert_ship):
                for i in vert_ship:
                    ship_points.append(i)
                ship_count += 1
                if ship_count == number_of_ships:
                    break
    elif vertical_horizontal == 2:
        while True:
            ship_lenght = randint(2, 4)
            char_one = chr(randint(ord('A'), ord('H')))
            hori_col = randint(1, (8-ship_lenght))

            hori_ship = []
            for i in range(ship_lenght):
                char_two = str(hori_col + i)
                hori_ship.append(char_one+char_two)
            if not any(item in ship_points for item in hori_ship):
                for i in hori_ship:
                    ship_points.append(i)
                ship_count += 1
                if ship_count == number_of_ships:
                    break
    return ship_points


def validate_data(guess, board):
    """
    """
    try:
        int(guess[1:2])
        test_str = isinstance(guess[:1], str)
        test_len = len(guess)
        if int(guess[1:2]) > 8 or int(ord(guess[:1].lower())-96) > 8:
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
# list_one = ["A1", "A2", "A3"]
# list_two = ["F5", "G5", "H5"]
# list_three = ["C1", "D1", "E1"]

# guess_list = ["A1", "A2", "F5", "A3", "G5", "H5", "C1", "D1", "E1"]
# print(all(item in guess_list for item in list_one))
# # True
