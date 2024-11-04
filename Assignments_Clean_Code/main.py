from user_interface import UserInterface
from menu import Menu
# Create classes that represent different aspects of the weather forecast application, such as fetching data, parsing data, and user interaction.
def main():
    ui = UserInterface()
    menu = Menu()
    while True:
        menu.display_menu()
        choice = menu.get_user_choice()
        if choice == '1':
            ui.run()
        elif choice == '2':
            print("Exiting the Weather Forecast Application. Goodbye!")
            break

if __name__ == "__main__":
    main()
