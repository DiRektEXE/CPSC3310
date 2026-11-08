import os
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Always read/write email.dat next to this script, regardless of the
# folder the program is run from.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(SCRIPT_DIR, 'email.dat')

def main():
    """Load the emails, run the menu loop, and save after each change."""
    # TODO - Load emails, then loop reading a choice and calling the
    #        matching function below until the user quits, saving after
    #        add/change/delete.

    # Load the saved email dictionary.
    emails = load_emails()

    # Initialize choice variable
    choice = 0

    while choice != QUIT:

        # Get user's menu choice
        choice = get_user_choice()

        # Process the choice
        if choice == LOOK_UP:
            look_up(emails)

        elif choice == ADD:
            add(emails)

        elif choice == CHANGE:
            change(emails)

        elif choice == DELETE:
            delete(emails)



def load_emails():
    """Load and return the saved emails dictionary (or an empty one)."""
    # TODO - Unpickle FILENAME; return an empty dict if it doesn't exist
    #        or is empty.
    try:
        with open(FILENAME, "rb") as file:
            return pickle.load(file)
        
    except (FileNotFoundError, EOFError):
        return {}



def get_user_choice():
    """Display the menu and return a validated choice."""
    # TODO - Print the menu, read a choice, and keep re-prompting until
    #        it's a valid menu option.
    print()
    print("Name | Email Address Map")
    print("------------------------")
    print("1. Look up an email")
    print("2. Add an email")
    print("3. Change an email")
    print("4. Delete an email")
    print("5. Quit the program")
    print()

    choice = int(input("Enter your choice: "))

    while choice < 1 or choice > 5:
        choice = int(input("Enter a valid choice: "))

    return choice
    


def look_up(emails):
    """Print the email address for a name the user enters, if found."""
    name = input("Enter a name: ")
    print(emails.get(name, "Not Found.")) # This is print(emails[name]) with error handling



def add(emails):
    """Add a new name/address pair if the name isn't already present."""
    name = input("Enter a name: ")
    email = input("Enter an email address: ")

    if name not in emails:
        emails[name] = email
    else:
        print("This entry already exists.")



def change(emails):
    """Update the address for an existing name."""
    name = input("Enter a name: ")
    if name in emails:
        email = input("Enter a new email address: ")
        emails[name] = email
    else:
        print("That name was not found.")



def delete(emails):
    """Remove a name/address pair."""
    # del dictionary[key] to delete entries
    # if a key isn't found, a KeyError exception is raised
    # Keys must be immutable
    # use dictionary.clear() to erase everything
    # dictionary.get(key, default) Get value associated with key. Default is returned if key not found
    # dictionary.items() returns all key/value pairs into a list where each element is a tuple
    # keys() returns all keys as a sequence
    # dict.pop(key, default_message) returns value related to key and removes the pair from the dict.

    name = input("Enter a name: ")
    if name in emails:
        del emails[name] #emails.pop(name)
    else:
        print("That name iis not found.")
    pass


def save_emails(emails):
    """Pickle the emails dictionary to FILENAME."""
    # TODO - Implement this function.
    with open(FILENAME, "wb") as output_file:
        pickle.dump(emails, output_file)

    pass


if __name__ == '__main__':
    main()
