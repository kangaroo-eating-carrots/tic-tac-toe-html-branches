import unittest
from game_setting import Game_Setting

class TestLogic(unittest.TestCase):
    def setUp(self):
        self.game_setting = Game_Setting(board_width=3,winning_line=3)

    #TESTS ALL WINNING CONDITIONS
    def test_winning_conditions(self):
        expected_row_winning_conditions = [[[0, 0], [0, 1], [0, 2]],
                                           [[1, 0], [1, 1], [1, 2]],
                                           [[2, 0], [2, 1], [2, 2]],
                                           [[0, 0], [1, 0], [2, 0]],
                                           [[0, 1], [1, 1], [2, 1]],
                                           [[0, 2], [1, 2], [2, 2]],
                                           [[0, 0], [1, 1], [2, 2]],
                                           [[0, 2], [1, 1], [2, 0]]]

        self.assertEqual(self.game_setting.winning_conditions,expected_row_winning_conditions)