import requests
import pycountry


def get_country_code(country_name):
    try:
        country_code = pycountry.countries.get(name=country_name).alpha_2
        return country_code
    except AttributeError:
        return None


def get_weather_data(api_key, city_name, country_name):
    # Get the country code for the given country name
    country_code = get_country_code(country_name)

    if country_code:
        # OpenWeatherMap API endpoint with city and country
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}"

        # Send a GET request to the API
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            # Extract relevant weather data
            weather = data['weather'][0]['description']
            temperature = data['main']['temp'] - 273.15  # Convert temperature to Celsius
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            return {
                'City': city_name,
                'Country': country_name,
                'Weather': weather,
                'Temperature (Celsius)': temperature,
                'Humidity (%)': humidity,
                'Wind Speed (m/s)': wind_speed
            }

    return None


if __name__ == "__main__":
    api_key = ''  # Replace with your OpenWeatherMap API key
    city_name = input("Enter the city name: ")
    country_name = input("Enter the country name: ")

    weather_data = get_weather_data(api_key, city_name, country_name)

    if weather_data:
        print("\nWeather Information for", weather_data['City'], ",", weather_data['Country'])
        print("Weather:", weather_data['Weather'])
        print("Temperature:", weather_data['Temperature (Celsius)'], "°C")
        print("Humidity:", weather_data['Humidity (%)'], "%")
        print("Wind Speed:", weather_data['Wind Speed (m/s)'], "m/s")
    else:
        print("Failed to fetch weather data. Please check the city name, country name, and your API key.")
