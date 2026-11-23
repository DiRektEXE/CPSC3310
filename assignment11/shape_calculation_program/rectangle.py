from shape import Shape

# Rectangle Subclass
class Rectangle(Shape):

    def __init__(self, name, width, height):
        super().__init__(name)
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

    def area(self):
            return self.__width * self.__height

    # String representation of class data
    def __str__(self):
        return f"Shape: Rectangle\nWidth: {self.get_width()}\nHeight: {self.get_height()}\n\n"  