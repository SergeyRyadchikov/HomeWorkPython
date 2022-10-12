# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def coding(text):
    count = 1
    res = ''
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            count += 1
        else:
            res = res + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text) - 2] != text[-1]):
        res = res + str(count) + text[-1]
    return res


def decoding(text):
    number = ''
    res = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            number += text[i]
        else:
            res = res + text[i] * int(number)
            number = ''
    return res


with open('HomeWork5/file_task4.txt', 'w') as data:
    data.write(input('Введите исходный текст: '))
with open('HomeWork5/file_task4.txt', 'r') as data:
    initial_data = data.readline()
print(f'Исходный текст: {initial_data}')

with open('HomeWork5/file_encode_task4.txt', 'w') as file:
    file.write(coding(initial_data))
with open('HomeWork5/file_encode_task4.txt', 'r') as file:
    encode_data = file.read()
print(f'Кодировка: {encode_data}')

with open('HomeWork5/file_decode_task4.txt', 'w') as file:
    file.write(decoding(encode_data))
with open('HomeWork5/file_decode_task4.txt', 'r') as file:
    decode_date = file.read()
print(f'Расшифровка: {decode_date}')
