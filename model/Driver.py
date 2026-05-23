from dataclasses import dataclass

@dataclass(frozen=True)
class Driver:
    driverId: int
    forename: str
    surname: str
