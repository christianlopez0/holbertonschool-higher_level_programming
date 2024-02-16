#!/usr/bin/python3
""" rectangle class"""
from models.base import Base


class Rectangle(Base):
    """makes a new rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
  
    @property
    def width(self):
        """get width"""
        return self.__width

    @property
    def height(self):
        """get height"""
        return self.__height

    @property
    def x(self):
        """get x"""
        return self.__x

    @property
    def y(self):
        """get y"""
        return self.__y

    @width.setter
    def width(self, value):
        """sets width"""
        self.validator("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """sets height"""
        self.validator("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        self.validator("x", value)
        """sets x"""
        self.__x = value

    @y.setter
    def y(self, value):
        """sets y"""
        self.validator("y", value)
        self.__y = value