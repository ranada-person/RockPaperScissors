import random

# ROCK PAPER SCISSORS MINI GAME
# RANADA PERSON
# 3.17.2022
# USER SELECTS THEIR MOVE AND PROGRAM WILL DETERMINE IF THEY WIN OR LOSE AGAINST RANDOM COMPUTER SELECTION


def display_menu():
    # DISPLAY MENU AND COLLECT USER'S SELECTION
    print("Make your selection: ")
    print("1: Rock")
    print("2: Paper")
    print("3: Scissors")
    return int(input())


def computer_selection():
    # RANDOMIZE COMPUTER'S SELECTION 1, 2, OR 3
    return random.randint(1, 3)


def determine_winner(user_move, computer_move):
    # DETERMINE WHO WINS
    if selection == computer_selection:
        print("TIE GAME")
    elif (selection == 1) & (computer_selection == 2):
        print("Paper covers Rock: You Lose :(")
    elif (selection == 1) & (computer_selection == 3):
        print("Rock Smashes Scissors: You Win!!")
    elif (selection == 2) & (computer_selection == 1):
        print("Paper covers Rock: You Win!!")
    elif (selection == 2) & (computer_selection == 3):
        print("Scissors Cut Paper: You Lose :(")
    elif (selection == 3) & (computer_selection == 1):
        print("Rock Smashes Scissors: You Lose :(")
    elif (selection == 3) & (computer_selection == 2):
        print("Scissors Cut Paper: You Win!!")
    else:
        print("ERROR")


def display_words(choice):
    # DISPLAY THE WORDS ROCK, PAPER, OR SCISSORS FOR SELECTION
    choice = choice
    if choice == 1:
        return "Rock"
    elif choice == 2:
        return "Paper"
    else:
        return "Scissors"


# MAIN
if __name__ == '__main__':
    selection = display_menu()
    computer_selection = computer_selection()
    print("You Selected " + display_words(selection) +
          " and the computer selected " + display_words(computer_selection))
    determine_winner(selection, computer_selection)




