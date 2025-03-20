import requests

def get_weather(city):
    API_KEY = "1076cc2d0068fdc869a9aebca0830ae7"  # Replace with your actual API key
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    # Parameters for the API request
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        print("\n[DEBUG] Sending request to OpenWeatherMap API...")
        response = requests.get(BASE_URL, params=params)
        print(f"[DEBUG] Response status code: {response.status_code}")
        
        # Check if the response was successful
        if response.status_code == 200:
            print("[DEBUG] Response received successfully.")
            print("[DEBUG] Raw response content:", response.content)  # Display raw byte data
            print("[DEBUG] Decoded response text:", response.text)  # Display decoded text

            # Parse JSON response
            data = response.json()
            print("[DEBUG] Parsed JSON data:", data)

            # Extract weather information
            weather = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }

            # Display weather details
            print(f"\nWeather in {weather['city']}:")
            print(f"Temperature: {weather['temperature']} C")
            print(f"Description: {weather['description'].capitalize()}")
            print(f"Humidity: {weather['humidity']}%")
            print(f"Wind Speed: {weather['wind_speed']} m/s\n")
        else:
            print(f"[ERROR] Failed to fetch weather data. HTTP Status Code: {response.status_code}")
            print("[DEBUG] Response text:", response.text)

    except requests.exceptions.RequestException as e:
        print("\n[ERROR] RequestException occurred:", e)
    except UnicodeDecodeError as e:
        print("\n[ERROR] UnicodeDecodeError occurred:", e)
    except KeyError as e:
        print("\n[ERROR] KeyError occurred. Possibly an issue with the city name or API response structure.", e)


if __name__ == "__main__":
    print("Welcome to the Weather App!")
    while True:
        city = input("Enter a city name (or type 'exit' to quit): ")
        if city.lower() == 'exit':
            print("Goodbye!")
            break
        get_weather(city)
