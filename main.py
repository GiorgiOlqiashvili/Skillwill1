from car import Car
from supercar import SuperCar
from van import Van
from bus import Bus


class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @classmethod
    def create_vehicle(cls):
        brand = cls.get_string_input("Enter vehicle brand: ")
        model = input("Enter vehicle model: ")
        year = cls.get_int_input("Enter vehicle year: ")
        return cls(brand, model, year)

    @staticmethod
    def get_string_input(prompt):
        while True:
            value = str(input(prompt))
            if value.isalpha():
                return value
            else:
                print("Invalid input. Please enter a valid string.")

    @staticmethod
    def get_int_input(prompt):
        while True:
            value = input(prompt)
            if value.isdigit():
                return int(value)
            else:
                print("Invalid input. The year must be an integer. Please try again.")

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

    @classmethod
    def input(cls, param):
        pass


def main():
    while True:
        print("Choose the type of vehicle to create:")
        print("1. Car")
        print("2. SuperCar")
        print("3. Van")
        print("4. Bus")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            vehicle = Car.create_car()
        elif choice == '2':
            vehicle = SuperCar.create_supercar()
        elif choice == '3':
            vehicle = Van.create_van()
        elif choice == '4':
            vehicle = Bus.create_bus()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        print(f"Result - {vehicle}")


if __name__ == "__main__":
    main()



