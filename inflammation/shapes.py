import numpy as np

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return np.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height

my_cirlce = Circle(5)
my_rect = Rectangle(5, 10)

