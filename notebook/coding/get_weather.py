# filename: get_weather.py

import requests

def get_weather(city, api_key):
    try:
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
        weather = response.json()
        return weather
    except Exception as e:
        return str(e)

# Replace 'your_api_key' with your actual API key
print(get_weather('Wichita', 'your_api_key'))