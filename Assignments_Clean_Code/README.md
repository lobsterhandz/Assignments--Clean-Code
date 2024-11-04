# Weather Forecast Application

## Overview
The Weather Forecast Application is a Python-based console program that provides weather information for selected cities. This project follows a modular and object-oriented design, separating functionality into different components, making it easy to understand, maintain, and extend.

## Features
- Fetch weather data for predefined cities (New York, London, Tokyo).
- Display detailed or brief weather reports.
- Modular design for easy code management.
- Unit tests to ensure the functionality of the components.

## Modules
1. **weather_data_fetcher.py**: Contains the `WeatherDataFetcher` class responsible for fetching weather data.
2. **data_parser.py**: Contains the `DataParser` class for parsing the fetched weather data into a readable format.
3. **user_interface.py**: Contains the `UserInterface` class for interacting with the user and providing weather reports.
4. **menu.py**: Contains the `Menu` class that displays the main application menu and gets user choices.
5. **main.py**: Main entry point to run the application.
6. **test_weather_app.py**: Unit tests for testing the core components of the application.

## Getting Started
### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone the repository or download the source code.
2. Navigate to the project directory.

### Running the Application
To run the Weather Forecast Application, execute the following command in your terminal:
```bash
python main.py
```

### Running the Tests
To run the unit tests for the application, execute:
```bash
python test_weather_app.py
```

## Usage
1. Run the application.
2. Choose an option from the menu.
   - Enter the city name to get the weather forecast.
   - You can choose between a detailed or brief weather report.
   - Exit the application by selecting the appropriate menu option.

## Available Cities
The application supports the following cities:
- New York
- London
- Tokyo

## Extending the Application
- To add more cities, update the `weather_data` dictionary in the `WeatherDataFetcher` class.
- Integrate with real-world weather APIs to enhance functionality.

## Error Handling
- Handles invalid city names by notifying users.
- Ensures input validation for user prompts.

## License
This project is open source and available under the MIT License.

## Acknowledgements
- Python for providing an intuitive programming language.
- The open-source community for inspiration in modular application design.
