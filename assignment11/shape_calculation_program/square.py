from shape import Shape

class Square(Shape):

    def __init__(self, name, side):
        super().__init__(name)
        self.__side = side

    def set_side(self, side):
        self.__side = side

    def get_side(self):
        return self.__side

    def area(self):
        return self.__side ** 2

    def __str__(self):
        return f"Shape: Square\nDimensions: {self.__side} x {self.__side}\nArea: {self.area():.2f}\n\n"