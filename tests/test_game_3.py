import unittest
from unittest.mock import patch
from io import StringIO
import json
import random

from health_exception import Health_exception
from hard_mini_games import Hard


class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Hard()

    def test_game3_draw(self):
        computer_choice = 'rock'
        user_input = 'rock'
        expected_output = "Computer chose rock. Draw. let's try again."
        with patch('hard_mini_games.time.sleep'):
            with patch('hard_mini_games.playsound'):
                with patch('sys.stdout', new=StringIO()) as fake_out:
                    with patch('hard_mini_games.random', return_value=computer_choice):
                        with patch('builtins.input', side_effect=user_input):
                            self.game.game3("en", "no")

        self.assertEqual(fake_out.getvalue().strip(), expected_output)

    def test_game3_win(self):
        computer_choice = 'paper'
        user_input = 'scissors'
        expected_output = "Computer chose paper. Congratulations. You win.\nLives have left 10."

        with patch('hard_mini_games.time.sleep'):
            with patch('hard_mini_games.playsound'):
                with patch('sys.stdout', new=StringIO()) as fake_out:
                    with patch('hard_mini_games.random', return_value=computer_choice):
                        with patch('builtins.input', side_effect=user_input):
                            self.game.game3("en", "no")

        self.assertEqual(fake_out.getvalue().strip(), expected_output)

    def test_game3_health_exception(self):
        computer_choice = 'paper'
        user_input = 'rock'

        with self.assertRaises(Health_exception):
            with patch('hard_mini_games.time.sleep'):
                with patch('hard_mini_games.playsound'):
                    with patch('hard_mini_games.random', return_value=computer_choice):
                        with patch('builtins.input', return_value=user_input):
                            self.game.game3("en", "no")
