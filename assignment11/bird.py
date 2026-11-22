from animal import Animal

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def set_name(self, name):
        self.__name = name

    def speak(self):
        return "Tweet!"

    def __str__(self):
        return f"Bird Name: {self.get_name()}"