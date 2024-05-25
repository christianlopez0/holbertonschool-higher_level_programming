#!/usr/bin/python3
# Mixin classes
class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


# Dragon class inheriting from SwimMixin and FlyMixin
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")


# Instantiate Dragon object
draco = Dragon()

# Tests
draco.swim()
draco.fly()
draco.roar()
