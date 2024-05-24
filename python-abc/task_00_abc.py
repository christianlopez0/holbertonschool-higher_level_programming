#!/usr/bin/python3
from abc import ABC, abstractmethod

# Setting up the Abstract Class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Implementing the Subclasses
class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Testing
dog = Dog()
cat = Cat()

print("Dog says:", dog.sound())
print("Cat says:", cat.sound())
