#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        if not isinstance(width, (int, float)):
            raise ValueError("Width must be a number.")
        if width <= 0:
            raise ValueError("Width must be positive.")
        self.__width = width
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        if not isinstance(height, (int, float)):
            raise ValueError("Height must be a number.")
        if height <= 0:
            raise ValueError("Height must be positive.")
        self.__height = height
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        if not isinstance(x, (int, float)):
            raise ValueError("X coordinate must be a number.")
        self.__x = x
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        if not isinstance(y, (int, float)):
            raise ValueError("Y coordinate must be a number.")
        self.__y = y


if __name__ == "__main__":
    rect = Rectangle(10, 20, 5, 5, id=1)
    print(rect.width)   # Output: 10
    print(rect.height)  # Output: 20
    print(rect.x)       # Output: 5
    print(rect.y)       # Output: 5
    print(rect.id)      # Output: 1
