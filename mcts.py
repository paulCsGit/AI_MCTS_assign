# mcts.py

import math
import random
from node import Node

class MCTS:
    def __init__(self, root_state):
        self.root = Node(root_state)
        self.C = math.sqrt(2)

    def run(self, iterations):
        for _ in range(iterations):
            node = self.select(self.root)
            result = self.simulate(node.state)
            self.backpropagate(node, result)

        return max(self.root.children, key=lambda c: c.visits)

    def select(self, node):
        while not node.state.is_terminal():
            if not node.fully_expanded():
                return self.expand(node)
            node = self.best_child(node)
        return node

    def expand(self, node):
        move = node.untried_moves.pop()
        next_state = node.state.next_state(move)
        child = Node(next_state, node)
        node.children.append(child)
        return child

    def best_child(self, node):
        return max(
            node.children,
            key=lambda c: self.uct_value(node, c)
        )

    def uct_value(self, parent, child):
        return (
            (child.wins / child.visits) +
            self.C * math.sqrt(math.log(parent.visits) / child.visits)
        )

    def simulate(self, state):
        while not state.is_terminal():
            move = random.choice(state.legal_moves())
            state = state.next_state(move)

        winner = state.winner()
        if winner == 'X':
            return 1.0
        elif winner == 'O':
            return 0.0
        else:
            return 0.5

    def backpropagate(self, node, result):
        while node is not None:
            node.visits += 1
            node.wins += result
            node = node.parent

