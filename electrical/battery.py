from datetime import datetime
from car import Car

class Battery(Car):
    def __init__(self, last_service_date):
        super().__init__()
        self.last_service_date = last_service_date
    
    def needs_service(self):
        return super().needs_service()
        
class SpindlerBattery(Battery):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return service_threshold_date < datetime.today().date()

class NubbinBattery(Battery):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return service_threshold_date < datetime.today().date()
