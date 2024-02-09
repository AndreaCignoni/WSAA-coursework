# This program prints out the current temperature and the current wind direction (10m) separately.
# The information is retrieved through an API.
# Author: Andrea Cignoni

import requests
import json

# This variable stores the response received from the url
url ="https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_speed_10m"

# New coordinates my current location
new_latitude = 51.89
new_longitude = -8.4

# Update the URL with the new coordinates
url = f"https://api.open-meteo.com/v1/forecast?latitude={new_latitude}&longitude={new_longitude}&current=temperature_2m,wind_speed_10m"

response = requests.get(url)

# Check if the response content type is JSON
content_type = response.headers.get('Content-Type', '')
# print(content_type)
# Parse the JSON response into a Python dictionary
weather_data = json.loads(response.text)

current_temperature = weather_data['current']['temperature_2m']
# Printing the current temperature only
print (f"{current_temperature}°C")

# Adding the wind direction variable.
new_url = f"https://api.open-meteo.com/v1/forecast?latitude=51.894469818054255&longitude=-8.467380631463682&current=wind_direction_10m&hourly=temperature_2m"

response_1 = requests.get(new_url)

# Parse the JSON response into a Python dictionary
weather_data1 = json.loads(response_1.text)

current_wind_direction = weather_data1['current']['wind_direction_10m']

# Printing the current temperature only
print (f"{current_wind_direction}°")