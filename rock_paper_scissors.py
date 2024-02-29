import random


def use_rock(move="Rock"):
    """ Initializing player move "Rock" """
    return move


def use_paper(move="Paper"):
    """ Initializing player move "Paper" """
    return move


def use_scissors(move="Scissors"):
    """ Initializing player move "Scissors" """
    return move


def player_move(move):
    """ Creating player's attempt """
    attempt_is_valid = False

    if move == "r":
        attempt_is_valid = True
        move = use_rock()
    elif move == "p":
        attempt_is_valid = True
        move = use_paper()
    elif move == "s":
        attempt_is_valid = True
        move = use_scissors()

    if attempt_is_valid:
        return move
    else:
        return "Invalid Input. Try again..."


def computer_move():
    """ Initializing computer's move """
    move = random.randint(1, 3)

    if move == 1:
        move = use_rock()
    elif move == 2:
        move = use_paper()
    elif move == 3:
        move = use_scissors()

    return move


def game_of_rock_paper_scissors():
    """ Initializing the game output """
    player_input = input("Choose: [r]ock, [p]aper, [s]cissors: ")
    result_player = player_move(player_input)
    result_computer = computer_move()
    if result_player == "Invalid Input. Try again...":
        print(result_player)
        raise SystemExit
    else:
        print(f"You chose {result_player}")
        print(f"Computer chose {result_computer}")
        if (result_player == "Rock" and result_computer == "Scissors") or \
                (result_player == "Paper" and result_computer == "Rock") or \
                (result_player == "Scissors" and result_computer == "Paper"):
            print("You win!")
        elif result_player == result_computer:
            print("Draw!")
        else:
            print("You lose!")


# Starting the game
game_of_rock_paper_scissors()





