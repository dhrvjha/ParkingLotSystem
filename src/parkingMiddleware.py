from weakref import WeakValueDictionary

from src.floor import NoEmptyParkingSpaceException

from .parkingLot import ParkingLot
from .settings import VEHICLES_MAP
from .ticket import NotaRegisteredTicketException, Ticket


class UnkownVehicleTypeException(Exception):
    """Vehicle type is not defined"""


class UnkownParkingLotIdException(Exception):
    """Parking Lot ID is not defined"""


class ParkingSystem:
    parking_lot_map = WeakValueDictionary()

    def free_count(self, vehicleType: str):
        """
        print for every floor
        No. of free slots for <vehicle_type> on Floor <floor_no>:
        <no_of_free_slots>
        """
        parkingLot: ParkingLot = self.getRandomParkingLot()

        for floor in parkingLot.parking_map:
            id = floor.id
            count = floor.empty(VEHICLES_MAP[vehicleType])
            print(
                "No. of free slots for {} on Floor {}: {}".format(
                    vehicleType, id, count
                )
            )

    def free_slots(self, vehicleType):
        """
        print for every floor
        Free slots for <vehicle_type> on Floor <floor_no>:
        <comma_separated_values_of_slot_nos>
        """
        parkingLot: ParkingLot = self.getRandomParkingLot()

        for floor in parkingLot.parking_map:
            id = floor.id
            count = ",".join(floor.freeSlots(VEHICLES_MAP[vehicleType]))
            print("Free slots for {} on Floor {}: {}".format(
                vehicleType, id, count))

    def occupied_slots(self, vehicleType: str):
        """
        print for every floor
        Occupied slots for <vehicle_type> on Floor <floor_no>:
         <comma_separated_values_of_slot_nos>
        """
        parkingLot: ParkingLot = self.getRandomParkingLot()
        for floor in parkingLot.parking_map:
            id = floor.id
            occup_slots = ",".join(
                map(str, floor.occupiedSlots(VEHICLES_MAP[vehicleType]))
            )
            print(
                "Occupied slots for {} on Floor {}: {}".format(
                    vehicleType, id, occup_slots
                )
            )

    @classmethod
    def getRandomParkingLot(cls) -> ParkingLot:
        return list(cls.parking_lot_map.values())[0]

    def create_parking_lot(self, id, floorLimit, slotLimit):
        self.parking_lot_map[id] = ParkingLot(id, floorLimit, slotLimit)
        print(
            "Created parking lot with {} floors and {} slots per floor".format(
                floorLimit, slotLimit
            )
        )
        return self.parking_lot_map[id]

    @classmethod
    def getParkingLot(cls, parkingLotID: str):
        parkingLot = cls.parking_lot_map.get(parkingLotID)
        if parkingLot is None:
            raise UnkownParkingLotIdException(
                f"{parkingLotID} is not a known parking lot."
            )
        return parkingLot

    def park_vehicle(
        self,
        vehicleType: str,
        vehicleRegNum: str,
        vehicleColor: str
    ):
        try:
            vehicleClass = VEHICLES_MAP[vehicleType]
        except KeyError:
            raise UnkownVehicleTypeException(
                f"{vehicleType} is not a defined vehicle type"
            )
        vehicle = vehicleClass(vehicleRegNum, vehicleColor)
        parkingLot = self.getRandomParkingLot()
        try:

            ticket: Ticket = parkingLot.park_vehicle(vehicle)
        except NoEmptyParkingSpaceException:
            print("Parking Lot Full")
            return None
        print(f"Parked vehicle. Ticket ID: {ticket}")

    def unpark_vehicle(self, strTicket: str):
        try:
            ticket = Ticket.getTicket(strTicket)
        except NotaRegisteredTicketException:
            print("Invalid Ticket")
            return None
        vehicle_reg = ticket.slot.vehicle.registrationNumber
        vehicle_col = ticket.slot.vehicle.color
        ParkingLot.unpark_vehicle(ticket)
        print(
            f"Unparked vehicle with Registration Number: {vehicle_reg} \
            and Color: {vehicle_col}"
        )

    @staticmethod
    def test():
        print("passed")

    def exit(self, *args, **kwargs):
        import sys

        sys.exit(0)
