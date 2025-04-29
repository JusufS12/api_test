import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.expedia.com/Flights')
https = BeautifulSoup(response.text, 'html.parser')

print(html)
