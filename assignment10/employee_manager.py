from employee import Employee

def create_employee():
    """Prompt for employee details and return a new Employee object."""
    name = input("Name: ")
    ID_Number = input("ID Number: ")
    department = input("Department: ")
    title = input("Title: ")

    return Employee(name, ID_Number, department, title)

