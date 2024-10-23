class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

class Engine:
    def start(self):
        print("Engine started")

car = Car()
car.start()  # Output: Engine started