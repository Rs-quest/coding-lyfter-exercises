import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = math.pi * (self.radius ** 2)
        print(f"El área es: {area}")


radius = int(input("Digite el radio del círculo: "))

circle = Circle(radius)
circle.get_area()