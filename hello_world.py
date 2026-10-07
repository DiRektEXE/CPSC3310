#Vajaran Nall

def temp_conversion(fahrenheit=None):

    if fahrenheit == None:
        fahrenheit = float(input("Please enter a temperature degree in fahrenheit: "))

    print(f"{fahrenheit} degrees in fahrenheit is {(fahrenheit-32.0) * (5.0/9.0):.2f} degrees in Celsius.")

if __name__ == "__main__":
    temp_conversion()