
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        print('height',height,)

        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        print("radius",radius)
    def area(self):
        print( 3.14159 * self.radius * self.radius)


