#Vajaran Nall


def temp_conversion(temperature=None):

    # Absolute zero constant
    ABSOLUTE_ZERO = -273

    while True:

        try:
            # Introduction message
            print("|\tTEMPERATURE CONVERSION PROGRAM\t|\n\n")

            # Grab temperature value from the user
            if temperature == None:

                temperature = float(input("Enter a temperature value: "))
                degree_type = str(input("Is this temperature supposed to be in Fahrenheit or Celsius?\n"))

                # Convert the temperature value to Fahrenheit or Celsius
                if degree_type.lower() == 'f' and temperature > ABSOLUTE_ZERO:
                    print("Converting to Celsius...\n")
                    print(f"{temperature} degrees in fahrenheit is {(temperature-32.0) * (5.0/9.0):.2f} degrees in Celsius.")

                if degree_type.lower() == 'c' and temperature > ABSOLUTE_ZERO:
                    print("Amazing\n")

            

            print("Celsius\tFahrenheit")
            print("-------------------------------------------------")
            

        except ValueError:
            print("Invlaid Input")

if __name__ == "__main__":
    temp_conversion()