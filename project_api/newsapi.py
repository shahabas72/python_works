import requests
from pprint import pprint

API_key = "5014f558d54b4d7dbb92982bf6ca89f5"
base_url = "https://newsapi.org/v2/everything?"
Title = input("Enter the title you want to search: ")
Final_url = base_url+"q="+Title+"&apiKey="+API_key
news_data = requests.get(Final_url).json()
pprint(news_data)