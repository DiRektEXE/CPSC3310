from shape import Shape

# Rectangle Subclass
class Rectangle(Shape):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    # Setter Methods
    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    # Getter Methods
    def get_width(self):
        return self.__width

    def get_height(self):
            return self.__height

    # String representation of class data
    def __str__(self):
        return f"Shape: Rectangle\nWidth: {self.width}\nHeight: {self.height}"
    
    length = int(input("Enter a length value for the rectangle: "))
    width = int(input("Enter a width value for the rectangle: "))

    def area(self):
        return self.__width * self.__height