from src.floor import NoEmptyParkingSpaceException, ParkingFloor
from src.ticket import Ticket
from src.vehicle import BaseVehicle


class DuplicateParkingLotIdException(Exception):
    """Parking lot ID must be unique"""


class ParkingLot:
    instances: dict = dict()

    def __init__(
        self,
        id="PR1234",
        numberOfFloors=2,
        numberOfSlots=6,
        *args,
        **kwargs
    ):
        self.id = self._assignID(id if len(args) == 0 else args[0])
        self.floorLimit = (int(numberOfFloors) +
                           1) if len(args) == 0 else int(args[1])
        self.slotLimit = numberOfSlots if len(args) == 0 else int(args[2])
        self.parking_map = [
            ParkingFloor(self.slotLimit, x) for x in range(1, self.floorLimit)
        ]

    def _assignID(self, id) -> str:
        if id in self.instances:
            raise DuplicateParkingLotIdException()
        else:
            self.instances[id] = self
        return id

    def _firstEmptyParkFloor(self, vehicle):
        for floor in self.parking_map:
            if floor.empty(vehicle) > 0:
                return floor
        raise NoEmptyParkingSpaceException

    def park_vehicle(self, vehicle: BaseVehicle) -> Ticket:
        emptyFloor = self._firstEmptyParkFloor(type(vehicle))
        ticket = emptyFloor.park_vehicle(vehicle)
        ticket.setParkingLot(self)
        ticket.openTicket()
        return ticket

    def unpark_vehicle(self, ticket: Ticket):
        ticket.floor.unpark_vehicle(ticket)
        ticket.closeTicket()
