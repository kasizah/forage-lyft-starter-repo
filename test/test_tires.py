import unittest

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class TestCarrigan(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire_wear_array = [0.2, 0.3, 0.93, 0.51]

        self.assertTrue(CarriganTires(tire_wear_array).needs_service())

    def test_tires_should_not_be_serviced(self):
        tire_wear_array = [0.2, 0.3, 0.3, 0.2]

        self.assertFalse(CarriganTires(tire_wear_array).needs_service())

class TestOctoprime(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire_wear_array = [1.2, 1.0, 0.9, 0.4]

        self.assertTrue(OctoprimeTires(tire_wear_array).needs_service())

    def test_tires_should_not_be_serviced(self):
        tire_wear_array = [0.3, 0.5, 0.9, 0.3]

        self.assertFalse(OctoprimeTires(tire_wear_array).needs_service())