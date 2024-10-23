class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"Starting {self.make} {self.model}")

    def stop(self):
        print(f"Stopping {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def honk(self):
        print("Honk honk!")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, cc):
        super().__init__(make, model, year)
        self.cc = cc

    def rev_engine(self):
        print("Vroom vroom!")