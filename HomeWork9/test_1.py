import unittest
from Task6 import define_the_day
from Task7 import check_predicate
from Task8 import quarter_position
from Task14 import sum_digits


class Test_for_function(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(define_the_day(7), "Выходной!")

    def teste_not_equal(self):
        self.assertNotEqual(define_the_day(5), "Выходной!")

    def test_true(self):
        res = check_predicate([1, 3, 7])
        self.assertTrue(res)

    def test_in(self):
        self.assertIn(quarter_position(3, -7), [1, 2, 3, 4])

    def test_raises(self):
        with self.assertRaises(TypeError):
            sum_digits(3)

    def test_is_not_none(self):
        self.assertIsNotNone(sum_digits('3.4'))


if __name__ == '__main__':
    unittest.main()
