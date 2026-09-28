while True:
    print(f"""
    Welcome to Your Shopping List!

    Please make a selection from one of the following options:

    1. Add an item to the shopping list.
    2. Display the shopping list.
    3. Display the item count.
    4. Display the first item in the shopping list.
    5. Display the last item in the shopping list.
    6. Clear the shopping list.
    7. Exit the program.
    """)
    selection = input("Selection: ")

    grocery_list = []

    if(selection == "1"):
        item = input("Item to add: ")
        grocery_list.append(item)
        input("Hit [enter] to continue...")
        continue

    elif(selection == "2"):
        print(f"Grocery List: {grocery_list}")
        input("Hit [enter] to continue...")
        continue

    elif(selection == "3"):
        print(f"ITEM COUNT: {len(grocery_list)}")
        input("Hit [enter] to continue...")
        continue

    elif(selection == "4"):
        print(f"FIRST ITEM: {grocery_list[0]}")
        input("Hit [enter] to continue...")
        continue

    elif(selection == "5"):
        print(f"LAST ITEM: {grocery_list[-1]}")
        input("Hit [enter] to continue...")
        continue

    elif(selection == "6"):
        grocery_list = []
        print(f"Shopping list is now empty.")
        input("Hit [enter] to continue...")
        continue

    elif(selection == "7"):
        print("Goodbye!")
        exit()
        
    else:
        print(f"You entered an invalid option. \nPlease try again!")