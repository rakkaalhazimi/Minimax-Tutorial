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
    if wins(state, COMP):
        score = -1
    elif wins(state, HUMAN):
        score = 1
    else:
        score = 0

    return score

def empty_cells(state):
    """Extract the remainder of board"""
    cells = [] # it contains all empty cells

    # Use enumerate for easy indexing
    for i, row in enumerate(state):
        for j, col in enumerate(row):
            if state[i][j] == 0:
                cells.append([i, j])

    return cells

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

    if [player, player, player] in win_state:
        return True
    else:
        return False

def game_over(state):
    """Check game over condition"""
    return wins(state, HUMAN) or wins(state, COMP)

def clean():
    """Clear system terminal"""
    os_name = sys.platform.lower()
    os.system("cls")
    if 'win' in os_name:
        os.system('cls')
    else:
        os.system('clear')

def minimax(state, depth, player):
    """
    Minimax implementation for computer moves,
    it recursively traverse the tree to search the
    best possible moves to hinder other players winning move.
    :return list of [best_row, best_col, best_score]
    """

    if player == COMP:
        best = [-1, -1, inf] # inf/-inf are the initial score for the players
    else:
        best = [-1, -1, -inf]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        # Fill the empty cells with the player symbols
        x, y = cell[0], cell[1]
        state[x][y] = player
        #
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] < best[2]:
                best = score
        else:
            if score[2] > best[2]:
                best = score

    return best

def human_turn(state):
    # All possible moves
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    remain = empty_cells(state)
    isTurn = True
    print("Human Turn")
    while isTurn:
        try:
            move = int(input("Enter your move (1-9) :"))
            # When the player move is valid
            if moves.get(move) in remain:
                x, y = moves.get(move)
                state[x][y] = HUMAN
                isTurn = False

            else: # Otherwise
                print("Bad Move, try again.")

        # When the player mistype
        except ValueError:
            print("Blank space and string are prohibited, please enter (1-9)")

    # While-else loop, this code below will run after successful loop.
    else:
        # Clean the terminal, and show the current board
        clean()
        print(render(state))

def ai_turn(state):
    depth = len(empty_cells(state)) # The remaining of empty cells
    row, col, score = minimax(state, depth, COMP) # the optimal move for computer
    state[row][col] = COMP
    print("A.I Turn")
    print(render(state)) # Show result board

def render(state):
    """Render the board state to stdout"""
    legend = {0: " ", 1: "X", -1: "O"}
    state = list(map(lambda x: [legend[y] for y in x], state))
    result = "{}\n{}\n{}\n".format(*state)
    return result

def main():
    """Main function: Function that will running at start"""
    print(MSG)

    start = False
    while not start:
        confirm = input("")

        if confirm.lower() in ["y", "yes"]:
            start = True
        elif confirm.lower() in ["n", "no"]:
            sys.exit()
        else:
            print("Please enter 'y' or 'n'")

    else:
        clean()
        print("Game is settled !\n")
        print(render(board), end="\n")

    while not wins(board, COMP) and not wins(board, HUMAN):
            human_turn(board)
            if len(empty_cells(board)) == 0: break
            ai_turn(board)

    if wins(board, COMP):
        print("A.I wins, 'I see throught your moves'")
    elif wins(board, HUMAN):
        print("Human wins, 'How can I lose to human ?'")
    else:
        print("It's a Draw. No one wins")


if __name__ == '__main__':
    main()