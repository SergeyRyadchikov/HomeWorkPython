# 14). Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

from multiprocessing.sharedctypes import Value


def sum_digits(number):
    result = 0
    for symbol in number:
        if symbol.isdigit():
            result += int(symbol)
    print(f'Сумма цифр = {result}')


user_number = input('Введите число: ')
sum_digits(user_number)
