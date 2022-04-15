import io
from contextlib import redirect_stdout

from .parkingMiddleware import ParkingSystem


class display:
    @staticmethod
    def free_count(vehicleType, *args):
        """
        print for every floor
        No. of free slots for <vehicle_type> on Floor <floor_no>:
         <no_of_free_slots>
        """
        pass

    @staticmethod
    def free_slots(vehicleType, *args):
        """
        print for every floor
        Free slots for <vehicle_type> on Floor <floor_no>:
         <comma_separated_values_of_slot_nos>
        """
        pass

    @staticmethod
    def occupied_slots(vehicleType, *args):
        """
        print for every floor
        Occupied slots for <vehicle_type> on Floor <floor_no>:
         <comma_separated_values_of_slot_nos>
        """
        pass


class UserInput:
    parkingSystem: ParkingSystem

    @classmethod
    def read(cls):
        line = input()
        args = line.split()
        if args[0] == "display":
            ParkingSystem.__dict__[args[1]](cls.parkingSystem, *args[2:])
        else:
            ParkingSystem.__dict__[args[0]](cls.parkingSystem, *args[1:])


def main():
    while True:
        UserInput.read()


def main_with_buffer():
    UserInput.parkingSystem = ParkingSystem()
    buffer: str
    with io.StringIO() as buf, redirect_stdout(buf):
        try:
            while True:
                UserInput.read()
        except SystemExit:
            buffer = buf.getvalue()
    return buffer
