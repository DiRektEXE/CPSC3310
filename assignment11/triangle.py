from shape import Shape

class Triangle(Shape):

    def __init__(self, name, base, t_height):
        super().__init__(name)
        self.__base = base
        self.__t_height = t_height

    def set_base(self, base):
        self.__base = base

    def set_triangle_height(self, t_height):
        self.__t_height = t_height

    def get_base(self):
        return self.__base

    def get_triangle_height(self):
        return self.__t_height

    def area(self):
        return (self.__base * self.__t_height) / 2

    def __str__(self):
        return f"Shape: Triangle\n Base: {self.__base}\nHeight: {self.__height}\nArea: {self.area():.2f}\n\n"