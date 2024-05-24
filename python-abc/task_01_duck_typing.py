#!/usr/bin/python3
from abc import ABC, abstractmethod
import math

# Define the abstract class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# Concrete class Circle inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * abs(self.radius)

# Concrete class Rectangle inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Function to print shape information
def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

# Testing
circle = Circle(-5)  # Negative radius for testing
rectangle = Rectangle(4, 6)

print("Circle:")
shape_info(circle)

print("\nRectangle:")
shape_info(rectangle)

