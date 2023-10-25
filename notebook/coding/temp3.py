import geocoder
import requests

# Get current location
g = geocoder.ip("me")
city = g.city
country = g.country

print(f"Current location: {city}, {country}")

# Get weather information
response = requests.get(f"http://wttr.in/{city}?format=%C+%t")

# Print weather information
print(f"Weather: {response.text}")
