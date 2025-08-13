import requests

# Replace with your OpenWeatherMap API key
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    # Parameters for API request
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Change to "imperial" for Fahrenheit
    }

    try:
        # Send GET request
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # Check if the city is found
        if data.get("cod") != 200:
            print("Error:", data.get("message", "Unknown error"))
            return

        # Extract weather details
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        # Display results
        print(f"\nWeather in {city.capitalize()}:")
        print(f"Condition  : {weather.capitalize()}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity   : {humidity}%\n")

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    if API_KEY == "YOUR_API_KEY_HERE":
        print("Please replace YOUR_API_KEY_HERE with your actual OpenWeatherMap API key.")
    else:
        city_name = input("Enter city name or ZIP code: ").strip()
        if city_name:
            get_weather(city_name)
        else:
            print("You must enter a city name or ZIP code.")
