class Passenger:
    def __init__(self, name: str, document_id: int, booking_ref: str, is_vip: bool):
        self.name = name
        self.__document_id = document_id
        self.booking_ref = booking_ref
        self.is_vip = is_vip

    def get_masked_id(self):
        __id = ""
        id_text = str(self.__document_id)
        _document_id = range(len(id_text))
        for i in _document_id:
            if i < (len(_document_id) - 4):
                __id = __id + "*"
            else:
                __id = __id + id_text[i]
        return __id

    def get_name(self):
        return self.name


class Flight:
    def __init__(
        self,
        code: str,
        destination: str,
        departure: str,
        capacity: int,
        _assigned_seats: list,
        _boarding_passes,
    ):
        self.code = code
        self.destination = destination
        self.departure = departure
        self.capacity = capacity
        self._assigned_seats: list[int] = []
        self._boarding_passes = _boarding_passes

    def available_seats(self) -> int:
        return self.capacity - len(self._assigned_seats)

    def is_full(self) -> bool:
        return self.available_seats() <= 0

    def assign_seat(self):
        if self.is_full():
            raise FlightFullError("There are no available seats")
        seat_number = len(self._assigned_seats) + 1
        self._assigned_seats.append(seat_number)
        return seat_number

    def __iter__(self):
        return iter(self._boarding_passes)
