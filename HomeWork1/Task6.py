# 6.	Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# o	6 -> да
# o	7 -> да
# o	1 -> нет

input_day = int(input("Введите число от 1 до 7: "))
if input_day > 7 or input_day < 1:
    print('Введите число от 1 до 7')
elif input_day == 6 or input_day == 7:
    print("Выходной!")
else:
    print("Нет, это не выходной")
