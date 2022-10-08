# 30). Вычислить число π c заданной точностью d
# Пример:
# при d = 0.001,π = 3.141 10^(-1)≤d≤10^(-10)


from cmath import pi


def calculating_number_pi(user_number):
    result_first = 0
    result_second = 0
    degree = 0
    while user_number != 1:
        user_number *= 10
        degree += 1
    for i in range(1, 10 * degree, 2):
        result_first = result_second + (4 / (2 * i - 1))
        result_second = result_first - (4 / (2 * (i + 1) - 1))
    number_pi = str((result_first + result_second) / 2)
    print(number_pi[:degree])


d = float(input('Веедите точность вычисления: '))
calculating_number_pi(d)
# num_pi = str(calculating_number_pi(d))
# print(num_pi[:8])
print(pi)
