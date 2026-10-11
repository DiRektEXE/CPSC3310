from pathlib import Path

MIN_CELSIUS = 0
MAX_CELSIUS = 50

# Anchor the output files to this script's own folder instead of using bare
# relative filenames, which depends on the working folder where the script gets executed.
SCRIPT_DIR = Path(__file__).resolve().parent
FORLOOP_FILE = SCRIPT_DIR / "temperature_forloop.txt"
WHILELOOP_FILE = SCRIPT_DIR / "temperature_whileloop.txt"


def main():
    celsius = get_celsius()
    write_temperature_file_forloop(celsius)
    write_temperature_file_whileloop(celsius)


def get_celsius():
    #TODO - get the user's input celsius value (0-50) and validate it until a good value received
    
    # Initialize the temperature variable so that we can enter the WHILE loop
    temperature = -1

    while temperature < MIN_CELSIUS or temperature > MAX_CELSIUS:
        temperature = int(input("Enter a celsius value from 0-50: "))

    if temperature >= MIN_CELSIUS and temperature <= MAX_CELSIUS:
        print("Captured celsius value input.")

    return temperature
    #pass

def write_temperature_file_forloop(celsius):
    #TODO - complete this function to reproduce what below write_temperature_file_whileloop does
    # but using a for-loop
    

    for i in range(0,celsius):
        print()

    pass


def write_temperature_file_whileloop(celsius):
    with open(WHILELOOP_FILE, "w") as outfile:
        outfile.write(f'{"Celsius":>8}\t\t{"Fahrenheit":>8}\n')
        outfile.write("------------------------------------\n")
        degree = 0
        while degree <= celsius:
            # Calculate C to F
            fahrenheit = (degree * 1.8) + 32
            outfile.write(f"{degree:>8}\t\t{fahrenheit:>8.2f}\n")
            degree += 1


if __name__ == "__main__":
    main()
