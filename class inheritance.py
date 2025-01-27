class Animal:
    def __init__ (self, name):
        self.name = name
        self.is_alive = True
    def sleep(self):
        print(f"{self.name} is sleeping")
    def eat(self):
        print(f"{self.name} is eating")
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says WOOF!!!")
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says MEOW!!!")
class Mouse(Animal):
    def speak(self):
        print(f"{self.name} says SQUEAK!!!")

dog = Dog("Scooby")
cat = Cat("Oggy")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
dog.sleep()
dog.eat()
dog.speak()
print()

print(cat.name)
print(cat.is_alive)
cat.sleep()
cat.eat()
cat.speak()
print()

print(mouse.name)
print(mouse.is_alive)
mouse.sleep()
mouse.eat()
mouse.speak()
