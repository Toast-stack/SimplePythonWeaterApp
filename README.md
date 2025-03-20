# Real-Time Weather Application

A Python-based command-line app for retrieving real-time weather data for any city using the OpenWeatherMap API.

---

## Features

- Retrieves current weather details: temperature, humidity, wind speed, and conditions.
- Handles invalid city names and API issues gracefully.
- Scalable design for future enhancements (e.g., multi-day forecasts, GUI).

---

## Requirements

- **Python 3.7+**
- **Dependencies**:  
  Install the required libraries using:
  ```bash
  pip install requests

## How to Run

1. Clone the repository and navigate to the project folder:
   ```bash
   git clone <repository_url>
   cd WeatherApp

## Replace the API Key

Open the `weather_app.py` file and replace the `API_KEY` with your OpenWeatherMap API key:

```python
API_KEY = "your_actual_api_key"
