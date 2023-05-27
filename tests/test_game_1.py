import unittest
from unittest.mock import patch
import json

from health_exception import Health_exception


def mock_playsound(file):
    if 'ua' in file:
        return 'Audio file in Ukrainian.'
    else:
        return 'Audio file in English.'


class TestGame1(unittest.TestCase):
    def setUp(self) -> None:
        # open json file "story" and read it.
        with open('story.json', encoding="utf-8") as f:
            self.story = json.loads(f.read())

    def test_game1_introduction_ukrainian(self):
        test_value = self.story["106"]["укр"]['text']
        result = "\nЦя гра називається \"Вгадай число\".\nКомп'ютер загадав число від 1 до 10..."

        self.assertEqual(test_value, result)

    def test_game1_introduction_english(self):
        test_value = self.story["106"]["en"]['text']
        result = "\nThis game named \"Guess the number\".\nThe computer guessed a number from 1 to 10..."

        self.assertEqual(test_value, result)

    def test_game1_introduction_without_audio(self):
        audio = 'no'
        test_value = None
        if audio == 'no' or audio == 'ні':
            test_value = self.story["106"]['time']
        self.assertEqual(test_value, 6)

        audio = 'ні'
        if audio == 'no' or audio == 'ні':
            test_value = self.story["106"]['time']
        self.assertEqual(test_value, 6)

    def test_game1_introduction_with_audio(self):
        audio = 'yes'
        language = 'en'
        test_value = None
        if audio == 'yes' or audio == 'так':
            test_value = mock_playsound(self.story["106"][language]['voice'])
        self.assertEqual(test_value, 'Audio file in English.')

        audio = 'так'
        language = 'укр'
        if audio == 'yes' or audio == 'так':
            test_value = mock_playsound(self.story["106"][language]['voice'])
        self.assertEqual(test_value, 'Audio file in Ukrainian.')

    def test_game1_choose_number_ukrainian(self):
        result = '\nОбери число (від 1 до 10): '
        language = 'укр'
        test_value = self.story["107"][language]['text']
        self.assertEqual(test_value, result)

    def test_game1_choose_number_english(self):
        result = '\nChoose number (from 1 to 10): '
        language = 'en'
        test_value = self.story["107"][language]['text']
        self.assertEqual(test_value, result)

    @patch('builtins.input', return_value='7')
    def test_game1_choose_number(self, mock_input):
        language = 'en'
        test_num = int(input(self.story["107"][language]['text']))
        self.assertEqual(test_num, 7)

    def test_check_set_different_numbers(self):
        test_all_num = set()
        test_all_num.add(1)
        test_all_num.add(2)
        test_all_num.add(3)
        result = {1, 2, 3}
        self.assertEqual(test_all_num, result)

    def test_check_set_same_numbers(self):
        test_all_num = set()
        test_all_num.add(1)
        test_all_num.add(1)
        test_all_num.add(1)
        result = {1}
        self.assertEqual(test_all_num, result)

    def test_lost_one_live(self):
        health = 10
        health -= 1

        test_value = f'\nOhh... You`re loose!\nMinus 1 point.\nYou have left {health} lives.'
        result = '\nOhh... You`re loose!\nMinus 1 point.\nYou have left 9 lives.'
        self.assertEqual(test_value, result)

        test_value = f'\nОй... Не вгадав!\nВи втратили одне життя.\nУ вас залишилося життів {health}.'
        result = '\nОй... Не вгадав!\nВи втратили одне життя.\nУ вас залишилося життів 9.'
        self.assertEqual(test_value, result)

    def test_lost_all_lives(self):
        num = 1
        number = 7
        health = 10
        with self.assertRaises(Health_exception):
            while num != number:
                health -= 1
                if health == 0:
                    raise Health_exception(health)

    def test_first_clue_ukrainian(self):
        clue = 1
        language = 'укр'
        result = "\nЯ дам тобі одну підказку.\nЦе число більше 5."
        test_value = None
        if clue == 1:
            test_value = self.story["108"][language]['text']

        self.assertEqual(test_value, result)

    def test_first_clue_english(self):
        clue = 1
        language = 'en'
        result = "\nI'll give you a clue.\nThis number is greater than 5."
        test_value = None
        if clue == 1:
            test_value = self.story["108"][language]['text']

        self.assertEqual(test_value, result)

    def test_second_clue_english(self):
        clue = 2
        language = 'en'
        result = "\nI'll give you one more clue.\nThis is odd number."
        test_value = None
        if clue == 2:
            test_value = self.story["109"][language]['text']

        self.assertEqual(test_value, result)

    def test_second_clue_ukrainian(self):
        clue = 2
        language = 'укр'
        result = "\nЩе одна підказка. Це непарне число."
        test_value = None
        if clue == 2:
            test_value = self.story["109"][language]['text']

        self.assertEqual(test_value, result)

    def test_print_all_chosen_different_numbers(self):
        all_num = {1, 2, 3}

        language = 'en'
        result = '\n(You have chosen [1, 2, 3])'
        test_value = None
        if language == "en":
            test_value = f'\n(You have chosen {sorted(all_num)})'
        self.assertEqual(test_value, result)

        language = 'укр'
        result = '\n(Ти вже обрав [1, 2, 3])'
        if language == "укр":
            test_value = f'\n(Ти вже обрав {sorted(all_num)})'
        self.assertEqual(test_value, result)

    def test_print_all_chosen_same_numbers(self):
        all_num = {1, 1, 1}

        language = 'en'
        result = '\n(You have chosen [1])'
        test_value = None
        if language == "en":
            test_value = f'\n(You have chosen {sorted(all_num)})'
        self.assertEqual(test_value, result)

        language = 'укр'
        result = '\n(Ти вже обрав [1])'
        if language == "укр":
            test_value = f'\n(Ти вже обрав {sorted(all_num)})'
        self.assertEqual(test_value, result)

    def test_victory_english(self):
        num = 7
        number = 7
        health = 10
        language = 'en'
        test_value = None
        while num != number:
            pass
        else:
            if language == "en":
                test_value = f'\nCongratulations, you win!!!\nYou have left {health} lives.'

        result = '\nCongratulations, you win!!!\nYou have left 10 lives.'
        self.assertEqual(test_value, result)

    def test_victory_ukrainian(self):
        num = 7
        number = 7
        health = 10
        language = 'укр'
        test_value = None
        while num != number:
            pass
        else:
            if language == "укр":
                test_value = f'\nМої вітання, ви перемогли!!!\nУ вас залишилося життів {health}.'

        result = '\nМої вітання, ви перемогли!!!\nУ вас залишилося життів 10.'
        self.assertEqual(test_value, result)
