# Pick any single product page (i.e., a single book) on Books to Scrape, and write a
# Python script that visits this page and extracts the following information:
# DONE ● product_page_url
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
import csv
# import pandas as pd

# Create a dictionary to hold the data
table_data = {}

# Navigate to the site index and pull site_soup
root_url = "https://books.toscrape.com/index.html"
response = requests.get(root_url)
# print(response.encoding)
site_soup = BeautifulSoup(response.text, "html.parser")

# Reset the root_url, so it's compatible with book_url
root_url = "https://books.toscrape.com/"

# Visit each of the pages and capture individual data
books = site_soup.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
for book in books:
    book_url = book.find('a')['href']
    book_url_full = root_url + book_url
    table_data['product_page_url'] = book_url_full

    # Go to the book page and scrape the data
    book_soup = BeautifulSoup(requests.get(book_url_full).text, "html.parser")

    # # find the table of data on the book page
    # Information_Table = book_soup.find("table")
    #
    # # Extract the data from the book page's table
    # n = 0
    # for label_itm in Information_Table.findAll("th"):
    #     value_item = Information_Table.select('td')[n].text
    #     table_data[label_itm.text] = value_item
    #     n += 1
    #
    # # Extract the book title
    # book_title = book_soup.find("h1").text
    # table_data['book_title'] = book_title
    #
    # # Extract the image URL
    # image_url = book_soup.find("img")["src"]
    # table_data['image_url'] = image_url
    #
    # # Extract the product description (assumption: descriptions will be more _
    # # than 60 characters; other targets not usable because aren't as long)
    # for product_description in book_soup.find_all("p"):
    #     if len(product_description.text) > 60:
    #         product_description = product_description.text
    #         table_data['product_description'] = product_description

    # Extract the Star Rating
    # for p in book_soup.find_all("p"):
    #     for item in p.find_all(class_=''star-rating"):
    #         if p['class'] == 'star':
    #             scrape_review_rating = item.select('p.star-rating ')
    #             table_data['review_rating'] = "scrape_review_rating"
    # Returns multiple errors: Gotta work on this one a bit. . .

    for rating in book_soup.find_all("p"):
        rating_2 = rating.__class__
        print(rating_2)
        # this currently prints class 'bs4.element.Tag' which doesn't seem right.

# print(table_data)  # [this prints out all the data I want. . . why doesn't it print to CSV?]
# print(table_data.keys())  # this prints out just the fields within the dictionary.

#    #Write it all to a CSV file
#     with open('results.csv', 'w', newline="") as f:
#         writer = csv.DictWriter(f, delimiter=",", fieldnames=table_data.keys())
#         writer.writeheader()
#         for data in table_data:
#             writer.writerow(data)
#             # this doesn't write at all. . . .

    # with open('results.csv', 'w', newline="") as f:
    #     writer = csv.DictWriter(f, delimiter=",", fieldnames=table_data.keys())
    #     writer.writeheader()
    #     for data in table_data:
    #         writer.writerow(table_data)
    #         # this writes just the headers and nothing else.

    # with open('results.csv', 'w', newline="") as f:
    #     writer = csv.DictWriter(f, delimiter=",", fieldnames=table_data.keys())
    #     writer.writeheader()
    #     for data in table_data:
    #         writer.writerow(data)
    #         # this doesn't work at all. . .error to follow
    #         # Expected type 'Mapping[str, Any]' (matched generic type 'Mapping[_T, Any]'), got 'str' instead

# with open('results.csv', 'w', errors='replace') as csvFile:
#     writer = csv.DictWriter(csvFile, delimiter=";", fieldnames=table_data.keys())
#     writer.writeheader()
#     for data in table_data:
#         writer.writerow(table_data)
#         # this just prints the same row on repeat with stupid formatting. . .
#         # in this version, I tried using DictWriter.

# with open('results.csv', 'w', errors='replace', newline="") as csvFile:
#     writer = csv.DictWriter(csvFile, delimiter=",", fieldnames=table_data.keys())
#     writer.writeheader()
#     for data in table_data:
#         writer.writerow(table_data)
#           # this prints the same row on repeat with improved formatting...
#           # In this version, I changed delimiter to a comma.

# with open('results.csv', 'w', errors='replace', newline="") as csvFile:
#     writer = csv.DictWriter(csvFile, delimiter=",", fieldnames=table_data.keys())
#     writer.writeheader()
#     for data in table_data:
#         writer.writerow(data)
#         # In this version, I changed writer.writerow(table_data) to writer.writerow(data)
#         # Result: Error at line 108 (the line I changed): Expected type
#         # 'Mapping[str, Any]' (matched generic type 'Mapping[_T, Any]'), got 'str' instead
