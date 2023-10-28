def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def main():
    print("Welcome to the assistant bot! (Привіт)")

    contacts = {}

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                name, phone = args
                contacts[name] = phone
                print("Contact added.")
            else:
                print("Invalid command. Usage: add [name] [phone]")
        elif command == "change":
            if len(args) == 2:
                name, new_phone = args
                if name in contacts:
                    contacts[name] = new_phone
                    print("Contact updated.")
                else:
                    print("Contact not found.")
            else:
                print("Invalid command. Usage: change [name] [new_phone]")
        elif command == "phone":
            if len(args) == 1:
                name = args[0]
                if name in contacts:
                    print(contacts[name])
                else:
                    print("Contact not found.")
            else:
                print("Invalid command. Usage: phone [name]")
        elif command == "all":
            if len(contacts) > 0:
                for name, phone in contacts.items():
                    print(f"{name}: {phone}")
            else:
                print("No contacts saved.")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
