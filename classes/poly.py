class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print( 3.14159 * self.radius * self.radius)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print( self.length * self.width)

r =Rectangle(4,5)
r.area()
c=Circle(9)

c.area()