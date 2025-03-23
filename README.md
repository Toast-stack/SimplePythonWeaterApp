# Weather API CLI Tool

This is a simple command-line tool that retrieves and displays weather information for a given city using the OpenWeatherMap API.

## Features

- Fetches real-time weather data based on the city name.
- Displays:
  - Temperature (in Fahrenheit by default)
  - Weather description
  - Humidity percentage
  - Wind speed
- Error handling for invalid city names or API request failures.

## Requirements

- Python 3.x
- Requests library

### Install dependencies:

```bash
pip install requests
```

## Usage

1. Run the script:

   ```bash
   python WeatherAPICalls.py
   ```

2. Enter a city name when prompted.
3. The weather details will be displayed.
4. Type `exit` to close the application.

## Example Output

```
Welcome to the Weather App!
Enter a city name (or type 'exit' to quit): London

Weather in London:
Temperature: 50.3 F
Description: Clear sky
Humidity: 65%
Wind Speed: 3.5 m/s
```

## API Key

This script requires an API key from OpenWeatherMap. Replace the `API_KEY` variable in the script with your own key.

## License

This project is licensed under the MIT License.
