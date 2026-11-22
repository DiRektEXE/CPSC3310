from employee import Employee

class CommissionEmployee(Employee):
    def __init__(self, name, base_pay, commission_rate, sales):
        super().__init__(name, base_pay)
        self.__commission_rate = commission_rate
        self.__sales = sales

    def get_base_pay(self):
        return self.get_salary()

    def get_commission(self):
        return self.__commission_rate * self.__sales

    def get_sales(self):
        return self.__sales

    def calculate_pay(self):
        return self.get_salary() + self.get_commission()

    def __str__(self):
        return f"Commission Employee Name: {self.get_name()}, Base Pay: {self.get_salary()}, Commission: {self.get_commission()}, Sales: {self.__sales}"