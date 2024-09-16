class Player:
    def __init__(self, mark):
        self.mark = mark
        self.choices = []

    def make_choice(self, index, width):
        index_2d = [index//width, index % width]
        self.choices.append(index_2d)

class Game_Setting:
    def __init__(self, board_width, winning_line):
        self.board_width = board_width
        self.board_size = self.board_width * self.board_width
        self.board = [' '] * self.board_size
        self.winning_line = winning_line
        self.player_marks = ['X', 'O', '△']

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

class Game_Play:
    def __init__(self, board_width, winning_line):
        self.board_width = board_width
        self.winning_line = winning_line
        self.setting = Game_Setting(self.board_width, self.winning_line)
        self.player1 = Player(self.setting.player_marks[0])
        self.player2 = Player(self.setting.player_marks[1])
        self.current_player = self.player1
        self.put_counter = 0


    def check_winner(self):
        for wc in self.setting.winning_conditions:
            match_count = 0
            for choice in self.player1.choices:
                if choice in wc:
                    match_count += 1
            if match_count == self.winning_line:
                return self.player1.mark

            match_count = 0
            for choice in self.player2.choices:
                if choice in wc:
                    match_count += 1
            if match_count == self.winning_line:
                return self.player2.mark
        return None

    def check_draw(self):
        return ' ' not in self.setting.board

    def do_continue(self):
        draw = self.check_draw()
        winner = self.check_winner()

        if draw or winner is not None:
            return False

        return True