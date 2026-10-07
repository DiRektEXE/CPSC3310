#Vajaran Nall

def temp_conversion():

    # Absolute zero constant
    ABSOLUTE_ZERO_C = -273.15
    ABSOLUTE_ZERO_F = -459.67
    

    try:
            # Introduction message
            print("|\tTEMPERATURE CONVERSION PROGRAM\t\t|\n")

            temperature = float(input("Enter a temperature value: "))
            degree_type = str(input("Enter the type of temperature (F for Fahrenheit, C for Celsius): "))

            # Convert the temperature value to Fahrenheit or Celsius
            if degree_type.lower() == 'f' and temperature > ABSOLUTE_ZERO_F:
                print("Converting to Celsius...\n")
                print(f"The temperature in Celsius is: {(temperature-32.0) * (5.0/9.0):.2f}")

            elif degree_type.lower() == 'c' and temperature > ABSOLUTE_ZERO_C:
                print("Converting to Fahrenheit...\n")
                print(f"The temperature in Fahrenheit is: {(temperature * (9.0/5.0)) + (32.0):.2f}")

            else:
                print("Invalid temperature type or value.")            

    except ValueError:
        print("Invlaid Input. Enter a temperature value.")

if __name__ == "__main__":
    temp_conversion()