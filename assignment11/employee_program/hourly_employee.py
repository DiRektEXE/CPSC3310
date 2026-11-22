from employee import Employee

class HourlyEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, 0)  # Initialize with a salary of 0
        self.__hourly_rate = hourly_rate
        self.__hours = hours_worked

    def calculate_pay(self):
        return self.__hourly_rate * self.__hours

    def __str__(self):
        return f"Hourly Employee Name: {self.get_name()}, Hourly Rate: {self.__hourly_rate}, Hours Worked: {self.__hours}, Department: {self.get_department()}"
    