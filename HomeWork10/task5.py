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


class TypeDescriptor:

    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if type(value) != str:
            raise TypeError("Неверные данные")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]


class Stationery:

    title = TypeDescriptor('title')

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


# obj_stationary = Stationery('Канцелярская принадлежность')
obj_pen = Pen('pen')
# obj_pencil = Pencil('Карандаш')
# obj_handle = Handle('Маркер')


# obj_stationary.draw()
obj_pen.draw()
print(obj_pen.title)
# obj_pen.title = '12'
# print(obj_pen.title)
# del obj_pen.title

# obj_pencil.draw()
# obj_handle.draw()
