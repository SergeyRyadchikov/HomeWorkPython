# 33). Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k и приравняйте его к нулю.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# 2*x*2 + 4*x + 5 = 0
# или
# 2*x^2 + 4*x + 5 = 0
# к = 4 --->  5х^4 + 11x^3 - 8x^2 + 3x - 17 = 0

import random


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

            
            


user_enter = int(input('Введите степень: '))
polynomial_divider = create_list_elements_polynomial(user_enter)
with open('HomeWork4/fileTask33.txt', 'w') as file:
    file.write(polynomial_divider)
