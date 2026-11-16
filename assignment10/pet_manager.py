
from .pet import Pet

# Get user input
name = input("Enter the name of the pet: ")
animal_type = input("Enter the type of animal: ")
age = int(input("Enter the age of the pet: "))

# Create a Pet object
my_pet = Pet(name, animal_type, age)

# Display pet information
print("Here is the data that you entered:")
my_pet.print_info()

