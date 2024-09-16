class Game_Setting:
    def __init__(self, board_width, winning_line):
        self.board_width = board_width
        self.board_size = self.board_width * self.board_width
        self.board = [' '] * self.board_size
        self.winning_line = winning_line
        self.player_marks = ['X', 'O']

    @property
    def winning_conditions(self):
        winning_conditions = []

        for i in range(self.board_width):
            for j in range(self.board_width - self.winning_line + 1):
                winning_condition = []
                for k in range(self.winning_line):
                    elem = [i, j + k]
                    winning_condition.append(elem)
                winning_conditions.append(winning_condition)

        for i in range(self.board_width - self.winning_line + 1):
            for j in range(self.board_width):
                winning_condition = []
                for k in range(self.winning_line):
                    elem = [i + k, j]
                    winning_condition.append(elem)
                winning_conditions.append(winning_condition)

        for i in range(self.board_width - self.winning_line + 1):
            for j in range(self.board_width - self.winning_line + 1):
                winning_condition = []
                for k in range(self.winning_line):
                    elem = [i + k, j + k]
                    winning_condition.append(elem)
                winning_conditions.append(winning_condition)

        for i in range(self.board_width - self.winning_line + 1):
            for j in range(self.board_width - self.winning_line + 1):
                winning_condition = []
                for k in range(self.winning_line):
                    elem = [i + k, j + self.winning_line - k - 1]
                    winning_condition.append(elem)
                winning_conditions.append(winning_condition)

        return winning_conditions