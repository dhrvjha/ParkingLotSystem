from pytest import fixture

from src.floor import ParkingFloor
from src.parkingLot import ParkingLot
from src.slot import BaseSlot, CarSlot, TruckSlot
from src.ticket import Ticket
from src.vehicle import Car, Truck


@fixture
def truck_slot_data() -> BaseSlot:
    return TruckSlot(1, Truck)


@fixture
def car_slot_data() -> BaseSlot:
    return CarSlot(5, Car)


@fixture
def truck() -> Truck:
    return Truck("2018ABCDEW", "BLACK")


@fixture
def floor() -> ParkingFloor:
    return ParkingFloor(10, 1)


@fixture
def floor_with_floormap() -> ParkingFloor:
    return ParkingFloor(10, {"TRUCK": [1, 4], "CAR": [4, 5]})


@fixture
def ticket(truck) -> Ticket:
    parkingLot = ParkingLot()
    return parkingLot.park_vehicle(truck)
