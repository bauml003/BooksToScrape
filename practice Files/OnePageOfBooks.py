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
# DONE ● review_rating
# DONE ● image_url
# DONE ● category
# Write the data to a CSV file using the above fields as column headings.

from bs4 import BeautifulSoup
import requests
import csv

# Create a list to hold the dictionaries
book_dict_list = []
book_number = 1



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
    table_data = dict()
    book_url = book.find('a')['href']
    book_url_full = root_url + book_url
    table_data['product_page_url'] = book_url_full

    # Go to the book page and scrape the data
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

    # append the book dictionary to the list of dictionaries
    book_dict_list.append(table_data)

# print(table_data)  # [this prints out all the data I want. . . why doesn't it print to CSV?]
# print(table_data.keys())  # this prints out just the fields within the dictionary.
# print(book_dict_list)
# print(book_dict_list.__len__())

with open('OnePage_results.csv', 'w', errors='replace', newline="") as csvFile:
    writer = csv.DictWriter(csvFile, delimiter=",", fieldnames=table_data.keys())
    writer.writeheader()
    for data in book_dict_list:
        writer.writerow(data)
