from abc import ABC
from weakref import WeakValueDictionary


class NotaRegisteredTicketException(Exception):
    """Ticket is not registered"""


class BaseTicket(ABC):
    pass


class Ticket(BaseTicket):
    tickets = WeakValueDictionary()

    def __init__(self, floor, slot, *args, **kwargs):
        self.floor = floor
        self.slot = slot
        self.parkingLot = None

    def generateTicket(self) -> str:
        return f"{self.parkingLot.id}_{self.floor.id}_{self.slot.id}"

    def openTicket(self) -> BaseTicket:
        self.tickets[str(self)] = self

    def setParkingLot(self, parkingLot: str) -> None:
        self.parkingLot = parkingLot

    @classmethod
    def getTicket(cls, ticket: str) -> BaseTicket:
        try:
            return cls.tickets[ticket]
        except KeyError:
            raise NotaRegisteredTicketException(
                f"{ticket} is not an open ticket")

    def closeTicket(self) -> None:
        self.tickets.pop(str(self))

    def __str__(self) -> str:
        return f"{self.parkingLot.id}_{self.floor.id}_{self.slot.id}"
