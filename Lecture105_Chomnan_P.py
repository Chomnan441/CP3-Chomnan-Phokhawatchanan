class Vehicle:
    lecenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")
class Car(Vehicle):
    pass

class Pickup(Vehicle):
    color = ""
    def colorPickup(self):
        print(self.color)

class Van(Vehicle):
    pass

Car1=Car()
Car1.turnOnAirConditioner()
Pickup1=Pickup()
Pickup1.turnOnAirConditioner()
Pickup1.color="red"
Pickup1.colorPickup()
Van1=Van()
Van1.turnOnAirConditioner()