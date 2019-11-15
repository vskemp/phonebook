def print_menu():
    print("ELECTRONIC PHONE BOOK")
    print("*********************")
    print('1. Look up an entry')
    print('2. Add an entry')
    print('3. Delete an entry')
    print('4. List all entries')
    print('5. Quit')
    print()

numbers = {}
menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = int(input("What do you want to do? (1-5): "))
    if menu_choice == 4:
        print("Your entries:")
        for x in numbers.keys():
            print("Name: ", x, "\tPhone Number:", numbers[x])
        print()
    elif menu_choice == 2:
        print("Add Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        print("Entry added for", (name))
        numbers[name] = phone
    elif menu_choice == 3:
        name = input("Name: ")
        if name in numbers:
            del numbers[name]
            print("Deleted entry", (name))
        else:
            print(name, "was not found")
    elif menu_choice == 1:
        print("Lookup Number")
        name = input("Name: ")
        if name in numbers:
            print("The number is", numbers[name])
        else:
            print(name, "was not found")
    elif menu_choice != 5:
        print("Bye!")
        print_menu()
