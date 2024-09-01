import requests
from bs4 import BeautifulSoup
import mysql.connector
from datetime import datetime
import re

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="giraffe"
)
cursor = conn.cursor()

url = "http://books.toscrape.com/"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

books = soup.find_all("article", class_="product_pod")
for book in books:
    title = book.h3.a["title"]

    price_text = book.find("p", class_="price_color").text.strip()
    scrape_date = datetime.now()
x
    insert_query = """
    INSERT INTO books (title, price, scrape_date)
    VALUES (%s, %s, %s)
    """
    cursor.execute(insert_query, (title, price, scrape_date))

conn.commit()
cursor.close()
conn.close()

print("Scraped data stored in MySQL.")
