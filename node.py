# node.py

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0.0
        self.untried_moves = state.legal_moves()

    def fully_expanded(self):
        return len(self.untried_moves) == 0

