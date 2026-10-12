from pathlib import Path

MIN_CELSIUS = 0
MAX_CELSIUS = 50

TEMPERATURE_FILE = Path(__file__).resolve().parent / "temperature_forloop.txt"


def main():
    celsius = get_celsius()

    fahrenheit_forloop = find_match_forloop(celsius)
    print(f"For-loop search result:   {fahrenheit_forloop}")

    if fahrenheit_forloop is not None:
        print(f"Match found: {celsius} Celsius is {fahrenheit_forloop:.2f} Fahrenheit.")
    else:
        fahrenheit = (celsius * 1.8) + 32
        append_record(celsius, fahrenheit)
        print(f"No match found. New record added: {celsius} Celsius = {fahrenheit:.2f} Fahrenheit.")


def get_celsius():
    # walrus operator cannot be used with try/except statement, 
    # otherwise the user just get one chance to try
    good_value_received = False
    while not good_value_received:
        celsius_text = input(f"Enter a celsius degree ({MIN_CELSIUS}-{MAX_CELSIUS}): ")

        # Attempt to cast to an integer        
        try:
            celsius = int(celsius_text)

            # Is this value within range?
            if (celsius < MIN_CELSIUS or celsius > MAX_CELSIUS):
                print(f"Value out of range. Please enter a value {MIN_CELSIUS}-{MAX_CELSIUS}.")
            else:
                good_value_received = True

        except ValueError:
            print("Can't convert to integer.")       
        

    return celsius


def find_match_forloop(celsius):
    # TODO - add try/except statement to catch FileNotFoundError
    pass


def skip_header(infile):
    infile.readline()  # skip the header line
    infile.readline()  # skip the dashed separator line

# OSError is required for 'appending' mode in case 
# the file is not granted with writing permission
def append_record(celsius, fahrenheit):
    try:
        with open(TEMPERATURE_FILE, "a") as outfile:
            outfile.write(f"{celsius:>8}\t\t{fahrenheit:>8.2f}\n")
    except OSError as error: 
        print(f"Could not write to the data file: {error}")


if __name__ == "__main__":
    main()
