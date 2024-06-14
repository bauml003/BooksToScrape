# Pick any single product page (i.e., a single book) on Books to Scrape, and write a
# Python script that visits this page and extracts the following information:
# ● product_page_url
# ● universal_ product_code (upc)
# ● book_title
# ● price_including_tax
# ● price_excluding_tax
# ● quantity_available
# ● product_description
# ● category
# ● review_rating
# ● image_url
# Write the data to a CSV file using the above fields as column headings.

from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

book_title = soup.find("h1").text

##find the table
Information_Table = soup.find("table")
print(Information_Table)



