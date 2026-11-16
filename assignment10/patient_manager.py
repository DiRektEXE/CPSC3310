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
    # TODO - create a loop to allow a user adding 0 to multiple procedures for the patient
    #        use create_procedure() to instantiate each procedure object
   
    print("\nPatient and Procedure Information:")
    # TODO - print the patient information, followed by all procedure information
    #        Total the cost of all procedures and print the sum

    


if __name__ == "__main__":
    main()