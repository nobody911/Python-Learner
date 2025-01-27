class Shape:
    def __init__(self, color, is_filled, shape):
        self.shape = shape
        self.color = color
        self.is_filled = is_filled
        
    def describe(self):
        print(f"The {self.shape} is {self.color} and {"is filled"if self.is_filled else "is not filled"}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled, shape)
        self.radius = radius

    def describe(self):
        print(f"The area of the circle is {3.14*self.radius**2}cm^2")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled, shape)
        self.side = side

    # def area(self):
    #     print(f"The area of the square is {self.side**2}cm^2")
    #     super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, base, height):
        super().__init__(color, is_filled, shape)
        self.base = base
        self.height = height

    def area(self):
        print(f"The area of the triangle is {0.5*self.base*self.height}cm^2")
        super().describe()

circle = Circle(color = "red", is_filled=True, radius=2, shape = "circle")
square = Square(color = "blue", is_filled=False, side=3, shape = "square")
triangle = Triangle(color = "yellow", is_filled=True, base=2, height=5, shape = "triangle")
circle.describe()
print()
square.describe()