import unittest
from task2 import Road
from Task1 import TrafficLight


class Test_for_function(unittest.TestCase):

    def test_is_instance(self):
        user_obj = Road(5000, 20)
        self.assertIsInstance(user_obj, Road)

    def test_not_is_instance(self):
        user_obj = Road(2300, 30)
        self.assertNotIsInstance(user_obj, TrafficLight)

    def test_is(self):
        user_obj = TrafficLight()
        user_obj_2 = user_obj
        self.assertIs(user_obj, user_obj_2)

    def test_is_not(self):
        user_obj = TrafficLight()
        user_obj_2 = TrafficLight()
        self.assertIsNot(user_obj, user_obj_2)


if __name__ == '__main__':
    unittest.main()
