# 15). Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def list_factorials(number):
    user_list = []
    factorial = 1
    if number < 1:
        list_factorials(int(input('Enter a positive number: ')))
    else:
        for i in range(1, number + 1):
            factorial *= i
            user_list.append(factorial)
        print(user_list)


try:
    list_factorials(int(input('Enter a positive number: ')))
except:
    print('Error: Вы ввели не число!')
    list_factorials(int(input('Enter a positive number: ')))
