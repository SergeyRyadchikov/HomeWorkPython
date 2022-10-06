# 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример:
# o [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def difference_max_min_fractional_parts(user_list):
    new_list = []
    for i in user_list:
        i -= i // 1
        if i == 0:
            continue
        else:
            new_list.append(round(i, 2))
    print('Разница между максимальным и минимальным значением ' +
          f'дробной части = {max(new_list) - min(new_list)}')


size = int(input('Задайте размерность списка: '))
lst = [float(input('Введите значение: ')) for i in range(size)]
print(lst)
difference_max_min_fractional_parts(lst)
