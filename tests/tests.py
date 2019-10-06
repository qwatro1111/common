import unittest
import math

from homework import Rectangle

class Test(unittest.TestCase):

    def setUp(self):
        self.width, self.height = 4, 6
        self.rectangle = Rectangle(self.width, self.height)

    def test_1_rectangle_perimeter(self):
        cheack = (self.width+self.height)*2
        result = self.rectangle.get_rectangle_perimeter()
        self.assertEqual(cheack, result)

    def test_2_rectangle_square(self):
        cheack = self.width*self.height
        result = self.rectangle.get_rectangle_square()
        self.assertEqual(cheack, result)

    def test_3_sum_of_corners_valid(self):
        cheack = 4*90
        result = self.rectangle.get_sum_of_corners(4)
        self.assertEqual(cheack, result)

    def test_4_sum_of_corners_invalid(self):
        with self.assertRaises(ValueError):
            self.rectangle.get_sum_of_corners(6)

    def test_5_sum_of_corners_invalid(self):
        with self.assertRaises(ValueError):
            self.rectangle.get_sum_of_corners(0)

    def test_6_rectangle_diagonal(self):
        cheack = math.sqrt(self.width**2 + self.height**2)
        result = self.rectangle.get_rectangle_diagonal()
        self.assertEqual(cheack, result)

    def test_7_radius_of_circumscribed_circle(self):
        cheack = self.rectangle.get_rectangle_diagonal() / 2
        result = self.rectangle.get_radius_of_circumscribed_circle()
        self.assertEqual(cheack, result)

    def test_8_radius_of_inscribed_circle(self):
        rectangle = Rectangle(width=1, height=1)
        cheack = rectangle.get_rectangle_diagonal() / 2 * math.sqrt(2)
        result = rectangle.get_radius_of_inscribed_circle()
        self.assertEqual(cheack, result)

    def test_9_radius_of_inscribed_circle(self):
        with self.assertRaises(ValueError):
            return self.rectangle.get_radius_of_inscribed_circle()

if __name__ == '__main__':
    unittest.main()
