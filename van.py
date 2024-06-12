from transport import Transport


class Van(Transport):
    def __init__(self, make: str, model: str, year: int, cargo_space: float):
        super().__init__(make, model, year)
        self._cargo_space = cargo_space
        self.__validate_cargo_space()

    def __validate_cargo_space(self):
        if self._cargo_space <= 0:
            raise ValueError("Cargo space must be a positive number.")

    def vehicle_type(self):
        return "Van"

    def __str__(self):
        return f"{super().__str__()} with {self._cargo_space} cubic meters of cargo space"

    def __repr__(self):
        return f"{super().__repr__()}, cargo_space={self._cargo_space}"


    @classmethod
    def create_van(cls):
        make = input("Enter the brand of the van: ")
        model = input("Enter the model of the van: ")
        year = int(input("Enter the year of the van: "))
        cargo_space = float(input("Enter the cargo space in cubic meters: "))
        return cls(make, model, year, cargo_space)