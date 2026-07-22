class FlightFullError(Exception):
    def __init__(self, flight_code: str) -> None:
        super().__init__(f"flight {flight_code} has no seats available.")

class OverweightLuggageError(Exception):
    def __init__(self, weight: float, max_weight: float, luggage_type: str) -> None:
        super().__init__(f"{luggage_type} weighs {weight} kg, exceeding the maximum allowed weight of {max_weight} kg.")

class EmptyQueueError(Exception):
    def __init__(self) -> None:
        super().__init__("No passengers are on the waiting list.")
