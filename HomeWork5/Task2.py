# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента 
# достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего
#  конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


from random import randint

def robot_logic(total_num):
    pick = total_num % 29
    return pick


def human_data(user_name):
    quantity_sweets = int(input(f"{user_name}, возьмите конфеты в количестве от 1 до 28: "))
    while quantity_sweets < 1 or quantity_sweets > 28:
        quantity_sweets = int(input(f"{user_name}, число указано неверно. Введите правильное число, пожалуйста: "))
    return quantity_sweets


def result_print(user_name, candy, total_amount):
    print(f"{user_name} взял {candy} конфет. Осталось {total_amount} кофет в игре.")

player_1 = input('Введите ваше имя: ')
player_2 = 'Умнейший бот'

total_amount = int(input("Введите количество конфет в игре: "))

lot = randint(0,2)

if lot:
    print(f"Первый ходит {player_1}")
else:
    print(f"Первый ходит {player_2}")

counter_user_1 = 0
counter_user_2 = 0

while total_amount > 28:
    if lot:
        candy =  human_data(player_1)
        counter_user_1 += candy
        total_amount -= candy
        lot = False
        result_print(player_1, candy, total_amount)
    else:
        candy = robot_logic(total_amount)
        counter_user_2 += candy
        total_amount -= candy
        lot = True
        result_print(player_2, candy, total_amount)

if lot:
    print(f"Победил ---> {player_1}")
else:
    print(f"Победил ---> {player_2}")