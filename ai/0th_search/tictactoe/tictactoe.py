"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
from random import shuffle

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

    # Return X if number of empty spots is odd else O
    num_empty = sum(row.count(EMPTY) for row in board)
    return X if num_empty % 2 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Iterate through nested loop to find which spots are EMPTY
    return {(index1, index2) for index1, value1 in enumerate(board) for index2, value2 in enumerate(value1) if value2 == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Find who's turn it is
    turn = player(board)

    # Verify action is a valid entry
    for i in action:
        if i not in range(len(board)):
            raise Exception("Invalid action")

    # Duplicate board and insert new value
    new_board = deepcopy(board)
    if new_board[action[0]][action[1]] == EMPTY:
        new_board[action[0]][action[1]] = turn
    else:
        raise Exception("Invalid action")

    # Return modified board
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Horizontal win
    for row in board:
        if len(set(row)) == 1 and row[0] != EMPTY:
            return row[0]

    # Vertical win
    transpose = list(map(list, zip(*board)))
    for row in transpose:
        if len(set(row)) == 1 and row[0] != EMPTY:
            return row[0]

    # Diagonal win
    if len(set(row[i] for i, row in enumerate(board))) == 1 and board[0][0] != EMPTY:
        return board[0][0]
    elif len(set(row[-(i+1)] for i, row in enumerate(board))) == 1 and board[0][-1] != EMPTY:
        return board[0][-1]

    # No winner
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is None and actions(board):
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        _, action = maxvalue(board, float('-inf'), float('inf'))
    elif player(board) == O:
        _, action = minvalue(board, float('-inf'), float('inf'))
    else:
        return None

    return action


def maxvalue(board, alpha, beta):
    if terminal(board):
        return utility(board), None

    list_action = list(actions(board))
    shuffle(list_action)

    for count, action in enumerate(list_action):
        new_v, _ = minvalue(result(board, action), alpha, beta)

        if count < 1 or v < new_v:
            v = new_v
            best_act = action

        alpha = max(v, alpha)

        if beta <= alpha:
            break

    return v, best_act


def minvalue(board, alpha, beta):
    if terminal(board):
        return utility(board), None

    list_action = list(actions(board))
    shuffle(list_action)

    for count, action in enumerate(list_action):
        new_v, _ = maxvalue(result(board, action), alpha, beta)

        if count < 1 or v > new_v:
            v = new_v
            best_act = action

        beta = min(v, beta)
        if beta <= alpha:
            break

    return v, best_act
