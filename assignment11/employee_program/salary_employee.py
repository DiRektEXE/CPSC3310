from employee import Employee

class SalaryEmployee(Employee):
    def __init__(self, name, annual_salary):
        super().__init__(name, annual_salary)

    def calculate_pay(self):
        return self.get_salary()

    def __str__(self):
        return f"Salary Employee Name: {self.get_name()}, Annual Salary: {self.get_salary()}"