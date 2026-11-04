# Vajaran Nall

# Ask user to enter a temperature value in Fahrenheit
temp_f = float(input("Please enter a degree in fahrenheit: "))

# Convert the temperature to celsius
temp_c = (temp_f - 32) * (5 / 9)

# Output a formated string as the result
print(f"{temp_f} degrees fahrenheit is {temp_c} degrees celsius.")