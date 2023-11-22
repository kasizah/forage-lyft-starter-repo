from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class CarFactory:
    @staticmethod
    def create_calliope(
        current_mileage, last_service_mileage,
        current_date, last_service_date
    ):
        return Car(
            CapuletEngine(current_mileage, last_service_mileage), 
            SpindlerBattery(current_date, last_service_date)
        )

    @staticmethod
    def create_glissade(
        current_mileage, last_service_mileage,
        current_date, last_service_date
    ):
        return Car(
            WilloughbyEngine(current_mileage, last_service_mileage), 
            SpindlerBattery(current_date, last_service_date)
        )
    
    @staticmethod
    def create_palindrome(
        warning_light_is_on,
        current_date, last_service_date
    ):
        return Car(
            SternmanEngine(warning_light_is_on), 
            SpindlerBattery(current_date, last_service_date)
        )
    
    @staticmethod
    def create_rorschach(
        current_mileage, last_service_mileage,
        current_date, last_service_date
    ):
        return Car(
            WilloughbyEngine(current_mileage, last_service_mileage), 
            NubbinBattery(current_date, last_service_date)
        )
    
    @staticmethod
    def create_thovex(
        current_mileage, last_service_mileage,
        current_date, last_service_date
    ):
        return Car(
            CapuletEngine(current_mileage, last_service_mileage), 
            NubbinBattery(current_date, last_service_date)
        )