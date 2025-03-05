class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Predator, Prey):
    pass

rabbit = Rabbit("Jack")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
rabbit.eat()
print()
hawk.hunt()
hawk.eat()
# hawk.flee()
print()
fish.flee()
fish.hunt()
fish.eat()
print()
