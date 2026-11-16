from patient import Patient
from procedure import Procedure


def create_patient():
    """Prompt for name, address, and phone, and return a new Patient."""
    """Collect patient information and return a new Patient."""

    first_name = input("First name: ")
    middle_name = input("Middle name: ")
    last_name = input("Last name: ")
    address = input("Address: ")
    city = input("City: ")
    state = input("State: ")
    zip_code = input("ZIP: ")
    phone = input("Phone: ")
    emergency_contact = input("Emergency contact: ")
    emergency_phone = input("Emergency phone: ")

    return Patient(
        first_name, middle_name, last_name, address, city, state,
        zip_code, phone, emergency_contact, emergency_phone
    )


def create_procedure():
    """Prompt for procedure details and return a new Procedure.

    The charge must be validated: keep re-prompting until the user
    enters a number greater than 0.
    """
    description = input("Procedure description: ")
    date = input("Procedure date (YYYY-MM-DD): ")
    practitioner = input("Practitioner: ")

    while True:
        try:
            charge = float(input("Charge: "))
            if charge <= 0:
                print("Charge must be a positive number. Please try again.")
                continue
            break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return Procedure(description, date, practitioner, charge)


def main():
    patient = create_patient()

    procedures = []
    print("\nAdd one or more procedures (enter 'n' to stop).")

    while True:
        add_procedure = input("Would you like to add a procedure? (y/n): ").strip().lower()
        if add_procedure == 'y':
            procedure = create_procedure()
            procedures.append(procedure)
        elif add_procedure == 'n':
            break
        elif type(add_procedure) is not str:
            print("Invalid input. Please enter a string 'y' or 'n'.")
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
   
    print("\nPatient and Procedure Information:")
    print(patient)
    total_charge = 0.0
    for procedure in procedures:
        print()
        print(procedure)
        total_charge += procedure.get_charge()

    print(f"\nTotal Charge: ${total_charge:.2f}")

if __name__ == "__main__":
    main()