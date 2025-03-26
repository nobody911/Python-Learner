class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
class Wheel:
    def __init__(self, wheel_size):
        self.wheel_size = wheel_size
class Car:
    def __init__(self, horsepower, wheel_size, model):
        self.model = model
        self.engine = Engine(horsepower)
        self.size = [Wheel(wheel_size) for wheel in range(4)]
    def display_car(self):
        return f"The {self.model} has {self.engine.horsepower} hp of horsepower and wheel size of {self.size[0].wheel_size} in"

car1 = Car(horsepower=800, wheel_size=18, model="Toyota")
car2 = Car(horsepower=1200, wheel_size=10, model="Omni")
car3 = Car(horsepower=600, wheel_size=15, model="Fortuner")

print(car1.display_car())
print(car2.display_car())
print(car3.display_car())