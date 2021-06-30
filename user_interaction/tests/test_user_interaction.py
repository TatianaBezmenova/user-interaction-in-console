import datetime
import unittest
from unittest.mock import patch

from user_interaction.user_interaction import UserInteraction, UserInputError


class TestUserInteraction(unittest.TestCase):
    def test_input_int(self):
        with patch('builtins.input', lambda *args: '1'):
            value = UserInteraction.input_int('Введите целое число')
            self.assertEqual(1, value)

        with patch('builtins.input', lambda *args: '1.0'):
            self.assertRaises(UserInputError, UserInteraction.input_int, 'Введите целое число')

        with patch('builtins.input', lambda *args: 'qwerty'):
            self.assertRaises(UserInputError, UserInteraction.input_int, 'Введите целое число')

    def test_input_date(self):
        with patch('builtins.input', lambda *args: '6-12-2021'):
            valid_date = datetime.datetime.strptime('06-12-2021', '%d-%m-%Y').date()
            date = UserInteraction.input_date('Введите дату', '%d-%m-%Y')
            self.assertEqual(valid_date, date)
            self.assertIsInstance(date, datetime.date)

        with patch('builtins.input', lambda *args: '06122021'):
            valid_date = datetime.datetime.strptime('06122021', '%d%m%Y').date()
            date = UserInteraction.input_date('Введите дату', '%d%m%Y')
            self.assertEqual(valid_date, date)

        with patch('builtins.input', lambda *args: '31022021'):
            self.assertRaises(UserInputError, UserInteraction.input_date, 'Введите дату', '%d%m%Y')

        with patch('builtins.input', lambda *args: 'qwerty'):
            self.assertRaises(UserInputError, UserInteraction.input_date, 'Введите дату', '%d%m%Y')
