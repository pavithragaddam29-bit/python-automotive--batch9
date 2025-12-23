class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def calculate_area(shape: Shape):
    print(f"Area: {shape.area()}")

circle = Circle(5)
rectangle = Rectangle(4, 6)

calculate_area(circle)  # Output: Area: 78.5
calculate_area(rectangle)  # Output: Area: 24
