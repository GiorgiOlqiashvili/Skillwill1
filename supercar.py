from car import Car


class SuperCar(Car):
    def __init__(self, make: str, model: str, year: int, doors: int, top_speed: int):
        super().__init__(make, model, year, doors)
        self.__top_speed = top_speed
        self.__validate_top_speed()

    def __validate_top_speed(self):
        if self.__top_speed <= 0:
            raise ValueError("Top speed must be a positive number.")

    def vehicle_type(self):
        return "SuperCar"

    def __str__(self):
        return f"{super().__str__()} with a top speed of {self.__top_speed} km/h"

    def __repr__(self):
        return f"{super().__repr__()}, top_speed={self.__top_speed}"

    @classmethod
    def create_supercar(cls):
        make = input("Enter the brand of the supercar: ")
        model = input("Enter the model of the supercar: ")
        year = int(input("Enter the year of the supercar: "))
        top_speed = int(input("Enter the top speed of the supercar: "))
        return cls(make, model, year, top_speed)



