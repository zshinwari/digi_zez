def player_choice(board_list):
    while True:
        try:
            number_choice = int(input("Enter value between 1-9: "))
            if number_choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print("Enter value between 0-9")
                continue
            if not space_check(number_choice, board_list):
                print("Chosen space has been taken, please try again.")
                continue
            else:
                return number_choice
        except ValueError:
             print("Enter a number between 1-9")


def display_board(board_list):
    x = f"""
    -------------
    | {board_list[0]} | {board_list[1]} | {board_list[2]} |
    -------------
    | {board_list[3]} | {board_list[4]} | {board_list[5]} |
    -------------
    | {board_list[6]} | {board_list[7]} | {board_list[8]} |
    -------------
    """
    print(x)

def player_input():
    while True:
        input_marker = input("Please pick a marker 'x' or 'o'").lower()
        if input_marker not in ['x', 'o']:
            print("Invalid input, please try agian.")
            continue
        else:
            marker = input_marker
            break
    return marker


def place_marker(board_list, player_input, player_choice):
    player_choice = player_choice -1
    try:
        if board_list[player_choice] != " ":
            print("Chosen space has been taken, please try again.")
        else:
            board_list[player_choice] = player_input
    except IndexError:
        print("list index out of range, please enter value between 1-9")
    return display_board(board_list)

def win_check(board_list, mark):
    if board_list[0] == mark and board_list[1] == mark and board_list[2] == mark:
        result = 'win'
        return result
    elif board_list[3] == mark and board_list[4] == mark and board_list[5] == mark:
        result = 'win'
        return result
    elif board_list[6] == mark and board_list[7] == mark and board_list[8] == mark:
        result = 'win'
        return result
    elif board_list[0] == mark and board_list[3] == mark and board_list[6] == mark:
        result = 'win'
        return result
    elif board_list[1] == mark and board_list[4] == mark and board_list[7] == mark:
        result = 'win'
        return result
    elif board_list[2] == mark and board_list[5] == mark and board_list[8] == mark:
        result = 'win'
        return result
    elif board_list[0] == mark and board_list[4] == mark and board_list[8] == mark:
        result = 'win'
        return result
    elif board_list[1] == mark and board_list[4] == mark and board_list[6] == mark:
        result = 'win'
        return result
    elif board_list[2] == mark and board_list[4] == mark and board_list[6] == mark:
        result = 'win'
        return result
    else:
        result = 'lost'
        return result

import random
def choose_first():
    chosen = random.randint(1,2)
    return chosen

def space_check(position, board_list):
    position = position - 1
    if position > len(board_list):
        print("list index out of range, please enter value between 1-9")
    elif board_list[position] != " ":
        return False
    else:
        return True

def full_board_check(board_list):
    for i in range(len(board_list)):
        if board_list[i] == ' ':
            return False
        else:
            result = True
    return result


def replay():
    while True:
        input_answer = input("Would you like to play Tic Tac Toe game? Enter Yes or No:  ").lower()
        if input_answer not in ['y', 'n']:
            print("Invalid input, please enter 'Y' or 'N'.")
            continue
        if input_answer == 'y':
            return True
        else:
            return False


board_list = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " "]
display_board(board_list)
player = choose_first()
print(f"Welcome to Tic Tac Toe!")

while True:
    p_one_input = player_input()
    # game_on = replay()
    while True:
        player_one = 'Player 1' if player == 1 else 'Player 2'
        print(f"{player_one} goes next")
        p_one_choice = player_choice(board_list)
        place_marker(board_list, p_one_input, p_one_choice)
        if win_check(board_list, p_one_input) == 'win':
            print("You won the game!")
            break
        x = full_board_check(board_list)
        if x:
            print("Draw!")
            break
        player_two = 'Player 2' if player_one == 1 else 'Player 1'
        print(f"{player_two} goes next")
        p_two_input = 'x' if p_one_input == 'o' else 'o'
        p_two_choice = player_choice(board_list)
        place_marker(board_list, p_two_input, p_two_choice)
        if win_check(board_list, p_two_input) == 'win':
            print("You won the game!")
            break
        if full_board_check(board_list):
            print("Draw!")
            break

    if not replay():
        break
    else:
        board_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]





