
class Employee:
    def __init__(self, name, salary, department=None):
        self.__name = name
        self.__salary = salary
        self.__department = department

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def get_department(self):
        return self.__department

    def calculate_pay(self):
        return self.__salary

    def __str__(self):
        return f"Employee Name: {self.__name}, Salary: {self.__salary}, Department: {self.__department}"