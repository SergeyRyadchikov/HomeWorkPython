# 34). Даны два файла, в каждом из которых находится запись многочлена, приравненного к нулю. Задача -
# сформировать файл, содержащий сумму многочленов (суммируем подобные слагаемые).
# Пример:
# 1 Файл : 2*x2 + 4*x + 5 = 0
# 2 Файл : 4*x2 + 7*x + 9 = 0
# 3 Файл: (содержит результат) 6*x2 + 11*x + 14 = 0
# Пример:
# 1 Файл : 2*x^3 + 4*x^2 + 5*x + 1 = 0
# 2 Файл : 4*x2 + 7*x + 9 = 0
# 3 Файл: (содержит результат) 2*x3 + 8*x2 + 12x + 10 = 0

import random


# Функция составляет многочлен заданной степени
def create_list_elements_polynomial(custom_value):
    actions_list = ['-', '+']
    list_elements_polynomial = []
    for i in range(custom_value, -1, -1):
        coefficient = random.randint(0, 100)
        if i == 0:
            if coefficient != 0:
                list_elements_polynomial.append(f'{coefficient}')
            else:
                continue
        elif i == 1:
            if coefficient > 1:
                list_elements_polynomial.append(f'{coefficient}x')
                list_elements_polynomial.append(random.choice(actions_list))
            elif coefficient == 1:
                list_elements_polynomial.append('x')
                list_elements_polynomial.append(random.choice(actions_list))
            else:
                continue
        else:
            if coefficient > 1:
                list_elements_polynomial.append(f'{coefficient}x^{i}')
                list_elements_polynomial.append(random.choice(actions_list))
            elif coefficient == 1:
                list_elements_polynomial.append(f'x^{i}')
                list_elements_polynomial.append(random.choice(actions_list))
            else:
                continue
    list_elements_polynomial.append('= 0')
    polynomial = " ".join(map(str, list_elements_polynomial))
    return polynomial


# Функция переводит строку, которая содержит многочлен в словарь
def translating_polynomial_in_dictionary(user_polinomail):
    user_polinomail = user_polinomail[:-4].replace('- ', '+ -')
    polynomial_list = user_polinomail.split(' + ')

    for i in range(len(polynomial_list)):
        if 'x' and '^' in polynomial_list[i]:
            pass
        elif 'x' in polynomial_list[i] and '^' not in polynomial_list[i]:
            polynomial_list[i] = polynomial_list[i] + '^1'
        elif 'x' and '^' not in polynomial_list[i]:
            polynomial_list[i] = polynomial_list[i] + 'x^0'

    dict_polynomial = {}
    for i in polynomial_list:
        temp_lst = i.split('x')
        if temp_lst[0] == '':
            temp_lst[0] = 1
        dict_polynomial[temp_lst[1][1:]] = int(temp_lst[0])
    return dict_polynomial


# Функция вовращает сумму элементов с одинаковыми ключами из двух словарей
def sum_elements_dictions(dict_1, dict_2):
    if len(dict_1) > len(dict_2):
        for key_1 in dict_1:
            for key_2 in dict_2:
                if key_1 == key_2:
                    dict_1[key_1] = dict_1[key_1] + dict_2[key_2]
                else:
                    pass
        result_diction = dict_1
    else:
        for key_2 in dict_2:
            for key_1 in dict_1:
                if key_2 == key_1:
                    dict_2[key_2] = dict_1[key_1] + dict_2[key_2]
                else:
                    pass
        result_diction = dict_2
    return result_diction


# Функция возвращает список строк, составленный из элементов словаря
def writing_dictionary_in_list(user_diction):
    result_list = []
    for key in user_diction:
        if int(key) > 1:
            if user_diction[key] > 1 or user_diction[key] < -1:
                result_list.append(f'{user_diction[key]}x^{key}')
            elif user_diction[key] == 1:
                result_list.append(f'x^{key}')
            elif user_diction[key] == -1:
                result_list.append(f'-x^{key}')
            else:
                pass
        elif int(key) == 1:
            if user_diction[key] > 1 or user_diction[key] < -1:
                result_list.append(f'{user_diction[key]}x')
            elif user_diction[key] == 1:
                result_list.append('x')
            elif user_diction[key] == -1:
                result_list.append('-x')
            else:
                pass
        else:
            if user_diction[key] != 0:
                result_list.append(f'{user_diction[key]}')
            else:
                pass
    return result_list


# Функция возвращает строку, составленную из элементов списка
def writing_list_in_string(user_list):
    for i in range(len(user_list)):
        if i == 0:
            result_string = user_list[i]
        elif i > 0 and i <= (len(user_list) - 1):
            if '-' in user_list[i]:
                result_string += ' - '
                result_string += user_list[i][1:]
            else:
                result_string += ' + '
                result_string += user_list[i]
    result_string += ' = 0'
    return result_string


user_enter_1, user_enter_2 = int(input('Введите степень: ')), int(input('Введите степень: '))
polynomial_divider_1 = create_list_elements_polynomial(user_enter_1)
polynomial_divider_2 = create_list_elements_polynomial(user_enter_2)

with open('HomeWork4/file_task34_1.txt', 'w') as file:
    file.write(polynomial_divider_1)
with open('HomeWork4/file_task34_2.txt', 'w') as file:
    file.write(polynomial_divider_2)

with open('HomeWork4/file_task34_1.txt', 'r') as file:
    polynomail_1 = file.read()
with open('HomeWork4/file_task34_2.txt', 'r') as file:
    polynomail_2 = file.read()

diction_polyonail_1 = translating_polynomial_in_dictionary(polynomail_1)
diction_polyonail_2 = translating_polynomial_in_dictionary(polynomail_2)
res_dict = sum_elements_dictions(diction_polyonail_1, diction_polyonail_2)
res_list = writing_dictionary_in_list(res_dict)
result = writing_list_in_string(res_list)

with open('HomeWork4/file_task34_result.txt', 'w') as file:
    file.write(result)