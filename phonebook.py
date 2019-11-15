#////////////////////////////////////////////////
#               LARGE LEVEL
#////////////////////////////////////////////////

#1. Phone Book App
# You will write a command line program to manage a phone book. When you start the 
# phonebook.py program, it will print out a menu and ask the user to enter a choice:

# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry           
# 4. List all entries
# 5. Quit

# What do you want to do (1-5)?

# If they choose to look up an entry, you will ask them for the person's name, and then 
# look up the person's phone number by the given name and print it to the screen.
# If they choose to set an entry, you will prompt them for the person's name and the 
# person's phone number,
# If they choose to delete an entry, you will prompt them for the person's name and delete 
# the given person's entry.
# If they choose to list all entries, you will go through all entries in the dictionary 
# and print each out to the terminal.
# If they choose to quit, end the program.
# phonebook_app = ()

# def print_entries():
#     if len(phonebook_app) == 0:
#         print("You have no entries!!")
#     else:
#         for count, entries in enumerate(phonebook_app):
#             print(f"{count}; {entries}")

# def look_up_entry():
#     if len(phonebook_app) == 0:
#         print("Sorry, no one by that name is listed!")
#     else:
#         for count, entries in enumerate(phonebook_app):
#             print(f"{count}; {entries}")

# def add_name(new_entry_name):
#     phonebook_app.update(new_entry_name)
# def add_num(new_entry_num):
#     phonebook_app.update(new_entry_num)

# def delete_entry(index):
#     try:
#         phonebook_app.pop(index)
#     except IndexError:
#         print("Sorry, that name does not exist!")



# def main{}:
#     menu = """
# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit
# """       
#     is_running = True
#     while is_running:
#         print(menu)
#         choice = (input("What do you want to do?: "))
#         if choice == "1":
#             look_up_entry = (input("Name?: "))
#             look_up_entry()
#         elif choice == "2":
#             new_entry_name = input("Name?: ")
#             new_entry_num = input("Phone Number?: ")
#             add_name(new_entry_name)
#             add_num(new_entry_num)
#         elif choice == "3":
#             entry_to_delete = int(input("Name?"))
#             delete_entry(entry_to_delete)
#         elif choice == "4":
#             print_entries()
#         elif choice == "5":
#             is_running = False
#             print("Bye!")
#         else:
#             print("Please enter a number of your choice.")
# main()

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