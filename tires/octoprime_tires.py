from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        sum = 0
        for tire in self.tire_wear_array:
            sum += tire
        return sum >= 3