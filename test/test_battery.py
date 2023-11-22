import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)
        
        self.assertTrue(SpindlerBattery(current_date, last_service_date).needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)

        self.assertFalse(SpindlerBattery(current_date, last_service_date).needs_service())

class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)

        self.assertTrue(NubbinBattery(current_date, last_service_date).needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)

        self.assertFalse(NubbinBattery(current_date, last_service_date).needs_service())