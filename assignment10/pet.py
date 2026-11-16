class Pet:

    # Initialize all class data members. 
    # Think of this as a C++ default constructor with initializer list
    def __init__(self, name, pet_type, age):
        self.__name = name
        self.__pet_type = pet_type
        self.__age = age

    # Accessor (getter) methods
    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__pet_type

    def get_age(self):
        return self.__age

    # Mutator (setter) methods
    def set_name(self, name):
        self.__pet_name = name

    def set_type(self, pet_type):

        if type(pet_type) != str:
            raise TypeError("Error: Non-string type entered for pet species")        
        self.__pet_type == pet_type

    def set_age(self, age):
            if age < 0:
                raise ValueError("Age cannot be negative")
            self.__age = age

    # Print pet information
    def print_info(self):
        print("Pet Information generated with print_info():")
        print(f"Pet Name: {self.__name}")
        print(f"Type: {self.__pet_type}")
        print(f"Age: {self.__age}")


    # __str__
    def __str__(self):
        return (f"Pet Name: {self.__name}\n"
                f"Type: {self.__pet_type}\n"
                f"Age: {self.__age}")