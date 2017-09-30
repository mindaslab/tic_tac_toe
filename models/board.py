class Board:

    def __init__(self):
        self.positions = "123456789"

    def __str__(self):
        string = ""
        for i in range(3):
            string = string + self.row(i) + "\n"
        return string

    """
    Fectches nth row
    """
    def row(self, row_number):
        start = row_number * 3
        end = start + 3
        return self.positions[start:end]

    """
    Fectches nth col
    """
    def col(self, col_number):
        string = ""
        for i in range(3):
            string = string + self.row(i)[col_number]
        return string

    def diagnol(self):
        string = ""
        for i in range(3):
            string = string + self.row(i)[i]
        return string

    def anti_diagnol(self):
        string = ""
        for i in range(3):
            string = string + self.row(2 - i)[i]
        return string

    def play(self, position, character):
        self.positions = self.positions.replace(str(position), character)
