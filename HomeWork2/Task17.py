# 17). Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях.
#  Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода и зависит от количества
#  элементов в списке) в одной строке одно число.
# Пример:
# Файл:
# 4
# 5
# 2
# N = 3 => [-3, -2, -1, 0, 1, 2, 3]
# Результат: 1*2*(-1) = -2

print('Заполните файл!')
with open("file.txt", "w") as file:
    file.write(input('Строка №1: ') + '\n')
    file.write(input('Строка №2: ') + '\n')
    file.write(input('Строка №3: '))

n = int(input('N = '))
new_list = []
for i in range(-n, n + 1):
    new_list.append(i)
print(new_list)

with open("file.txt", "r") as file:
    list_indexes = []
    for i in file:
        list_indexes.append(i)

result = 1
for index in list_indexes:
    result *= new_list[int(index)]
print(f'Результат = {result}')
