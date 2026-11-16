

class Employee:
    def __init__(self, name, ID_Number, department , title):
        self.__name = name
        self.__ID_Number = ID_Number
        self.__department = department
        self.__title = title

    # Gettter Methods
    def get_name(self):
        return self.__name

    def get_ID_Number(self):
        return self.__ID_Number

    def get_title(self):
        return self.__title

    def get_department(self):
        return self.__department

    # Setter Methods
    def set_name(self, name):
        self.__name = name

    def set_ID_Number(self, ID_Number):
        self.__ID_Number = ID_Number

    def set_title(self, title):
        self.__title = title

    def set_department(self, department):
        self.__department = department

    # __str__ method to return a string representation of the employee object
    def __str__(self):
        return (
            f"Name: {self.__name}\n"
            f"ID Number: {self.__ID_Number}\n"
            f"Department: {self.__department}\n"
            f"Title: {self.__title}"
        )    
    
    # Method to display employee information
    def display_employee_info(self):
        print(f"Name: {self.__name}")
        print(f"ID Number: {self.__ID_Number}")
        print(f"Department: {self.__department}")
        print(f"Title: {self.__title}")