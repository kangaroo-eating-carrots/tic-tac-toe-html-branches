import unittest
from game_player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(mark="X")
        self.choices = []

    # tests if the player puts the choice on the right index position on the 2d
    def test_make_choice(self):
        self.player.make_choice(2, 3)
        self.assertEqual(self.player.choices, [[0,2]])

