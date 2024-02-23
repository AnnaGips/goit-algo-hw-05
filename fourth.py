def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Контакт не знайдено."
        except ValueError:
            return "Невірний ввід."
        except IndexError:
            return "Неповна команда або аргумент."
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split(maxsplit=1)
    cmd = cmd.strip().lower()
    args = args[0].split() if args else []
    return cmd, args

@input_error
def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        return "Enter the argument for the command"

@input_error
def show_phone(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Contact not found."
    else:
        return "Enter the argument for the command"

@input_error
def list_all_contacts(args, contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found"

def main():
    contacts = {}
    print("Enter a command: ")

    while True:
        user_input = input()
        command, args = parse_input(user_input)

        if command == "add":
            print(add_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(list_all_contacts(args, contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
