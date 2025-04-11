# Weather Projects
This repository contains two Python projects focused on weather data: **Weather API CLI Tool** and **Weather Visualization Project**. These projects demonstrate how to fetch real-time weather data using the OpenWeatherMap API and Python for informative, dynamic applications.
---

## 1. Weather API CLI Tool
A simple command-line tool that retrieves and displays weather information for a given city using the OpenWeatherMap API.

### Features
  - Fetches **real-time weather data** based on the city name.
  - Displays:
    - Temperature (in Fahrenheit by default).
    - Weather description.
    - Humidity percentage.
    - Wind speed.
  - Includes **error handling** for invalid city names or API request failures

### Requirements
  - Python 3.x
  - Requests library
Install dependencies:
```bash
pip install requests
```

### Usage
```bash
python WeatherAPICalls.py
```
Instructions
1. Enter a city name when prompted.
2. View the weather details displayed for your input.
3. Type `exit` to close the application.

Example Output
```
Welcome to the Weather App!
Enter a city name (or type 'exit' to quit): london

Weather in London:
Temperature: 67.98 F
Description: Clear sky
Humidity: 36%
Wind Speed: 12.66 m/s
```

## 2. Weather Visualization Project
A dynamic Python tool that fetches weather data and creates visualization using libraries like Matplotlib. This project showcases weather statistics in an easy-to-understand graphical format.

### Features
  - Fetches **real-time weather data** for a given city using OpenWeatherMap API.
  - Visualizes:
    - Temperature.
    - Humidity percentage.
    - Wind speed.
  - Handles errors like invalid city names or API request failures.

### Requirements
  - Python 3.x
  - Requests library
  - Matplotlib

Install dependencies:
```bash
pip install requests matplotlib
```

### Usage
Run the script:
```bash
python VisualizationCalls.py
```
Instructions
1. Enter a city name when prompted.
2. View weather statistics in a graphical bar chart.
3. Type `exit` to close the application.

Example Output
When you enter a valid city name, a bar chart is generated, displaying:
  - Temperature (°F).
  - Humidity (%).
  - Wind speed (mph)

## API Key
Both projects require an API Key from OpenWeatherMap. Follow these steps:
1. Sign up at [OpenWeatherMap](https://openweathermap.org/) and generate your API Key.
2. Replace the `API_KEY` variable in both scripts with your key.

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute this software.
