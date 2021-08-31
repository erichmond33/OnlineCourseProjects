"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Vairble to count how many Xs or Os are on the board
    counter = 0
    # Looping the board to see if each position is an X/O/Empty
    for column in board:
        for row in column:
            # Adding one to the counter if it is X/O
            if (row == "O") or (row == "X"):
                counter += 1
    # Checking whether counter is even or odd
    mod = counter % 2
    # If mod is even it is X's turn, or if it is odd then it is O's turn
    if mod == 0:
        return "X"
    else:
        return "O"



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # An empty set to hold the actions
    actions = set()
    # Looping the board to see if each position is an X/O/Empty
    for column in range(3):
        for row in range(3):
            # Adding to actions if postion is empty
            if board[column][row] == None:
                actions.add((column, row))
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Copying the board
    board_copy = copy.deepcopy(board)
    # Splitting the action into row and column
    i = int(action[1])
    j = int(action[0])
    # Applying the move to the board
    board_copy[j][i] = player(board_copy)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # A list of all the possible winning positions
    possible_wins = [[board[0][0], board[0][1], board[0][2]], [board[1][0], board[1][1], board[1][2]], [board[2][0], board[2][1], board[2][2]], [board[0][0], board[1][0], board[2][0]], [board[0][1], board[1][1], board[2][1]], [board[0][2], board[1][2], board[2][2]], [board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]
    # Looping over each position to see if X or O won
    for win in possible_wins:
        if win[0] == "X" and win[1] == "X" and win[2] == "X":
            return "X"
        elif win[0] == "O" and win[1] == "O" and win[2] == "O":
            return "O"
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Checking for any winners
    if winner(board) != None:
        return True

    # Looping the board to see if each position is an X/O/Empty
    for column in board:
        for row in column:
            # If there are any empty spaces we know the game isn't terminal
            if (row == None):
                return False
    # If there are no empty spaces the game is terminal
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Using winner to determine what utility should output
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Making sure the game is't over
    if terminal(board) == True:
        return None
    # Vairble to hold the best action, and "neg/pos" iffinty vairbles
    optimal_action = ()

    min_v = 5
    max_v = -5
    # Looping over each action
    for action in actions(board):
        # If the player is O, then find the minimum value action
        if player(board) == "O":
            min_s = (max_value(result(board, action)))
            if min_s < min_v:
                min_v = min_s
                optimal_action = action
        # If the player is X, then find the maximum value action
        elif player(board) == "X":
            max_s = (min_value(result(board, action)))
            if max_s > max_v:
                max_v = max_s
                optimal_action = action

    return optimal_action
    

def max_value(board):
    # Checking if the state is terminal
    if terminal(board) == True:
        return utility(board)
    # Neg iffinity vairble
    v = -5
    # Recursivly calling min value to get the maximum choice 
    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v

def min_value(board):
    # Checking if the state is terminal
    if terminal(board) == True:
        return utility(board)
    # Pos iffinity
    v = 5
    # Recursivley calling the max value to get the minimum value
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v




