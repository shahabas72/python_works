import requests
from pprint import pprint
API_key = "6b21af090f4d0836dd5bb720fa6f9c11"
base_url="http://api.openweathermap.org/data/2.5/weather?"
city_name=input("Enter a city name:")
Final_url = base_url + "appid=" + API_key + "&q=" + city_name
weather_data=requests.get(Final_url).json()
print("\nCurrent Weather Data of"+city_name+":\n")
pprint(weather_data)
print("URL", Final_url)
