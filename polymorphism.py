from abc import abstractmethod
class Shapes:
    @abstractmethod
    def area(self):
        pass
class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print(f"{3.14*self.radius*self.radius} cm²")
class Square(Shapes):
    def __init__(self, side):
        self.side = side
    def area(self):
        print(f"{self.side*self.side} cm²")
class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        print(f"{self.base*self.height/2} cm²")
class Roti(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        self.radius = radius
        super().area()


shape = [Circle(2), Square(4), Triangle(3,4), Roti("ghee", 3)]        
for i in shape:
    i.area()