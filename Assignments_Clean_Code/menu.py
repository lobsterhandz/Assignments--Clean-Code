class Menu:
    def display_menu(self):
        print("\nWeather Forecast Application Menu:")
        print("1. Get Weather Forecast")
        print("2. Exit")

    def get_user_choice(self):
        while True:
            choice = input("\nEnter your choice: ").strip()
            if choice not in ['1', '2']:
                print("Invalid choice. Please enter 1 or 2.")
            else:
                return choice
