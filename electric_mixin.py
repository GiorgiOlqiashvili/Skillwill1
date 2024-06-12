class ElectricMixin:
    def __init__(self, battery_capacity: int):
        self._battery_capacity = battery_capacity
        self.__validate_battery_capacity()

    def __validate_battery_capacity(self):
        if self._battery_capacity <= 0:
            raise ValueError("Battery capacity must be a positive number.")

    def charge(self):
        return f"Charging the battery with capacity {self._battery_capacity} kWh."

#     კომპოზიცია და მიქსინგი
