import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup


url='https://books.toscrape.com/catalogue/category/books/history_32/index.html'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
page=requests.get(url, headers=headers)

soup=BeautifulSoup(page.text, 'html.parser')

fetch_title = soup.find_all('a')
titles=[title.get('title') for i, title in enumerate(fetch_title) if i >= 55 and i % 2 != 0]


fetch_price = soup.find_all('p', class_='price_color')
prices=[str(i.get_text()).split('Â£')[1] for i in fetch_price]

prices = [*map(float, prices)]

books = []

rating = soup.find_all('p', class_='star-rating')
rating_transformed=[*map(str, rating)]

reviews = []

for string in rating_transformed:
    if 'One' in string:
        reviews.append(1)

    if 'Two' in string:
        reviews.append(2)

    if 'Three' in string:
        reviews.append(3)

    if 'Four' in string:
        reviews.append(4)

    if 'Five' in string:
        reviews.append(5)
    
for title, price, review in zip(titles, prices, reviews):
    dic={}
    dic['name']=title
    dic['price']=price
    dic['rating']=review
    books.append(dic)

print(books[2])



