import requests
from bs4 import BeautifulSoup

def scrape_books():
  url = 'https://books.toscrape.com/'
  response = requests.get(url)
  html = BeautifulSoup(response.text, 'html.parser')

  # print(html)

  books_html = html.find_all('article', class_='product_pod')

  books = []
  index = 0

  for book in books_html:
    article = {}
    article['index'] = index
    article['title'] = book.h3.a['title']
    article['price'] = book.find('p', class_='price_color').text[1:]
    if book.find('p', class_='instock availability').text.strip() == 'In stock':
      article['stock'] = True
    else:
      article['stock'] = False
    article['star-rating'] = book.find('p', class_='star-rating')['class'][1]

    books.append(article)

    index += 1

  return books
