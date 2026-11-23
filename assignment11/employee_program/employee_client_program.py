from salary_employee import SalaryEmployee
from hourly_employee import HourlyEmployee
from commission_employee import CommissionEmployee

def main():
    print("Employee Database")
    print("-" * 30)

    departments = {
    "Engineering": [SalaryEmployee("Anthony Jo", 98000)],
    "HR": [SalaryEmployee("Emily Smith", 65000)],
    "Software Engineering": [CommissionEmployee("Anthony Jo", 98000)]}

    total_payroll = 0

    for department, employees in departments.items():
        
        print(f"\nDepartment: {department}")
        
        for employee in employees:
            
            total_payroll += employee.calculate_pay()
            
            #print(employee)
            print(f"\t{employee.get_name()} ({employee.__class__.__name__}): ${employee.calculate_pay():.2f}") 
            print("-" * 30)

        if isinstance(employee, CommissionEmployee):
            base_pay = employee.get_base_pay()
            commission = employee.get_commission()
            commission_percentage = (employee.get_commission() / employee.calculate_pay()) * 100

            print(f"({commission_percentage:.1f}% of earnings)")
        
        print(f"Total Payroll: ${total_payroll:.2f}")







if __name__ == "__main__":
    main()