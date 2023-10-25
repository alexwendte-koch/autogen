# filename: get_ip.py

import requests

def get_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip = response.json()['ip']
        return ip
    except Exception as e:
        return str(e)

print(get_ip())