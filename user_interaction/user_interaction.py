import datetime


class UserInteraction:
    """Класс для взаимодействия с пользователем через консоль, а имеено:
        - запрос ввода данных
        - проверка введенных данных
        Реализованы методы для запроса ввода целого числа, даты.
    """

    @staticmethod
    def input_int(instruction: str) -> int:
        """
        Запрос ввода целого числа
        :param instruction: инструкция, приглащающая пользователя ввести данные
        :return: введенное пользователем целое число
        """
        try:
            return int(input(f"{instruction} >"))
        except ValueError as e:
            raise UserInputError(f'Entered value is not an integer: {e.args[0]}')

    @staticmethod
    def input_date(instruction: str, format: str) -> datetime:
        """
        Запрос ввода даты
        :param instruction: инструкция, приглащающая пользователя ввести данные
        :param format: формат даты (допустимы форматы из модуля  datetime)
        :return: введенная пользователем дата
        """
        value = input(f"{instruction} >")
        try:
            return datetime.datetime.strptime(value, format).date()
        except ValueError as e:
            raise UserInputError(f'Entered value does not match the format {format}: {e.args[0]}')


class UserInputError(Exception):
    """Пользователь ввел некорректные данные"""
