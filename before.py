from math import inf
import sys, os

HUMAN = 1
COMP = -1

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

MSG = "Welcome to Unbeatable Tic Tac Toe.\n" \
        "Our A.I can foreseen your moves ahead.\n" \
        "Are you sure to continue ? (y/n)"


def evaluate(state):
    """
    Perform heuristic evaluation from board.
    Heuristic - allow the computer to discover the solution
    of some problems by itself.
    """

def empty_cells(state):
    """Extract the remainder of board"""

def wins(state, player):
    """
    Contains all winning condition,
    players are win for sure if their symbols (X or O) are
    placed in 3 consecutive lines (horizontal, vertical or diagonal)
    example:

    Three in a row      Three in a diagonal     Three in a col
        [X, X, X]           [O,  ,  ]               [O, X, X]
        [ , O, O]           [X, O,  ]               [O, X,  ]
        [ ,  ,  ]           [X,  , O]               [O,  ,  ]

    """
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]


def game_over(state):
    """Check game over condition"""

def clean():
    """Clear system terminal"""

def minimax(state, depth, player):
    """
    Minimax implementation for computer moves,
    it recursively traverse the tree to search the
    best possible moves to hinder other players winning move.
    :return list of [best_row, best_col, best_score]
    """


def human_turn(state):
    # All possible moves
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }


def ai_turn(state):
    pass

def render(state):
    """Render the board state to stdout"""

def main():
    """Main function: Function that will running at start"""


if __name__ == '__main__':
    main()
