import pytest

from src.parkingLot import DuplicateParkingLotIdException, ParkingLot
from src.ticket import NotaRegisteredTicketException, Ticket


def test__assignID():
    ParkingLot(id="12")
    with pytest.raises(DuplicateParkingLotIdException):
        ParkingLot(id="12")


def test_park_vehicle(truck):
    parkinglot = ParkingLot(id="13")
    ticket: Ticket = parkinglot.park_vehicle(truck)
    assert ticket.parkingLot == parkinglot


def test_unpark_vehicle(truck):
    parkinglot = ParkingLot(id="14")
    ticket: Ticket = parkinglot.park_vehicle(truck)
    parkinglot.unpark_vehicle(ticket)
    with pytest.raises(NotaRegisteredTicketException):
        Ticket.getTicket(str(ticket))
