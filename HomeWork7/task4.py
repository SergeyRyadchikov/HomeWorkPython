"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

from random import randint as rnd


class Car:

    direction = {1: 'направо', 2: 'налево', 3: 'прямо'}
    speed = rnd(-10, 100)

    def __init__(self, color, name, is_police):
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            print('Автомобиль начал движение вперед!')
        elif self.speed < 0:
            print('Автомобиль начал движение назад!')
        else:
            print('Автомобиль стоит на месте!')

    def stop(self):
        if self.speed == 0:
            print('Автомобиль остановился!')
        else:
            print('Автомобиль находится в движениии!')

    def turn(self):
        key = rnd(1, 3)
        if key != 3:
            print(f'Автомобиль поворачивает {self.direction[key]}!')
        else:
            print(f'Автомобиль движется {self.direction[key]}!') 

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed <= 60:
            print(f'Текущая скорость автомобиля: {self.speed}')
        else:
            print(f'ВНИМАНИЕ! Превышение скорости! Текущая скорость автомобиля: {self.speed}')


class SportCar(Car):

    def overclocking_0_100(self):
        self.overclocking = rnd(3, 10)
        print(f'Разгон от 0 до 100 км/ч = {self.overclocking} сек.')


class WorkCar(Car):

    def show_speed(self):
        if self.speed <= 40:
            print(f'Текущая скорость автомобиля: {self.speed}')
        else:
            print(f'ВНИМАНИЕ! Превышение скорости! Текущая скорость автомобиля: {self.speed}')


class PoliceCar(Car):

    def view(self):
        if self.is_police:
            print('Это полицейский автомобиль')
        else:
            print('Это гражданский автомобиль')


print('\n<<   Car   >>\n')
obj_car = Car('Red', 'Ferarri', False)
obj_car.go()
obj_car.stop()
obj_car.show_speed()
obj_car.turn()
print(obj_car.color)
print(obj_car.name)

print('\n<<   TownCar   >>\n')

obj_town_car = TownCar('Blue', 'Lada', False)
obj_town_car.go()
obj_town_car.stop()
obj_town_car.show_speed()
obj_town_car.turn()
print(obj_town_car.color)
print(obj_town_car.name)

print('\n<<   SportCar   >>\n')

obj_sport_car = SportCar('Yellow', 'Lamborghini', False)
obj_sport_car.go()
obj_sport_car.stop()
obj_sport_car.show_speed()
obj_sport_car.turn()
obj_sport_car.overclocking_0_100()
print(obj_sport_car.color)
print(obj_sport_car.name)

print('\n<<   WorkCar   >>\n')

obj_work_car = WorkCar('Black', 'Chevrolet', False)
obj_work_car.go()
obj_work_car.stop()
obj_work_car.show_speed()
obj_work_car.turn()
print(obj_work_car.color)
print(obj_work_car.name)

print('\n<<   PoliceCar   >>\n')

obj_police_car = PoliceCar('White', 'Kia', True)
obj_police_car.go()
obj_police_car.stop()
obj_police_car.show_speed()
obj_police_car.turn()
obj_police_car.view()
print(obj_police_car.color)
print(obj_police_car.is_police)