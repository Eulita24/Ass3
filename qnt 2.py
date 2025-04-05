import math

# Base class: Shape
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override the 'area' method.")

# Subclass: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

# Subclass: Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Function to calculate the total area
def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()  # Polymorphism in action: Calls the appropriate `area` method
    return total

# Example usage
shapes = [
    Circle(5),            # Circle with radius 5
    Rectangle(4, 6),      # Rectangle with width 4 and height 6
    Circle(3),            # Circle with radius 3
    Rectangle(2, 3)       # Rectangle with width 2 and height 3
]

print("Total Area:", total_area(shapes))
