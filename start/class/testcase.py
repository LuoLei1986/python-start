import unittest
from car import Car

class CarTestCase(unittest.TestCase):
    def test_car_year(self):
        testcar = Car('audi', 'a4', 2021)
        self.assertEqual(testcar.get_descriptive_name(), '2021 Audi A4')

unittest.main()