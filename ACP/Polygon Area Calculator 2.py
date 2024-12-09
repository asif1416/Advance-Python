from abc import ABC, abstractmethod

class Polygon(ABC):
    """Abstract base class for polygons."""

    @abstractmethod
    def area(self):
        """Calculates the area of the polygon."""
        pass

class Triangle(Polygon):
    """Represents a triangle."""

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Polygon):
    """Represents a rectangle."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    """Represents a square."""

    def __init__(self, side):
        super().__init__(side, side)

if __name__ == "__main__":
    triangle = Triangle(5, 10)
    rectangle = Rectangle(4, 6)
    square = Square(5)

    print(f"Area of triangle: {triangle.area()}")
    print(f"Area of rectangle: {rectangle.area()}")
    print(f"Area of square: {square.area()}")