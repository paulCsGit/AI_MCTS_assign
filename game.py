# game.py

class GameState:
    def __init__(self, board=None, player='X'):
        self.board = board if board is not None else [' '] * 9
        self.player = player

    def legal_moves(self):
        return [i for i in range(9) if self.board[i] == ' ']

    def is_terminal(self):
        wins = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]

        for a, b, c in wins:
            if self.board[a] != ' ' and \
               self.board[a] == self.board[b] == self.board[c]:
                return True

        return len(self.legal_moves()) == 0

    def winner(self):
        wins = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]

        for a, b, c in wins:
            if self.board[a] != ' ' and \
               self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]

        return ' '

    def next_state(self, move):
        new_board = self.board.copy()
        new_board[move] = self.player
        next_player = 'O' if self.player == 'X' else 'X'
        return GameState(new_board, next_player)

