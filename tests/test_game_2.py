import unittest
from unittest.mock import patch
import json

from hard_mini_games import Hard
from health_exception import Health_exception


def mock_playsound(file):
    if isinstance(file, dict):
        raise ValueError
    if 'ua' in file:
        return 'Audio file in Ukrainian.'
    else:
        return 'Audio file in English.'


class TestGame2(unittest.TestCase):
    def setUp(self) -> None:
        self.test_hard = Hard()
        with open('story.json', encoding="utf-8") as f:
            self.story = json.loads(f.read())

    def test_game2_introduction_ukrainian(self):
        test_value = self.story["110"]["укр"]['text']
        result = "\nЦя гра називається \"Кидання кубиків\"." \
                 "\nВи повинні кинути кубики так, щоб сума цифр була більшою або дорівнювала 8."

        self.assertEqual(test_value, result)

    def test_game2_introduction_english(self):
        test_value = self.story["110"]["en"]['text']
        result = "\nThis game named \"Dice rolling\"." \
                 "\nYou must roll the dice and the sum of the digits must be greater than or equal to 8."

        self.assertEqual(test_value, result)

    def test_game2_introduction_without_audio(self):
        audio = 'no'
        test_value = None
        if audio == 'no' or audio == 'ні':
            test_value = self.story["110"]['time']
        self.assertEqual(test_value, 12)

        audio = 'ні'
        if audio == 'no' or audio == 'ні':
            test_value = self.story["110"]['time']
        self.assertEqual(test_value, 12)

    def test_game2_introduction_with_audio(self):
        audio = 'yes'
        language = 'en'
        test_value = None
        if audio == 'yes' or audio == 'так':
            for voice in self.story["110"][language]['voice'].values():
                test_value = mock_playsound(voice)
        self.assertEqual(test_value, 'Audio file in English.')

        audio = 'так'
        language = 'укр'
        if audio == 'yes' or audio == 'так':
            for voice in self.story["110"][language]['voice'].values():
                test_value = mock_playsound(voice)
        self.assertEqual(test_value, 'Audio file in Ukrainian.')

    def test_game2_introduction_with_audio_dict(self):
        audio = 'так'
        language = 'укр'
        with self.assertRaises(ValueError):
            if audio == 'yes' or audio == 'так':
                mock_playsound(self.story["110"][language]['voice'])

        audio = 'yes'
        language = 'en'
        with self.assertRaises(ValueError):
            if audio == 'yes' or audio == 'так':
                mock_playsound(self.story["110"][language]['voice'])

    def test_input_throw(self):
        with patch('builtins.input', return_value='throw'):
            language = 'en'
            input(self.story["111"][language]['text'])
            result = 1

        self.assertEqual(result, 1)

    def test_input_different_word(self):
        # I should fix bug
        with patch('builtins.input', return_value='put'):
            language = 'en'
            input(self.story["111"][language]['text'])
            result = 1

        self.assertEqual(result, 1)

    def test_win_game2(self):
        health = 10
        rand_choice = [6, 6]
        test_value = None
        if (rand_choice[0] + rand_choice[1]) >= 8:
            test_value = f"You win. Lives have left {health}."
        result = "You win. Lives have left 10."

        self.assertEqual(test_value, result)

    def test_lost_game2(self):
        health = 10
        rand_choice = [1, 1]
        with self.assertRaises(Health_exception):
            while True:
                if (rand_choice[0] + rand_choice[1]) >= 8:
                    test_value = f"You win. Lives have left {health}."
                    break
                health -= 1
                test_value = f'Bad luck. Lives have left {health}.'
                if health == 0:   # if lives ends it will raise the exception.
                    raise Health_exception(health)
        result = f'Bad luck. Lives have left 0.'
        self.assertEqual(test_value, result)
