
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def calculate_pay(self):
        return self.__salary

    def __str__(self):
        return f"Employee Name: {self.__name}, Salary: {self.__salary}"