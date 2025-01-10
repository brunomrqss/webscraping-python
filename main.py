import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup



url='https://books.toscrape.com/catalogue/category/books/history_32/index.html'

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}

page=requests.get(url, headers=headers)

soup=BeautifulSoup(page.text, 'html.parser')
var = soup.find_all('a')[55].get('title')
print(var)