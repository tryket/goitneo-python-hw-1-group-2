class CMD:
    @staticmethod
    def close(*args):
        print("Good bye!")
        return True

    @staticmethod
    def hello(*args):
        print("How can I help you?")

    @staticmethod
    def add(args, contacts):
        if len(args) == 2:
            name, phone = args
            contacts[name] = phone
            print("Contact added.")
        else:
            print("Invalid command. Usage: add [name] [phone]")

    @staticmethod
    def change(args, contacts):
        if len(args) == 2:
            name, new_phone = args
            if name in contacts:
                contacts[name] = new_phone
                print("Contact updated.")
            else:
                print("Contact not found.")
        else:
            print("Invalid command. Usage: change [name] [new_phone]")

    @staticmethod
    def phone(args, contacts):
        if len(args) == 1:
            name = args[0]
            if name in contacts:
                print(contacts[name])
            else:
                print("Contact not found.")
        else:
            print("Invalid command. Usage: phone [name]")

    @staticmethod
    def all(args, contacts):
        if len(contacts) > 0:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts saved.")


CMD.exit = CMD.close
CMD.q = CMD.close
