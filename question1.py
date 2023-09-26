class Vehicle:
    def __init__(self, name, speed, average):
        self.name_of_vehicle = name
        self.max_speed = speed
        self.average_of_vehicle = average

class Car(Vehicle):
    def __init__(self, seats, name, speed, average):
        super().__init__(name, speed, average)
        pass

    def seating_capacity(self):
        return f"Name: {self.name_of_vehicle}"



