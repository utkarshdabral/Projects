import requests

API_KEY = 'your_openweathermap_api_key'  # Replace with your API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def display_weather(data):
    if data['cod'] == 200:
        city = data['name']
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        print(f'Weather in {city}:')
        print(f'Temperature: {temp}°C')
        print(f'Description: {weather.capitalize()}')
    else:
        print(f"Error: {data['message']}")

def main():
    city_name = input('Enter city name: ')
    weather_data = get_weather(city_name)
    display_weather(weather_data)

if __name__ == '__main__':
    main()
