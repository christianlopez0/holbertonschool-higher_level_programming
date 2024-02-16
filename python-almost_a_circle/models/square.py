#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    """Creates a new square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"