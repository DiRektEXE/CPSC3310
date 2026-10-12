from pathlib import Path


MIN_CELSIUS = 0
MAX_CELSIUS = 50

# find the file in the same folder that host the Python script
TEMPERATURE_FILE = Path(__file__).resolve().parent / "temperature_forloop.txt"

def main():
    celsius = get_celsius()

    #this section is to test both for-loop and while-loop for searching target in a file
    fahrenheit_forloop = find_match_forloop(celsius)
    fahrenheit_whileloop = find_match_whileloop(celsius)
    print(f"For-loop search result:   {fahrenheit_forloop}")
    print(f"While-loop search result: {fahrenheit_whileloop}")

    if fahrenheit_forloop is not None:
        print(f"Match found: {celsius} Celsius is {fahrenheit_forloop:.2f} Fahrenheit.")
    else:
        fahrenheit = (celsius * 1.8) + 32
        append_record(celsius, fahrenheit)
        print(f"No match found. New record added: {celsius} Celsius = {fahrenheit:.2f} Fahrenheit.")


def get_celsius():
    #TODO - enforce the user to enter a good celsius temperature between (0-50)
    # Initialize the temperature variable so that we can enter the WHILE loop
    celsius_value = -1
    
    while (celsius_value:= int(input("Enter a celsius value from 0-50: "))) < MIN_CELSIUS or celsius_value > MAX_CELSIUS:    
        print("Invalid celsius value. Please enter an integer value ranging 0-50.")        
    
        # I could remove the IF statement for simplicity
    if celsius_value >= MIN_CELSIUS and celsius_value <= MAX_CELSIUS:
        print("Captured celsius value input.")
    
    return celsius_value


def find_match_forloop(celsius):
    fahrenheit = None

    with open(TEMPERATURE_FILE, "r") as infile:
        skip_header(infile)
        for line in infile:
            #Advanced technique applied here: a 'tuple-unpacking' split one record to two variables. Positional.
            degree_text, fahrenheit_text = line.split("\t\t")
            if int(degree_text) == celsius:
                fahrenheit = float(fahrenheit_text)

    return fahrenheit


def find_match_whileloop(celsius):
    #TODO - construct a while-loop to complete what the above find_match_forloop() does.
    fahrenheit = None
    with open(TEMPERATURE_FILE, 'r') as infile:
        skip_header(infile)
        line = infile.readline()

        # Keep searching the file until we arrive at an empty string (end of file)
        while line != "":

            # Seperate the celsius and fahrenheit values with TAB characters near them
            # Use tuple unpacking to assign the first value to degree_text and the second value to fahrenheit_text
            degree_text, fahrenheit_text = line.split("\t\t")

            # Is the first value equal to the target?
            if int(degree_text) == celsius:

                # If so, store the corresponding fahrenheit value
                fahrenheit = float(fahrenheit_text)

            # If the target value wasn't found, read the next line
            line = infile.readline()

    return fahrenheit       



# this function is to remove the header and dashline. If you have different header format, ensure to remove them all
def skip_header(infile):
    infile.readline()  # skip the header line
    infile.readline()  # skip the dashed separator line

def append_record(celsius, fahrenheit):
    #TODO - append a new record to the existing file
    pass


if __name__ == "__main__":
    main()
