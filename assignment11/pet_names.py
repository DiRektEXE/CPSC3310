from animal import Animal
from dog import Dog
from cat import Cat
from bird import Bird

def main():

    print("Pet Menu")
    print("1. Add Dog")
    print("2. Add Cat")
    print("3. Add Bird")
    print("4. Show all Pets")
    print("5. Exit")

    choice = input("Enter choice: ")
    animals = []

    if choice == "1":
        name = input("Enter the dog's name: ")
        animal = Dog(name)
        animals.append(animal)
    elif choice == "2":
        name = input("Enter the cat's name: ")
        animal = Cat(name)
        animals.append(animal)
    elif choice == "3":
        name = input("Enter the bird's name: ")
        animal = Bird(name)
        animals.append(animal)
    elif choice == "4":
        print("Showing all pets...\n\n")

        print("Your Pets:")
        for animal in animals:
            print(f"{animal.name} the {animal.__class__.__name__} says {animal.speak()}")

    elif choice == "5":
        print("Exiting...")
        return
    else:
        print("Invalid choice.")
        return 

    if __name__ == "__main__":
        main()
