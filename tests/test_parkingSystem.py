import pytest

from src.parkingLot import DuplicateParkingLotIdException
from src.parkingMiddleware import ParkingSystem


def test_create_parking_lot():
    args = ["PR1234", "2", "6"]
    ParkingSystem().create_parking_lot(*args)
    with pytest.raises(DuplicateParkingLotIdException):
        ParkingSystem().create_parking_lot(*args)


def test_create_parking_lot_from_args():
    args = "create_parking_lot PR1334 2 6".split()
    p = ParkingSystem()
    ParkingSystem.__dict__[args[0]](p, *args[1:])
    with pytest.raises(DuplicateParkingLotIdException):
        ParkingSystem.__dict__[args[0]](p, *args[1:])


def test_free_count_args():
    args = "display free_count CAR".split()
    p = ParkingSystem()
    ParkingSystem.__dict__[args[1]](p, *args[2:])


def test_occupied_slots_args():
    args = "display occupied_slots CAR".split()
    p = ParkingSystem()
    ParkingSystem.__dict__[args[1]](p, *args[2:])


def test_free_slots_args():
    args = "display free_slots CAR".split()
    p = ParkingSystem()
    ParkingSystem.__dict__[args[1]](p, *args[2:])


def test_park_vehicle_args():
    args = "park_vehicle CAR KA-01-DB-1234 black".split()
    p = ParkingSystem()
    ParkingSystem.__dict__[args[0]](p, *args[1:])


def test_unpark_vehicle_args():
    args = "unpark_vehicle PR1234_2_5".split()
    p = ParkingSystem()
    ParkingSystem.__dict__[args[0]](p, *args[1:])


def test_exit_args(capsys):
    args = "exit".split()
    p = ParkingSystem()
    with pytest.raises(SystemExit):
        ParkingSystem.__dict__[args[0]](p, *args[1:])
        out, err = capsys.readouterr()
        assert out == "0"
