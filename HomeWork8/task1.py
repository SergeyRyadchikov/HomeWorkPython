"""
Задание 1.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
Пример:
1 2 3
4 5 6
7 8 9
1 2 3
4 5 6
7 8 9
Сумма матриц:
2 4 6
8 10 12
14 16 18
"""

from random import randint as rndint


class Matrix:

    def __init__(self, list):
        self.list = list

    def __str__(self):
        result = '\n'.join(map(str, self.list))
        return result

    def __add__(self, other):
        sum_elements_matrix = []
        result = []
        for i in range(len(self.list)):
            for k in range(len(self.list[i])):
                result.append(self.list[i][k] + other.list[i][k])
            sum_elements_matrix.append(result)
            result = []
        result = '\n'.join(map(str, sum_elements_matrix))
        return result


def create_matrix(size):
    matrix = []
    for i in range(size):
        temp_list = [rndint(1, 10) for i in range(size)]
        matrix.append(temp_list)
    return matrix


obj_matrix_1 = Matrix(create_matrix(3))
obj_matrix_2 = Matrix(create_matrix(3))
print(obj_matrix_1)
print('------------------')
print(obj_matrix_2)
print('------------------')
print(f'Результат сложения:\n{obj_matrix_2 + obj_matrix_1}')
