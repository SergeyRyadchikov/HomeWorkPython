# 16). Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.

def create_list(num):
    new_list = []
    for i in range(1, num + 1):
        new_list.append(round(((1 + 1 / i) ** i), 3))
    return(new_list)

def sum_elements_list(user_list):
    result = 0
    for i in user_list:
        result += i
    print(f'Сумма элементов списка = {result}')


n = int(input('Введите число: '))
print(create_list(n))
sum_elements_list(create_list(n))