# 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на
#  нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# size = int(input('Задайте размерность списка: '))
# lst = [int(input('Введите значение: ')) for i in range(size)]
# print(lst)

# result = 0
# for i in range(1, len(lst) - 1, 2):
#     result += lst[i]
# print(f'\nСумма элементов на нечетных позициях = {result}')


import random

lst = [random.randint(1, 20)
       for i in range(int(input('Введите длину списка: ')))]
print(lst)
# result = sum([x for i, x in enumerate(lst) if i % 2])
result = sum([lst[x] for x in range(len(lst)) if x % 2])
print(result)
