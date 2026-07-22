class FlightFullError(Exception):
    def __init__(self, flight_code: str) -> None:
        super().__init__(f"Flight {flight_code} has not seats available.")

class OverweightLuggageError(Exception):
    def __init__(self, weight: float, max_weight: float, luggage_type: str) -> None:
        super().__init__(f"{luggage_type} weights {weight} kg, exceeding the maximum allowed of {max_weight} kg.")

class EmptyQueueError(Exception):
    def __init__(self) -> None:
        super().__init__("No passengers are on the waiting list.")
