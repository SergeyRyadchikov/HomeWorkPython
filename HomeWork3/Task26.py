# 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# o для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fibonacci(a):
    lst_fibonaci = []
    for i in range(a + 1):
        if i == 0 or i == 1:
            lst_fibonaci.append(i)
        else:
            lst_fibonaci.append(lst_fibonaci[i - 1] + lst_fibonaci[i - 2])
    return lst_fibonaci


def negafibonacci(lst):
    lst_negafibonacci = []
    for i in range(1, len(lst)):
        lst_negafibonacci.append(((-1)**(i+1)) * lst[i])
    return list(reversed(lst_negafibonacci))


k = int(input('Введите целое число: '))

fib = fibonacci(k)
negafib = negafibonacci(fib)
print(negafib + fib)
