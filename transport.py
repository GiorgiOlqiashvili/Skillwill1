from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, make: str, model: str, year: int):
        self._make = make
        self._model = model
        self._year = year

    @abstractmethod
    def vehicle_type(self):
        pass

    def __str__(self):
        return f"{self._make} {self._model} ({self._year})"

    def __repr__(self):
        return f"{self.__class__.__name__}(make='{self._make}', model='{self._model}', year={self._year})"
