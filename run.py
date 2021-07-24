# python code goes here
def main_menu():
    while True:
        print("1: Start game")
        print("2: Highscores\n")
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
    print("Stagnating")


def main():
    """
    Main function to set in motion the other functions
    """
    main_menu()


print("Welcome to Battleships")
main()
