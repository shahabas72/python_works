import requests

API_key = "6b21af090f4d0836dd5bb720fa6f9c11"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter a city name : ")
Final_url = base_url + "appid=" + API_key + "&q=" + city_name
weather_data = requests.get(Final_url).json()
temp = weather_data['main']['temp']
wind_speed = weather_data['wind']['speed']
description = weather_data['weather'][0]['description']
latitude = weather_data['coord']['lat']
longitude = weather_data['coord']['lon']

print("Temperature:", temp)
print("Wind Speed:", wind_speed)
print("Description", description)
print("Latitude", latitude)
print("Longitude", longitude)