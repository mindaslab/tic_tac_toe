import re

class Winner:
    def who(board, players=['X', 'O']):
        for player in players:
            for i in range(3):
                if (board.row(i).count(player) == 3):
                    return player
                if (board.col(i).count(player) == 3):
                    return player
            if (board.diagnol().count(player) == 3):
                return player
            if (board.anti_diagnol().count(player) == 3):
                return player
        p = re.compile('\d')
        if (not len(p.findall(board.positions))):
            return "None"
        return False
