
class Animal:

    def eat(self):
        print("This animal is eating.")


class Flyable:

    def fly(self):
        print("This animal can fly.")


class Swimmable:

    def swim(self):
        print("This animal can swim.")


class Duck(Animal, Flyable, Swimmable):
    pass


# Create an instance

duck = Duck()

duck.eat()
duck.fly()
duck.swim()
