# filename: get_location.py

import requests

def get_location(ip):
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        location = response.json()['city']
        return location
    except Exception as e:
        return str(e)

print(get_location('146.209.159.4'))