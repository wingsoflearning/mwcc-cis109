#temperatures = [99, "hello", 50]

#temperatures.append(40) # add item to end of list
#last_index = len(temperatures) - 1 # find last index of list

#print(temperatures[last_index]) # print last item in list
#print(temperatures[-1]) # print last item in list
#print(temperatures) # print entire list
#temperatures[1] = "goodbye" # change item to something else
#print(len(temperatures)) how many items in list
#print(temperatures[0]) Print only 1 item list starts at 0
#print(temperatures[1])

# for item in temperatures:
#     print(type(item))

temperatures = []

while(True):
    print("Select an option from the following menu:")
    menu = """
    1. Add a temperature
    2. List temperatures
    3. Calculate average temperature
    4. Exit
    """
    print(menu)
    selection = input("Enter a selection: ")
    if (selection == "1"):
        temperature = float(input("Enter a temperature: "))
        print(type(temperature))
        if (type(temperature) != type(1.0)):
            print("Please enter a numerical number")
            input("Hit [enter] to continue...")
            continue
        temperatures.append(float(temperature))
        #total += temperature # 
    elif (selection == "2"):
        print(temperatures)
        input("Hit [enter] to continue...")
    elif (selection == "3"):
        if len(temperatures) == 0:
            print("No temperatures to average")
            input("Hit [enter] to continue...")
            continue
        total = 0
        for temperature in temperatures:
            total += temperature
        average = total / len(temperatures)
        print(f"Average Temp: {average}")
        input("Hit [enter] to continue...")
    elif (selection == "4"):
        print("Goodbye!")
        exit() # or break