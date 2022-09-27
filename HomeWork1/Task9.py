# 9.	Напишите программу, которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой четверти (x и y).

def check_range(input_quarter):
    if input_quarter < 1 or input_quarter > 4:
        print('Пожалуйста, введите число от 1 до 4-х')
    elif input_quarter == 1:
        print('x > 0 и y > 0')
    elif input_quarter == 2:
        print('x < 0 и y > 0')
    elif input_quarter == 3:
        print('x < 0 и y < 0')
    elif input_quarter == 4:
        print('x > 0 и y < 0')

quarter = int(input("Введите число от 1 до 4-х:\n"))
check_range(quarter)
