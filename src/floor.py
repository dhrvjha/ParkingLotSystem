from math import inf
from typing import List

from src.settings import DEFAULT_FLOOR_MAP, SLOTS_MAP
from src.ticket import Ticket
from src.vehicle import BaseVehicle


class NoEmptyParkingSpaceException(Exception):
    """There is no empty parking space"""


class Floor:
    def __init__(self, size, floor_id):
        self.floor_map = DEFAULT_FLOOR_MAP
        self.busy_slot_map = {x: {} for x in self.floor_map.keys()}
        self.busy_slot_len = {x: 0 for x in self.floor_map.keys()}
        self.id: int = int(floor_id)
        self.size = int(size)

    def park(self, vehicle: BaseVehicle):
        pass

    def unpark(self, ticket: Ticket):
        pass

    def occupiedSlots(self, vehicle_class):
        pass

    def freeSlots(self, vehicle_class):
        pass


class ParkingFloor:
    """
    A parking floor can contain one or more types of parking slots
    default:
        trucks = 1
        bikes = 2
        cars = every other slot

    A Vehicle should be parked at the first empty position of its type
    """

    def __init__(self, size, floor_id, *args, **kwargs):
        self.floor_map = (
            DEFAULT_FLOOR_MAP if "floor_map" not in kwargs
            else kwargs["floor_map"]
        )

        self.busy_slot_map = {x: {} for x in self.floor_map.keys()}
        self.busy_slot_len = {x: 0 for x in self.floor_map.keys()}
        self.id: int = int(floor_id)
        self.size = int(size)

        self._floorMapSetup()

    def _floorMapSetup(self):
        """clear inf value from floor_map"""
        for v in self.floor_map.values():
            if v[1] == inf:
                v[1] = self.size + 1

    def _firstEmptyParkSlot(self, vehicle) -> int:
        """find first empty slot for vehicle class"""
        slot_range = self.floor_map[vehicle]
        for x in range(slot_range[0], slot_range[1]):
            if x not in self.busy_slot_map[vehicle]:
                return x
        return -1

    def park_vehicle(self, vehicle: BaseVehicle) -> Ticket:
        """park vehicle in first empty slot"""
        minSlotValue = self._firstEmptyParkSlot(type(vehicle))
        if minSlotValue == -1:
            raise NoEmptyParkingSpaceException()
        parking_slot = SLOTS_MAP[type(vehicle)](minSlotValue, vehicle)
        self.busy_slot_map[type(vehicle)][minSlotValue] = parking_slot
        self.busy_slot_len[type(vehicle)] += 1
        return Ticket(self, parking_slot)

    def unpark_vehicle(self, ticket: Ticket):
        """unpark vehicle"""
        vehicle_class = type(ticket.slot.vehicle)
        self.busy_slot_map[vehicle_class].pop(ticket.slot.id)
        self.busy_slot_len[vehicle_class] -= 1

    def occupiedSlots(self, vehicle) -> List[int]:
        """list of all occupied slots of vehicle class"""
        return self.busy_slot_map[vehicle].keys()

    def freeSlots(self, vehicle) -> List[int]:
        """list of all free slots of vehicle class"""
        vehicleMap = self.floor_map[vehicle]
        return [
            str(x)
            for x in range(vehicleMap[0], vehicleMap[1])
            if x not in self.busy_slot_map
        ]

    def empty(self, vehicle):
        """"""
        vehicle_floor_map = self.floor_map[vehicle]
        size = vehicle_floor_map[1] - vehicle_floor_map[0]
        return size - self.busy_slot_len[vehicle]
