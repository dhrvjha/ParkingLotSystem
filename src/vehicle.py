class BaseVehicle:
    def __init__(self, regNo, color):
        self.registrationNumber = regNo
        self.color = color


class Truck(BaseVehicle):
    pass


class Bike(BaseVehicle):
    pass


class Car(BaseVehicle):
    pass
