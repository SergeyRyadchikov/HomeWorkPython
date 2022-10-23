"""
Задание 5.
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки!')


class Pen(Stationery):

    def draw(self):
        print('Запуск отрисовки ручкой!')


class Pencil(Stationery):

    def draw(self):
        print('Запуск отрисовки карандашом!')


class Handle(Stationery):

    def draw(self):
        print('Запуск отрисовки маркером!')


obj_stationary = Stationery('Канцелярская принадлежность')
obj_pen = Pen('Ручка')
obj_pencil = Pencil('Карандаш')
obj_handle = Handle('Маркер')


obj_stationary.draw()
obj_pen.draw()
obj_pencil.draw()
obj_handle.draw()


