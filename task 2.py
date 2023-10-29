from cmd_utils import CMD


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

        if hasattr(CMD, command) and callable(getattr(CMD, command)):
            if getattr(CMD, command)(args, contacts):
                break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
