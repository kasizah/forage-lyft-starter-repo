from car import Car
from powertrain.engine import *
from electrical.battery import *

class CarFactory(Car):
    def __init__(self, engine, battery):
        super().__init__(engine, battery)

    def create_calliope(self, current_mileage, last_service_mileage, last_service_date):
        super().__init__(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date))

    def create_glissande(self, current_mileage, last_service_mileage, last_service_date):
        super().__init__(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date))

    def create_palindrome(self, warning_light_on, last_service_date):
        super().__init__(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date))

    def create_rorchach(self, current_mileage, last_service_mileage, last_service_date):
        super().__init__(WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date))

    def create_thovex(self, current_mileage, last_service_mileage, last_service_date):
        super().__init__(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date))