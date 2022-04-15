from src.floor import ParkingFloor
from src.ticket import Ticket
from src.vehicle import Truck


def test_floor_size(floor, *args, **kwargs):
    assert floor.size == 10


def test_floor_id(floor, *args, **kwargs):
    assert floor.id == 1


# def test_floor_floormap(floor, *args, **kwargs):
#     assert floor.floor_map == DEFAULT_FLOOR_MAP


def test_floor_parking(floor: ParkingFloor, truck: Truck):
    initial_size = len(floor.occupiedSlots(type(truck)))
    floor.park_vehicle(truck)
    assert initial_size + 1 == len(floor.occupiedSlots(type(truck)))


def test_floor_paring_firstEmptySlot(floor: ParkingFloor, truck: Truck):
    ticket: Ticket = floor.park_vehicle(truck)
    first_empty_slot = floor._firstEmptyParkSlot(type(truck))
    assert ticket.slot.id < first_empty_slot or first_empty_slot == -1


def test_floor_occupied_slots(floor, truck):
    ticket = floor.park_vehicle(truck)
    assert ticket.slot.id in floor.occupiedSlots(type(truck))


def test_floor_unparking_slot(floor: ParkingFloor, truck: Truck):
    ticket: Ticket = floor.park_vehicle(truck)
    floor.unpark_vehicle(ticket)
    assert ticket.slot.id not in floor.occupiedSlots(type(truck))


def test_floor_unparking_size(floor: ParkingFloor, truck: Truck):
    ticket: Ticket = floor.park_vehicle(truck)
    initial_size = len(floor.occupiedSlots(type(truck)))
    floor.unpark_vehicle(ticket)
    assert initial_size - 1 == len(floor.occupiedSlots(type(truck)))
