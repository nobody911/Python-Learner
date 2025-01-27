from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def go(self):
        print("You are driving a car")
    def stop(self):
        print("You are stopping a car")
class Motorcycle(Vehicle):
    def go(self):
        print("You are driving a motorcycle")
    def stop(self):
        print("You are stopping a motorcycle")
class Boat(Vehicle):
    def go(self):
        print("You are driving a boat")
    def stop(self):
        print("You are stopping a boat")
car = Car()
car.go()
car.stop()
print()
motorcycle = Motorcycle()
motorcycle.go()
motorcycle.stop()
print()
boat = Boat()
boat.go()
boat.stop()
# vehicle = Vehicle()