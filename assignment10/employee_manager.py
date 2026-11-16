from employee import Employee
import pickle

def create_employee():
    """Prompt for employee details and return a new Employee object."""
    name = input("Name: ")
    ID_Number = input("ID Number: ")
    department = input("Department: ")
    title = input("Title: ")

    return Employee(name, ID_Number, department, title)

def add_employee(employees):
    employee = create_employee()
    employee_id = employee.get_ID_Number()

    if employee_id in employees:
        print("An employee with that ID number already exists.")
    else:
        employees[employee_id] = employee
        print("The new employee has been added.")

def save_employees(employees, filename):
    with open(filename, 'wb') as file:
        pickle.dump(employees, file)

def load_employees(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}

def edit_employee(employees):
    employee_id = input("Enter the ID number of the employee to edit: ")
    employee = employees.get(employee_id)

    if employee:
        print("\nCurrent Employee Information:")
        print(employee)

        print("\nEnter new information (leave blank to keep current value):")
        name = input(f"Name [{employee.get_name()}]: ") or employee.get_name()
        department = input(f"Department [{employee.get_department()}]: ") or employee.get_department()
        title = input(f"Title [{employee.get_title()}]: ") or employee.get_title()

        employee.set_name(name)
        employee.set_department(department)
        employee.set_title(title)

        print("The employee's information has been updated.")
    else:
        print("No employee found with that ID number.")

def lookup_employee(employees):
    employee_id = input("Enter the ID number of the employee to look up: ")
    employee = employees.get(employee_id)

    if employee:
        print("\nEmployee Information:")
        print(employee)
    else:
        print("No employee found with that ID number.")

def delete_employee(employees):
    employee_id = input("Enter the ID number of the employee to delete: ")
    if employee_id in employees:
        del employees[employee_id]
        print("The employee has been deleted.")
    else:
        print("No employee found with that ID number.")

def main():
    employees = load_employees('employees.dat')

    while True:
        print("\nMenu")
        print("--------------------------------------------")
        print("1. Look up an employee")
        print("2. Add a new employee")
        print("3. Change an existing employee's information")
        print("4. Delete an employee")
        print("5. Quit the program")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            lookup_employee(employees)
        elif choice == '2':
            add_employee(employees)
        elif choice == '3':
            edit_employee(employees)
        elif choice == '4':
            delete_employee(employees)
        elif choice == '5':
            save_employees(employees, 'employees.dat')
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()