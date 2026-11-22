from employee import Employee

class CommissionEmployee(Employee):
    def __init__(self, name, commission_rate, sales):
        super().__init__(name)
        self.__commission_rate = commission_rate
        self.__sales = sales

    def get_commission_rate(self):
        return self.__commission_rate

    def get_sales(self):
        return self.__sales

    def calculate_pay(self):
        return self.__commission_rate * self.__sales

    def __str__(self):
        return f"Commission Employee Name: {self.get_name()}, Commission Rate: {self.__commission_rate}, Sales: {self.__sales}, Department: {self.get_department()}"