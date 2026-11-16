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