class Rectangle:
    def __init__(self, height, width):
        self._height = height
        self._width = width

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width cannot be less than or equal to 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height cannot be less than or equal to 0")
            
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

rectangle = Rectangle(height=3, width=4)

rectangle.height = 6
rectangle.width = 7

del rectangle.width
del rectangle.height

# print(rectangle.height)
# print(rectangle.width)