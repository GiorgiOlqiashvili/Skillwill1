class Heart:
    def __init__(self, usage):
        self.usage = usage

    @property
    def state(self):
        if self.usage > 70:
            return "high blood pressure"
        else:
            return "feeling good"


class Brain:
    def __init__(self, usage):
        self.usage = usage

    @property
    def state(self):
        if self.usage > 90:
            return "tired"
        else:
            return "rested"


class Leg:
    def __init__(self, moving_speed):
        self.moving_speed = moving_speed

    @property
    def state(self):
        if self.moving_speed > 10:
            return "running"
        else:
            return "walking" if self.moving_speed > 0 else "standing"


class Person:
    def __init__(self, heart_usage, brain_usage):
        self.heart = Heart(heart_usage)
        self.brain = Brain(brain_usage)
        self.legs = []

    def add_leg(self, moving_speed):
        leg = Leg(moving_speed)
        self.legs.append(leg)


person = Person(heart_usage=60, brain_usage=85)
print(person.heart.state)
print(person.brain.state)

person.add_leg(moving_speed=7)
person.add_leg(moving_speed=15)

for leg in person.legs:
    print(leg.state)
