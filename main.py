import management

if __name__ == "__main__":
    while True:
        user_input = management.read_option()

        if user_input == '1':
            management.add_spartan()
        elif user_input == '2':
            management.remove_spartan()
        elif user_input == '3':
            management.list_spartans()
        elif user_input == '4':
            management.retrieve_spartan()
        elif user_input == '5':
            break
