
# Shape Superclass
class Shape:

    def area(self):
        return 0

# Rectangle Subclass
class Rectangle(Shape):

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    # Setter Methods
    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    # Getter Methods
    def get_length(self):
        return self.__length

    def get_width(self):
            return self.__width

    def __str__(self):
        return f"Shape: Rectangle\nLength: {self.length}\nWidth: {self.width}"
    
    length = int(input("Enter a length value for the rectangle: "))
    width = int(input("Enter a width value for the rectangle: "))

    def area(self):
        return 