#Vajaran Nall

# Global Constants

# These values are fixed physical constants derived from 
# thermodynamic principles and the behavior of gases at 
# extremely low temperatures.
ABSOLUTE_ZERO_C = -273.15
ABSOLUTE_ZERO_F = -459.67
def main():
    
    temperature_type = get_temperature_type()
    temperature = get_temperature(temperature_type)
    display_conversion(temperature_type, temperature)

# Celsius or Fahrenheit?
def get_temperature_type():

    temperature_type = input("Enter temperature type (C or F): ").upper()

    while temperature_type != "C" and temperature_type != "F":
        print("Invalid input. Please enter C (Celsius) or F (Fahrenheit).")
        temperature_type = input("Enter temperature type (C or F): ").upper()

    return temperature_type


def get_temperature(temperature_type):

    # Ask user for input until they enter a valid temperature value
    if temperature_type == "C":

        temperature = float(input("Enter a temperature above absolute zero in Celsius: "))    
        while( temperature := float(input("Enter a temperature above absolute zero in Celsius: "))) < ABSOLUTE_ZERO_C:
            print("Invalid celsius temperature value. Please enter a value above absolute zero.")
            #temperature = float(input("Enter a temperature above absolute zero in Celsius: "))
        
    elif temperature_type == "F":
        
        temperature = float(input("Enter a temperature above absolute zero in Fahrenheit: "))            
        while ( temperature := float(input("Enter a temperature above absolute zero in Fahrenheit: "))) < ABSOLUTE_ZERO_F:
            print("Invalid temperature value. Please a value abvoe absolute zero.")

    return temperature       


def display_conversion(temperature_type, temperature):

    # User friendly output view
    if temperature_type == "C" and temperature > ABSOLUTE_ZERO_C:
        print("Converting from Celsius to Fahrenheit...")
        print(f"The temperature in Fahrenheit is: {(temperature * (9.0/5.0)) + (32.0):.2f}")

    if temperature_type == "F" and temperature > ABSOLUTE_ZERO_F:
        print("Converting from Fahrenheit to Celsius...")
        print(f"The temperature in Fahrenheit is: {(temperature - 32.0) * (5.0/9.0):.2f}")       


if __name__ == "__main__":
    main()