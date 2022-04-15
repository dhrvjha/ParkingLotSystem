from src.vehicle import BaseVehicle


class BaseSlot:
    def __init__(self, id, vehicle):
        self.id: int = id
        self.vehicle: BaseVehicle = vehicle

    def __str__(self):
        return f"{self.id}"


class TruckSlot(BaseSlot):
    pass


class CarSlot(BaseSlot):
    pass


class BikeSlot(BaseSlot):
    pass
