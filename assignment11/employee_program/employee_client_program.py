from salary_employee import SalaryEmployee
from hourly_employee import HourlyEmployee
from commission_employee import CommissionEmployee

def main():
    print("Employee Database")
    print("-" * 30)

    departments = {
    "Engineering": [SalaryEmployee("Anthony Jo", 98000)],
    "HR": [SalaryEmployee("Emily Smith", 65000)],
    "Maintenance": [CommissionEmployee("Dominic Togo", 20000.00, 0.62, 45000.00), HourlyEmployee("Christina Gonzalez", 30000.00, 40)]
}

    

    for department, employees in departments.items():
        total_payroll = 0
        
        print(f"\nDepartment: {department}")
        
        for employee in employees:
            
            total_payroll += employee.calculate_pay()
            
            #print(employee)
            print(f"\t{employee.get_name()}: ({employee.__class__.__name__}) ${employee.calculate_pay():.2f}") 
            

            if isinstance(employee, CommissionEmployee):
                base_pay = employee.get_base_pay()
                commission = employee.get_commission()
                commission_percentage = (commission / employee.calculate_pay()) * 100

                print(f"\t\tBase {base_pay:.2f} + Commission {commission:.2f} ({commission_percentage:.1f}% of earnings)")
        
        print(f"Total Payroll: ${total_payroll:.2f}")







if __name__ == "__main__":
    main()