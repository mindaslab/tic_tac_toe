import re
import copy
from models.winner import Winner

class Agent:
    WEIGHTS = [5, 1, 7, 9, 3, 2, 4, 6, 8 ]

    def __init__(self):
        self.my_symbol = 'X'
        self.opponent_symbol = 'O'
        self.board = None

    def move(self, board):
        self.board = board
        return self.top_move()

    def playable_positions(self):
        positions = self.board.positions
        p = re.compile('\d')
        return [ int(position) for position in p.findall(positions)]

    def top_move(self):
        # try to win if possible
        # try to block if possible
        for symbol in [self.my_symbol, self.opponent_symbol]:
            for position in self.WEIGHTS:
                board_copy = copy.copy(self.board)
                board_copy.play(position, symbol)
                if Winner.who(board_copy):
                    return position

        # play center move if possib;e
        # play diagnol move if possible
        # play some move
        for position in self.WEIGHTS:
            if (self.playable_positions().count(position)):
                return position

        return False
