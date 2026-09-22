grocery_list = []

while(True):
    print("Welcome to Your Shopping List! ")
    print()
    print("Please make a selection from one of the following options: ")
    print()

    menu = """1. Add an item to the shopping list.
2. Display the shopping list.
3. Display the item count.
4. Display the first item in the shopping list.
5. Display the last item in the shopping list.
6. Clear the shopping list."""

    print(menu)
    print()
    selection = input("Selection: ")

    if selection == "1":
        item = input("Item to add: ")
        grocery_list.append(item)
        continue
    elif selection == "2":
        print(grocery_list)
        continue
    elif selection == "3":
        print(f"ITEM COUNT: {len(grocery_list)}")
        continue
    elif selection == "4":
        if grocery_list:
            print(f"FIRST ITEM: {grocery_list[0]}")
        else:
            print("Shopping list is empty.")
        continue
    elif selection == "5":
        if grocery_list:
            print(f"LAST ITEM: {grocery_list[-1]}")
        else:
            print("Shopping list is empty.")
        continue
    elif selection == "6":
        grocery_list = []
        continue
    else:
        print("You entered an invalid option.")
        print("Goodbye!")
        break
