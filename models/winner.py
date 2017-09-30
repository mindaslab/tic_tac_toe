from data.constants import *

class Winner:
    def who(board):
        for player in PLAYERS:
            for i in range(3):
                if (board.row(i).count(player) == 3):
                    return player
                if (board.col(i).count(player) == 3):
                    return player
            if (board.diagnol().count(player) == 3):
                return player
            if (board.anti_diagnol().count(player) == 3):
                return player
        return False
