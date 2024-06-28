# got it!
from bs4 import BeautifulSoup
import requests
import csv

# Create a dictionary to hold the data
table_data = {}

# Navigate to the site index and pull site_soup
book_url_full = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

# Go to the book page and get the html
book_soup = BeautifulSoup(requests.get(book_url_full).text, "html.parser")

# find the table of data on the book page
Information_Table = book_soup.find("table")

# Extract the data from the book page's table
n = 0
for label_itm in Information_Table.findAll("th"):
    value_item = Information_Table.select('td')[n].text
    table_data[label_itm.text] = value_item
    n += 1

# Extract the book title
book_title = book_soup.find("h1").text
table_data['book_title'] = book_title

# Extract the image URL
image_url = book_soup.find("img")["src"]
table_data['image_url'] = image_url

# Extract the product description (assumption: descriptions will be more _
# than 60 characters; other targets not usable because aren't as long)
for product_description in book_soup.find_all("p"):
    if len(product_description.text) > 60:
        product_description = product_description.text
        table_data['product_description'] = product_description

# Extract the Star Rating
for rating in book_soup.find_all("p", class_="star-rating"):
    ex_class = rating["class"]
    rating_str = ex_class[1]
    # print(rating_str)
    if rating_str == 'One':
        rating_int = int(rating_str.replace("One", '1'))
    elif rating_str == 'Two':
        rating_int = int(rating_str.replace("Two", '2'))
    elif rating_str == 'Three':
        rating_int = int(rating_str.replace("Three", '3'))
    elif rating_str == 'Four':
        rating_int = int(rating_str.replace("Four", '4'))
    elif rating_str == 'Five':
        rating_int = int(rating_str.replace("Five", '5'))
    else: rating_int = 'whoops'
table_data['rating'] = rating_int

# Extract the Category
for category in book_soup.find_all('ul', class_ = 'breadcrumb'):
    for li in category.find_all("a"):
        category2 = li.text
        table_data['category'] = category2

with open('SingleBook_results.csv', 'w', errors='replace', newline="") as csvFile:
    writer = csv.DictWriter(csvFile, delimiter=",", fieldnames=table_data.keys())
    writer.writeheader()
    writer.writerow(table_data)
      # this prints the same row on repeat with improved formatting...
      # In this version, I changed delimiter to a comma.
