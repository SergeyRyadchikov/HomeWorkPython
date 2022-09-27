# 10.	Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними 
# в 2D пространстве.
# Пример:
# o	A (3,6); B (2,1) -> 5,09
# o	A (7,-5); B (1,-1) -> 7,21

from math import sqrt


print('Введите координаты точки А:')
x_first_point = float(input('X1: '))
y_first_point = float(input('Y1: '))
print("Введите координаты точки Б:")
x_second_point = float(input('X2: '))
y_second_point = float(input('Y2: '))

print('расстояние между точками А и Б равно: ',round(sqrt((x_first_point - x_second_point)**2 + 
                                                (y_first_point - y_second_point)**2), 2))