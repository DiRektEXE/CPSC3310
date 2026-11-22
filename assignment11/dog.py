from animal import Animal

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def set_name(self, name):
        self.__name = name

    def speak(self):
        return "Woof!"

    def __str__(self):
        return f"Dog Name: {self.get_name()}"