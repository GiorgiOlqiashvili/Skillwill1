from car import Car
from electric_mixin import ElectricMixin


class ElectricCar(Car, ElectricMixin):
    def __init__(self, make: str, model: str, year: int, doors: int, battery_capacity: int):
        Car.__init__(self, make, model, year, doors)
        ElectricMixin.__init__(self, battery_capacity)

    def __str__(self):
        return f"{super(Car, self).__str__()} and a battery capacity of {self._battery_capacity} kWh"

    def __repr__(self):
        return f"{super(Car, self).__repr__()}, battery_capacity={self._battery_capacity}"


# Creating ElectricCar instance with runtime data input
def create_electric_car():
    make = input("Enter the brand of the electric car: ")
    model = input("Enter the model of the electric car: ")
    year = int(input("Enter the year of the electric car: "))
    doors = int(input("Enter the number of doors: "))
    battery_capacity = int(input("Enter the battery capacity in kWh: "))
    return ElectricCar(make, model, year, doors, battery_capacity)


# Creating and printing ElectricCar instance
electric_car = create_electric_car()
print(electric_car)
print(repr(electric_car))
