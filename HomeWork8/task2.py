"""
Задание 2.
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Единственный класс этого проекта — одежда (класс Clothes).
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property
Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57
Два класса: абстрактный и Clothes
"""

from abc import ABC, abstractmethod


class My_abs_method(ABC):

    @abstractmethod
    def choice_of_clothes(self):
        pass


class Clothes(My_abs_method):

    def __init__(self, type_clothes, value):
        self.type_clothes = type_clothes
        self.value = value

    @property
    def choice_of_clothes(self):
        if str.lower(self.type_clothes) == 'пальто':
            result = round((self.value / 6.5 + 0.5), 2)
        if str.lower(self.type_clothes) == 'костюм':
            result = round(((2 * self.value) + 0.3), 2)
        return result

    def __add__(self, other):
        result = self.choice_of_clothes + other.choice_of_clothes
        return result

    def __str__(self):
        return str.lower(self.type_clothes)


obj_coat = Clothes('Пальто', 12)
obj_suit = Clothes('Костюм', 5)
print(f'{obj_coat.choice_of_clothes} метров ткани необходимо что бы пошить {obj_coat}')
print(f'\n{obj_suit.choice_of_clothes} метров ткани необходимо что бы пошить {obj_suit}')
print(f'\n{obj_coat + obj_suit} метров ткани необходимо чтобы пошить {obj_coat} и {obj_suit}')
