print("Welcome to Temperature Converter!")
print("Menu:")
print("1. Convert Fahrenheit to Celsius")
print("2. Convert Celsius to Fahrenheit")
selection = input("Enter selection (1 or 2): ")

if (selection == "1"):
    temp_f = input("Enter a temperature in Fahrenheit: ")
    temp_c = (float(temp_f) - 32) * (5/9)
    print(f"{temp_f} Fahrenheit is {temp_c} Celsius.")
elif (selection == "2"):
    pass

else:
    print("You failed to enter a valid selection")
    print("Invalid selection. Please enter 1 or 2.")
    print("Goodbye")

