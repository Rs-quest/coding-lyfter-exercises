
"""
MULTIPLE INHERITANCE

Multiple inheritance allows a class to inherit attributes
and methods from more than one parent class.

It is useful for:
- Code reuse: avoiding duplicated code.
- Combining different functionalities in one class.
- Using mixins to add specific behaviors to different classes.

However, it can create conflicts when two parent classes
have methods with the same name.

Python uses Method Resolution Order (MRO) to determine
which method should be executed.
"""


# Parent classes

class Animal:

    def eat(self):
        print("This animal is eating.")

    def move(self):
        print("Animal is moving.")


class Flyable:

    def fly(self):
        print("This animal can fly.")

    def move(self):
        print("This animal is flying.")


class Swimmable:

    def swim(self):
        print("This animal can swim.")


# Multiple inheritance

class Duck(Animal, Flyable, Swimmable):
    pass


# Create an instance

duck = Duck()

print("Duck abilities:")

duck.eat()
duck.fly()
duck.swim()


# Testing Method Resolution Order (MRO)

print("\nMethod Resolution Order:")
print(Duck.__mro__)


# Testing method name conflict

print("\nTesting method conflict:")

duck.move()
