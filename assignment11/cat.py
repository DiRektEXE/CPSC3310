from animal import Animal

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def set_name(self, name):
        self.__name = name

    def speak(self):
        return "Meow!"

    def __str__(self):
        return f"Cat Name: {self.get_name()}"