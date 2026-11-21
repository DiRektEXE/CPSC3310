
# Shape Superclass
class Shape:

    def area(self):
        return 0

# Rectangle Subclass
class Rectangle(Shape):

    def __init__(self, length, width):
        self.__length = length
        self.__width = width


    length = int(input("Enter a length value for the rectangle: "))
    width = int(input("Enter a width value for the rectangle: "))

    def area(self):
        return 