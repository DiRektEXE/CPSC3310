# Vajaran Nall
import random


# Create a dictionary object to hold 10 US states as keys and their capitals they map to as values
capitals_map = {"Illinois":"Springfield", 
            "Arizona":"Phoenix", 
            "Colorado":"Denver", 
            "Georgia":"Atlanta", 
            "Ohio":"Columbus", 
            "Oregon":"Salem",
            "Texas":"Austin",
            "Virginia":"Richmond",
            "Wisconsin":"Madison",
            "Utah":"Salt Lake City"}

states = list(capitals_map.keys())

correct_answers = 0
incorrect_answers = 0
while True:
    random_state = random.choice(states)
    answer = input(f"What is the capital of {random_state} (Or enter 0 to exit)? ")

    # Check this condition first
    if answer == "0":
        break

    elif answer == capitals_map[random_state]:
        correct_answers += 1
        print("That is correct!")

    else:
        incorrect_answers += 1
        print("That is incorrect.")

print(f"You had {correct_answers} correct responses and {incorrect_answers} incorrect responses.")
print("Exiting the program...")



