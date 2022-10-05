# 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# o 45 -> 101101
# o 3 -> 11
# o 2 -> 10

def conversion_binary_sistem(user_number):
    print(f'Число {user_number} в двоичной системе счисления =', end=' ')
    lst = []
    while user_number != 0:
        lst.append(user_number % 2)
        user_number = user_number // 2
    for i in reversed(lst):
        print(i, end='')


num = int(input('Введите число: '))
conversion_binary_sistem(num)
