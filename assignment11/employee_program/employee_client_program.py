from employee import Employee
from salary_employee import SalaryEmployee
from hourly_employee import HourlyEmployee
from commission_employee import CommissionEmployee

def main():
    print("Employee Database")
    print("-" * 30)

    departments = {
        "Sales": [
            HourlyEmployee("Nick DeFalco", 25.00, 2080),
            SalaryEmployee("Applejack Johnson", 44000),
            SalaryEmployee("Mario Dubois", 77200)
        ],

        "Engineering": [
            SalaryEmployee("Anthony Jo", 98000),
            Employee("Stephanie Johnson", 31200)
        ],

        "Maintenance": [CommissionEmployee("Dominic Togo", 20000, 0.15, 300000),
                        HourlyEmployee("Christina Gonzalez", 19.80, 2080)],

        "HR": [HourlyEmployee("Geoffrey Dav", 65.00, 2080)]
    }

    for department, employees in departments.items():
        total_payroll = 0

        print(f"\nDepartment: {department}")

        for employee in employees:
            total_payroll += employee.calculate_pay()

            if isinstance(employee, SalaryEmployee):
                employee_type = "Salaried Employee"
            elif isinstance(employee, HourlyEmployee):
                employee_type = "Hourly Employee"
            elif isinstance(employee, CommissionEmployee):
                employee_type = "Commission Employee"
            else:
                employee_type = "Employee"

            #print(employee)
            print(f"\t{employee.get_name()}: ({employee_type}) ${employee.calculate_pay():.2f}")

            if isinstance(employee, CommissionEmployee):
                base_pay = employee.get_base_pay()
                commission = employee.get_commission()
                total_pay = employee.calculate_pay()

                if total_pay != 0:
                    commission_percentage = (commission / total_pay) * 100
                else:
                    commission_percentage = 0

                print(f"\t\tBase ${base_pay:.2f} + Commission ${commission:.2f} ({commission_percentage:.1f}% of earnings)")

        print(f"Total Payroll: ${total_payroll:.2f}")

if __name__ == "__main__":
    main()