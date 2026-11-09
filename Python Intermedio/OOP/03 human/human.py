#Este ejercicio me costó un poco entenderlo al final con la composicion, haciendo print a todo, pero despues de algunos intentos lo decidí dejar así aunque igual no haya un programa ejecutable. 

class Head:
    pass
class Hand:
    pass
class Feet:
    pass
class Arm:
    def __init__(self, hand):
        self.hand = hand
class Leg:
    def __init__(self, feet):
        self.feet = feet
class Torso:
    def __init__(self, right_arm, left_arm, right_leg, left_leg):
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg
class Human:
    def __init__(self, head, torso):
        self.head = head
        self.torso = torso

head = Head()
right_hand = Hand()
left_hand = Hand()
right_feet = Feet()
left_feet = Feet()


right_arm = Arm(right_hand)
left_arm = Arm(left_hand)


right_leg = Leg(right_feet)
left_leg = Leg(left_feet)


torso = Torso(right_arm, left_arm, right_leg, left_leg)


human = Human(head, torso)


print(human.head)
print(human.torso)
print(human.torso.right_arm.hand)
print(human.torso.left_arm.hand)
print(human.torso.right_leg.feet)
print(human.torso.left_leg.feet)
