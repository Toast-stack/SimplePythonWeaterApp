import requests
import matplotlib.pyplot as plt

# Function to get weather data from OpenWeatherMap API
def get_weather(city, api_key):
    try:
        # Build the API URL
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
        
        # Make the API request
        response = requests.get(url, timeout=10)  # Set a timeout for the request
        
        # Check for HTTP errors
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Extract relevant data
        return {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again later.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error: Unable to fetch data. {req_err}")
    except KeyError:
        print("Error: Unexpected response format from the API.")
    return None

# Main program
def main():
    # Your OpenWeatherMap API key (replace with your actual key)
    API_KEY = "1076cc2d0068fdc869a9aebca0830ae7"

    print("Welcome to the Weather Visualization Program!")
    city = input("Enter the name of the city you want to check: ")

    # Fetch weather data
    weather_data = get_weather(city, API_KEY)
    
    if weather_data:
        print(f"\nWeather for {weather_data['city']}:")
        print(f"Temperature: {weather_data['temperature']}\u00b0F")
        print(f"Description: {weather_data['description'].capitalize()}")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind_speed']} mph")
        
        # Visualize the data
        attributes = ['Temperature (\u00b0F)', 'Humidity (%)', 'Wind Speed (mph)']
        values = [weather_data['temperature'], weather_data['humidity'], weather_data['wind_speed']]
        
        plt.bar(attributes, values, color=['skyblue', 'lightgreen', 'orange'])
        plt.title(f"Weather Stats for {weather_data['city']}")
        plt.ylabel("Values")
        plt.show()
    else:
        print("Sorry, unable to fetch weather data. Please check the city name or your API key.")

# Run the program
if __name__ == "__main__":
    main()