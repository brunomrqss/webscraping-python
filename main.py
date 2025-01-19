import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import os


url="https://books.toscrape.com/catalogue/category/books/history_32/index.html"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
page=requests.get(url, headers=headers)

soup=BeautifulSoup(page.text, "html.parser")

fetch_title = soup.find_all("a")
titles=[title.get("title") for i, title in enumerate(fetch_title) if i >= 55 and i % 2 != 0]


fetch_price = soup.find_all("p", class_="price_color")
prices=[str(i.get_text()).split("Â£")[1] for i in fetch_price]
prices = [*map(float, prices)]

fetch_rating = soup.find_all("p", class_="star-rating")
rating_transformed=[*map(str, fetch_rating)]

reviews = []

for string in rating_transformed:
    if "One" in string:
        reviews.append(1)

    if "Two" in string:
        reviews.append(2)

    if "Three"in string:
        reviews.append(3)

    if "Four" in string:
        reviews.append(4)

    if "Five" in string:
        reviews.append(5)
    
books = []

for title, price, review in zip(titles, prices, reviews):
    dic={}
    dic["name"]=title
    dic["price"]=price
    dic["rating"]=review
    books.append(dic)

avg_prices = sum(prices)/len(prices)
print(f'The avg price is £{avg_prices:.2f}')
avg_reviews = sum(reviews)/len(reviews)
print(f'The avg of rating is {avg_reviews:.0f} stars')
qtt_books=len(titles)
print(f'This category has {qtt_books} books')

raw_path=os.makedirs("raw", exist_ok=True)

def write_to_csv():
    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["title", "prices", "rating"])
        
        for title, price, review in zip(titles, prices, reviews):
            writer.writerow([title, price, review])
    
if __name__ == "__main__":
    write_to_csv()