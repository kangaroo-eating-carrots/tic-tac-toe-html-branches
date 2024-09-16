from game_logic import Game_Setting
from game_player import Player

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