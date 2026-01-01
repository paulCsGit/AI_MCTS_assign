# main.py

from game import GameState
from mcts import MCTS

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

if __name__ == "__main__":
    state = GameState()
    mcts = MCTS(state)

    best_node = mcts.run(iterations=2000)

    print("Best move chosen by MCTS:")
    print_board(best_node.state.board)

