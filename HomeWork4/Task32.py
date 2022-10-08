# 32). Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
#  элементов исходной последовательности.

import random


def create_list(list_length):
    lst = []
    for i in range(list_length):
        lst.append(random.randint(0, 10))
    return (lst)


def list_unique_elements(user_lsit):
    unique_elements = []
    for i in user_lsit:
        if i not in unique_elements:
            unique_elements.append(i)
    return unique_elements


def list_unique_elements2(user_lsit):
    unique_elements = []
    count = 0
    for i in user_lsit:
        for j in user_lsit:
            if i == j:
                count += 1
        if count == 1:
            unique_elements.append(i)
        count = 0
    return unique_elements


# Version 1: Убирает дубли, последовательность сохраняется
# user_lst = create_list(int(input('Введите размерность списка: ')))
# print(user_lst)
# lst_unique_elem = list_unique_elements(user_lst)
# print(lst_unique_elem)

# Version 2: Убирает дубли, порядок не сохраняется
# user_lst = create_list(int(input('Введите размерность списка: ')))
# print(user_lst)
# lst_unique_elem = list(set(user_lst))
# print(lst_unique_elem)

# Version 3: Остаются только неповторяющиеся элементы исходного списка
user_lst = create_list(int(input('Введите размерность списка: ')))
print(user_lst)
lst_unique_elem = list_unique_elements2(user_lst)
print(lst_unique_elem)