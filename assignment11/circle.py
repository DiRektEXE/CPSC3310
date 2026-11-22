from shape import Shape

class Circle(Shape):


    def __init__(self, radius):
        self.__radius = radius


    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def area(self):
        return 3.14 * (self.__radius ** 2)

    
    def __str__(self):
        return f"Shape: Circle\nRadius: {self.__radius}\n\n"
