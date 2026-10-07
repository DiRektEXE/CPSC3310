# Celsius Conversion Program

def celsius_conversion():

# Constant
    ABSOLUTE_ZERO = -273

# Input and validation
    while True:

        # Attempt to grab the celsius value from the user
        try:             
            max_celsius = int(input("Enter a celsius degree: "))

            if ABSOLUTE_ZERO<= max_celsius < 0:
                            print("The celsius degree you entered was negative.")

            # The temperature you entered was lower than absolute zero
            if max_celsius < ABSOLUTE_ZERO:
                print("Error: Celsius degree cannot be below absolute zero (-273).")

            # You provided a celsius temperature greater than absolute zero. 
            # Your value will be used by the FOR loop.
            else:
                break

        # Handle invalid input
        except ValueError:
            print("Error: Please enter an integer number.")

    # Output headings
    print("Celsius\t\tFahrenheit")
    print("----------------------------")

    # Convert Celsius to Fahrenheit
    for celsius in range(0, max_celsius + 1):

        fahrenheit = (celsius * (9 / 5)) + 32        
        print(f"{celsius:<16}{fahrenheit:.1f}")

if __name__ == "__main__":
    celsius_conversion()