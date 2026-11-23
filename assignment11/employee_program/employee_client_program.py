from salary_employee import SalaryEmployee
from hourly_employee import HourlyEmployee
from commission_employee import CommissionEmployee

def main():
    print("Employee Database")
    print("-" * 30)

    departments = {
    "Engineering": [SalaryEmployee("Anthony Jo", 98000)],
    "HR": [SalaryEmployee("Emily Smith", 65000)]}

    for department, employees in departments.items():
        print(f"\nDepartment: {department}")
        for employee in employees:
            print(employee)
            print(f"Calculated Pay: {employee.calculate_pay()}")
            print("-" * 30)








if __name__ == "__main__":
    main()