# 18). Реализуйте алгоритм перемешивания списка.

import random


def new_list_creation(list_length):
    create_list = []
    for i in range(list_length):
        new_number = random.randint(0, 30)
        create_list.append(new_number)
    return create_list


def shuffle_list(list_length, old_list):
    new_list = old_list
    for i in range(list_length):
        index = random.randint(0, list_length - 1)
        temp = old_list[i]
        new_list[i] = old_list[index]
        old_list[index] = temp
    print(f'Новый список: \n{new_list}')


size_list = int(input('Введите длину списка: '))
first_list = new_list_creation(size_list)
print(f'Заданный список: \n{first_list}')
shuffle_list(size_list, first_list)
