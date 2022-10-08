# 31). Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 70 = 2*5*7 => [2, 5, 7]
# 140 = 2*2*5*7 => [2, 2, 5, 7]
# 140|2
# 70|2
# 35|5
# 7|7


def list_number_multipliers(user_number):
    multipliers_list = []
    divider = 2
    while user_number / divider != 1:
        if user_number % divider == 0:
            user_number = user_number // divider
            multipliers_list.append(divider)
        else:
            divider += 1
    else:
        multipliers_list.append(divider)
    return multipliers_list


entered_number = int(input('Введите число: '))
multipliers_number = list_number_multipliers(entered_number)
print(
    f'Список простых множителей числа {entered_number} ---> {multipliers_number}')
