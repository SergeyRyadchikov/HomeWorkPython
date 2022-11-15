"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

def ping_resurs(domain):
    args = ['ping', domain]

    ping_resurs = subprocess.Popen(args, stdout=subprocess.PIPE)

    for line in ping_resurs.stdout:
        char_detect = chardet.detect(line)
        encoded_line = line.decode(char_detect['encoding']).encode('utf-8')
        print(encoded_line.decode('utf-8'))

ping_resurs('yandex.ru')
ping_resurs('youtube.com')

