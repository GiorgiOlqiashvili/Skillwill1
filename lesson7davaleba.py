from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.current_speed = 0

    def start_engine(self):
        return "car started"

    def stop_engine(self):
        return "car stopped"


class SportCar(Car):
    def start_engine(self):
        parent_start = super().start_engine()
        print(parent_start)
        print(f"Max speed is {self.max_speed} km/h")

    def stop_engine(self):
        parent_stop = super().stop_engine()
        print(parent_stop)
        self.current_speed = 0
        print(f"Current speed is {self.current_speed} km/h")


if __name__ == "__main__":
    my_sport_car = SportCar(max_speed=100)
    my_sport_car.start_engine()
    my_sport_car.stop_engine()
