from command_handlers import AddressBook, function


def command_parser(addressbook: AddressBook, input_string) -> str:
    input_string = input_string.strip().lstrip()
    command = input_string.split()[0].lower()
    arguments = input_string.split()[1:]
    if command in function:
        message = function[command](addressbook, *arguments)
    elif input_string.lower() in ("good bye", "exit", "close", "bye", "."):
        message = "\nGood bye!\n"
    else:
        message = f"\nCommand {command} does not exist!\n"
    return message


def main() -> None:
    my_address_book = AddressBook()
    try:
        print('\nType "help" for list of commands.\n')

        my_address_book.load_records("storage1.dat")

        while True:
            input_string = input("Enter Command: ")

            if not len(input_string):
                continue
            message = command_parser(my_address_book, input_string)
            print(message)
            if message == "\nGood bye!\n":
                break
    except Exception as e:
        print(f"Unexpected error occurred. {e}")

    finally:
        my_address_book.save_records("storage1.dat")
        print("\nDon't worry. All saved")
        exit(0)


if __name__ == "__main__":
    main()
