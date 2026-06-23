import contacts

instantation = contacts.Contacts("my.json")

def main_menu(title, options):
    print(f"\n{('*** ' + title).center(60)}\n")
    for i, option in enumerate(options, 1):
        print(f"{i}, {option}")
    return input("Enter your Choice: ")

menu_options = ["Add contact", "Modify contact", "Delete contact"
                , "Print contact list", "Send message", "Set contact filename"
                , "Exit the program" ]

def main():
    while True:
        global instantation

        choice = main_menu("TUFFY TITAN CONTACT MAIN MENU", menu_options)
        if choice == '1':
            phone = input("Enter phone number")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name ")

            contact_information = instantation.add_contact(phone, first_name, last_name)

            if contact_information == "error":
                 print("Error: phone number already exists. ")
            else:
                print(f"Added: {first_name} {last_name}. ")
        elif choice == "2":
            phone = input("Enter phone number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            contact_modify = instantation.modify_contact(phone, first_name, last_name)

            if contact_modify == "error":
                print("Error: phone number not found")
            else:
                print(f"Contact Modified: {first_name} {last_name}. ")
        elif choice == "3":
            phone = input("Enter phone number: ")

            del_phone = instantation.delete_contact(phone)

            if del_phone == "error":
                print("Error: phone number not found. ")
            else:
                first_name, last_name = del_phone[phone]
                print(f"Deleted Contact: {first_name} {last_name}. ")
        elif choice == "4":
            print("\n     ====================== CONTACT LIST ======================")
            print(f"{'Last Name':<22}{'First Name':<22}{'Phone'}")
            print(f"{'='*22} {'='*22} {'='*10}")

            if not instantation.dict:
                print("     No contacts found.")
            else:
                for phone, (first_name, last_name) in sorted(
                    instantation.dict.items(),
                    key=lambda item: (item[1][1].lower(), item[1][0].lower())
                ):
                    print(f"{last_name:<22}{first_name:<22}{phone}")
        elif choice == "5":
            phone = input("\nEnter phone number to send message to: ")
            message = input("Enter message: ")

            result = instantation.send_message(phone, message)

            if result == "error":
                print("Error: phone number not found. ")
            else:
                print(result)
        elif choice == "6":
            new_filename = input("\nEnter new contact filename: ")
            try:
                instantation = contacts.Contacts(new_filename)
                print(f"Contact filename set to: {new_filename}")
            except FileNotFoundError as exc:
                print(f"Error: {exc}")
            
        elif choice == "7":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvaid choice. Please try again. ")
    

if __name__ == "__main__":
    main()
