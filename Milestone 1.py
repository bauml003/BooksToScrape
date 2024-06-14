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

table_data = {}
root_url = "https://books.toscrape.com/index.html"
response = requests.get(root_url)
site_soup = BeautifulSoup(response.text, "html.parser")

root_url = "https://books.toscrape.com/"

books = site_soup.find_all('li', class_ = "col-xs-6 col-sm-4 col-md-3 col-lg-3")
for book in books:
    book_url = book.find('a')['href']
    book_url_full = root_url + book_url
    table_data['product_page_url'] = book_url_full
    #go to the book page and scrape the data
    book_soup=BeautifulSoup(requests.get(book_url_full).text, "html.parser")

    ##find the table
    Information_Table = book_soup.find("table")

    n=0
    for label_itm in Information_Table.findAll("th"):
        value_item = Information_Table.select('td')[n].text
        table_data[label_itm.text] = value_item
        n+=1

    book_title = book_soup.find("h1").text
    table_data['book_title'] = book_title

    image_url = book_soup.find("img")["src"]
    table_data['image_url'] = image_url

    for product_description in book_soup.find_all("p"):
        if len(product_description.text) > 60:
            product_description = product_description.text
            table_data['product_description'] = product_description

    # for p in book_soup.find_all("p"):
    #     for item in p.find_all(class_=''star-rating")
    #         if p['class'] == 'star':
    #             review_rating = soup.select('p.star-rating ')
    #             table_data['review_rating'] = review_rating

    print(table_data)
#
#
#
#
#
#
#
#
