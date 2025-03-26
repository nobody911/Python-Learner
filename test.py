class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
class Wheel:
    def __init__(self, size):
        self.size = size
class Car:
    def __init__(self, horse_power, wheel_size, model, year):
        self.model = model
        self.year = year
        self.engine = Engine(horsepower=horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]
    def print_wheel(self):
        return f"{self.engine.horsepower}, {self.model}, {self.year}, {self.wheels[0].size}"

car1 = Car(horse_power=200, wheel_size=18, model="Tesla", year=2021)
car2 = Car(horse_power=600, wheel_size=14, model="Mercedes", year=2024)

print(car1.print_wheel())
print(car2.print_wheel())