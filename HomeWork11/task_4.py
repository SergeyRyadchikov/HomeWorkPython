"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = ['разработка', 'администрирование', 'protocol', 'standard']

for word in words:
    encoded_word = word.encode()
    print(f'Байтовое представление: {encoded_word}')
    decoded_word = encoded_word.decode()
    print(f'Обратное преобрзованние: {decoded_word}\n')
    
    
    