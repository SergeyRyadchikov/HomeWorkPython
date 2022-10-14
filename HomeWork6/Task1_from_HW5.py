# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

file = open('HomeWork5/file_task1.txt', 'r', encoding='utf-8')
input_text = file.read().lower().split()
file.close()

search_word = input('Введите текст который нужно искать: ').lower()

new_text = " ".join(list(filter(lambda x: search_word not in x, input_text)))
print(f'Текст в редакции  --->', new_text)
