from bs4 import BeautifulSoup
import requests

url = 'https://news.ycombinator.com/'

response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

news = []
i = 0

elements = html.find_all('span', class_='titleline')

for element in elements:
  new1 = {}
  new1['title'] = element.a.text
  new1['link'] = element.a['href']
  news.append(new1)

print(news)