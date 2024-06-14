# Pick any single product page (i.e., a single book) on Books to Scrape, and write a
# Python script that visits this page and extracts the following information:
# ● product_page_url
# DONE ● universal_ product_code (upc)
# DONE ● book_title
# DONE ● price_including_tax
# DONE ● price_excluding_tax
# DONE ● quantity_available
# DONE ● product_description
# DONE ● category
#  ● review_rating
# DONE ● image_url
# Write the data to a CSV file using the above fields as column headings.

from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
table_data = {}

book_title = soup.find("h1").text

##find the table
Information_Table = soup.find("table")

n=0
for label_itm in Information_Table.findAll("th"):
    value_item = Information_Table.select('td')[n].text
    table_data[label_itm.text] = value_item
    n+=1

book_title = soup.find("h1").text
table_data['book_title'] = book_title

image_url = soup.find("img")["src"]
table_data['image_url'] = image_url

for product_description in soup.find_all("p"):
    if len(product_description.text) > 60:
        product_description = product_description.text
        table_data['product_description'] = product_description

path_info = "TBD"
table_data['product_page_url'] = path_info

review_rating = "TBD"
table_data['review_rating'] = review_rating

print(table_data)








