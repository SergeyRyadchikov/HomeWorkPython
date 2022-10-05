# 23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и
# последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random


def create_list(list_length):
    lst = []
    for i in range(list_length):
        lst.append(random.randint(0, 10))
    return (lst)


def multiplication_element_lists(user_list):
    a = 0
    b = len(user_list) - 1
    result_list = []
    while a != b:
        result_list.append(user_list[a] * user_list[b])
        a += 1
        b -= 1
    else:
        result_list.append(user_list[a] ** 2)
    print(result_list)


size_list = int(input('Введите длину списка: '))
lst = create_list(size_list)
print(lst)
multiplication_element_lists(lst)
