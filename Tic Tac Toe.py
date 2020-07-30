import random as rd
from random import randint


def display_board(board):
    """
    This will display the tic_tac_toe board
    """
    print('\t\t|\t\t|\t\n\t' + board[1] + '\t|\t' + board[2] + '\t|\t' + board[3] + '\n\t\t|\t\t|\t')
    print('--------------------------')
    print('\t\t|\t\t|\t\n\t' + board[4] + '\t|\t' + board[5] + '\t|\t' + board[6] + '\n\t\t|\t\t|\t')
    print('--------------------------')
    print('\t\t|\t\t|\t\n\t' + board[7] + '\t|\t' + board[8] + '\t|\t' + board[9] + '\n\t\t|\t\t|\t')


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']


def player_input():
    """
    Takes in player input and assigns their
    marker as X or O.
    """
    marker = "wrong"

    while marker not in ['X', 'O']:

        marker = input("Please choose your marker X/O: ")

        if marker not in ['X', 'O']:
            print('\n' * 100)
            print("Sorry, use either X or O!")

    if marker == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]


def place_marker(board, marker, position):
    """
    Takes in board list object, a marker, desired
    position (1-9) and assigns it to the board.
    """
    board[position] = marker


def win_check(board, mark):
    """
    Checks for winner.
    """
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True


def player_order():
    """
    Decides first opportunity of a player randomly.
    """
    player_choice = rd.randint(0, 1)

    if player_choice == 0:
        return "Player 1"
    else:
        return "Player 2"


def space_finder(board, position):
    """
    Checks for spaces on the game board.
    """
    if board[position].isspace():
        return True
    else:
        return False


def board_full_check(board):
    """
    To check if the board is full and returns a boolean
    value.True if full, false otherwise.
    """
    for i in board:
        # Checks if all the boxes are full
        if i.isspace() == 0:
            return True
        else:
            return False


def players_next_move(board):
    """
    This function determines players next choice of
    position (1-9) and returns the position for marker.
    """
    # FOR STARTING A WHILE LOOP
    position = 0

    # CHECKS IF POSITION IS B/W 1-9 AND THOSE POSITIONS ARE EMPTY
    while position not in range(1, 10) and space_finder(board, position):

        position = int(input("Enter any position for marker (1-9): "))

    return position


def keep_playing():
    """
    Checks if players want to continue playing or quit,
    returns a boolean value
    """

    replay = input("Do you want to keep playing ? Y/N: ")

    while replay in ["Y", "N"]:

        if replay == "Y":
            return True
        elif replay == "N":
            print("See ya!")
            break


# SETTING UP GAME LOGIC

print("WELCOME TO TIC TAC TOE")
print("*" * 22)
print("\t\tRULES:\n1.Let any player choose a marker\n2.system randomly decides player 1/2")
print("3.Players take turns in putting marker")

while True:
    # DISPLAY FRESH TIC TAC TOE BOARD
    new_board = [' '] * 10
    display_board(new_board)

    # ALLOW PLAYERS CHOOSE MARKER
    player1_marker, player2_marker = player_input()

    # SET A PLAYER ORDER, PLAYER 1/PLAYER 2 GOES FIRST
    turn = player_order()
    print(f"{turn} goes first")

    # GAME ON CHOICE
    game_on = input("Do you wish to continue? Y/N: ").upper()

    if game_on == "Y":
        start_game = True
    else:
        print("Ready when you are!")
        start_game = False

    while start_game:

        if turn == "Player 1":

            # TURN FOR PLAYER 1
            # DISPLAYS BOARD TAKES IN POSITION AND ENTERS MARKER THERE
            display_board(new_board)
            position = players_next_move(new_board)
            place_marker(new_board, player1_marker, position)

            # CHECKS FOR WINNING COMBINATION OF MARKERS
            # DISPLAYS FINAL BOARD AND PRINTS A MESSAGE
            # ASKS FOR 'keep_playing' FUNCTION
            if win_check(new_board, player1_marker):
                display_board(new_board)
                print(f"Hurrah {turn} won!")
                start_game = False

            # CHECKS IF BOARD IS FULL FOR A DRAW MATCH
            elif board_full_check(new_board):
                display_board(new_board)
                print("Match drawn, don't give up!")
                break
            else:
                turn = "Player 2"

        if turn == "Player 2":

            # TURN FOR PLAYER 2
            # DISPLAYS BOARD TAKES IN POSITION AND ENTERS MARKER THERE
            display_board(new_board)
            position = players_next_move(new_board)
            place_marker(new_board, player2_marker, position)

            # CHECKS FOR WINNING COMBINATION OF MARKERS
            # DISPLAYS FINAL BOARD AND PRINTS A MESSAGE
            # ASKS FOR 'keep_playing' FUNCTION
            if win_check(new_board, player2_marker):
                display_board(new_board)
                print(f"Hurrah {turn} won!")
                start_game = False

            # CHECKS IF BOARD IS FULL AND MATCH DRAWN
            elif board_full_check(new_board):
                display_board(new_board)
                print("Match drawn")
                break
            else:
                turn = "Player 1"

    # STOPS GAME AND BREAKS FROM WHILE LOOP
    if not keep_playing():
        break
