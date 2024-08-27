import requests
from pprint import pprint
API_key = "6b21af090f4d0836dd5bb720fa6f9c11"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_id = input("Enter city id : ")
Final_url = base_url + "appid=" + API_key + "&id=" + city_id
weather_data = requests.get(Final_url).json()
pprint(weather_data)