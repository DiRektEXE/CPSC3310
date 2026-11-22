from employee import Employee

class SalaryEmployee(Employee):
    def __init__(self, name, annual_salary, department=None):
        super().__init__(name, department)
        self.__annual_salary = annual_salary

    def calculate_pay(self):
        return self.__annual_salary

    def __str__(self):
        return f"Salary Employee Name: {self.get_name()}, Annual Salary: {self.get_salary}, Department: {self.get_department()}"