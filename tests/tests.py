import unittest
import math

from homework import Rectangle

class Test(unittest.TestCase):

    def setUp(self):
        self.width, self.height = 4, 6
        self.rectangle = Rectangle(self.width, self.height)

    def test_1_rectangle_perimeter(self):
        check = (self.width+self.height)*2
        result = self.rectangle.get_rectangle_perimeter()
        self.assertEqual(check, result)

    def test_2_rectangle_square(self):
        check = self.width*self.height
        result = self.rectangle.get_rectangle_square()
        self.assertEqual(check, result)

    def test_3_sum_of_corners_valid(self):
        check = 4*90
        result = self.rectangle.get_sum_of_corners(4)
        self.assertEqual(check, result)

    def test_4_sum_of_corners_invalid(self):
        with self.assertRaises(ValueError):
            self.rectangle.get_sum_of_corners(6)

    def test_5_rectangle_diagonal(self):
        check = math.sqrt(self.width**2 + self.height**2)
        result = self.rectangle.get_rectangle_diagonal()
        self.assertEqual(check, result)

    def test_6_radius_of_circumscribed_circle(self):
        check = self.rectangle.get_rectangle_diagonal() / 2
        result = self.rectangle.get_radius_of_circumscribed_circle()
        self.assertEqual(check, result)

    def test_7_radius_of_inscribed_circle(self):
        check = self.width / 2
        result = Rectangle(width=self.width, height=self.width).get_radius_of_inscribed_circle()
        self.assertEqual(check, result)

    def test_8_radius_of_inscribed_circle(self):
        with self.assertRaises(ValueError):
            return self.rectangle.get_radius_of_inscribed_circle()

if __name__ == '__main__':
    unittest.main()
