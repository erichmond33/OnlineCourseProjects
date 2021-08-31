from tictactoe import initial_state, player,actions, result, winner, terminal,utility, minimax, min_value, max_value
import math
import copy


X = "X"
O = "O"
EMPTY = None

custom_board = [[X, X, None],
                [None, None, O], 
                [None, None, None ]]

board2 = [[X, None, X],
            [None, None, None], 
            [O, None, O ]]

board3 = [[X, None, X], 
            [None, None, None], 
            [None, None, O]]


b = copy.deepcopy(custom_board)
#print(b)

#print(min_value(board2))

#print(max_value(board2))

print(minimax(board3))