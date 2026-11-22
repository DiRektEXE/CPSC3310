from shape import Shape

class Circle(Shape):


    def __init__(self, radius):
        self.__radius = radius

    # Constant for Pi
    PI = 3.14

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def area(self):
        return self.__radius * (PI**2)
    
    def __str__(self):
        return f"Shape: Circle\nRadius: {self.__radius}\n\n"
