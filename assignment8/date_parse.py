# Vajaran Nall

def main():
    """Main function to run the password validator."""
    try:
        date, result = validate(enter_date())
        if result:
            print(result)
        else:
            print(f"Date: {date}")
    except Exception as e:
        print(f"An error occurred: {e}")



def enter_date():

    while True:
        date = input("Enter a date in M/D/YY or MM/DD/YYY format: ")

        if not date.strip():
            print("Enter a date.")
        
        else:
            return date

def validate(date):

    month, day, year = date.split("/")

    month = int(month)
    day = int(day)
    

    if len(year) == 2:
        year = int(year)
        
       
        if year <= 68:
            year += 2000

        else:
            year += 1900

    else:
        year = int(year)

    formatted_date_out = f"{month}/{day}/{year}"
    return formatted_date_out, None

if __name__ == "__main__":
    main()
