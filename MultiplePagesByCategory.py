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
import time
import math
import csv
start_time = time.time()

# Give the user a message
print("The scrape has commenced!")
# Create a list to hold the dictionaries
book_dict_list = []
category_list = []

# Navigate to the site and pull site_soup
root_url = "https://books.toscrape.com/"
response = requests.get(root_url)
# print(response.encoding)
site_soup = BeautifulSoup(response.text, "html.parser")

# # Make a list of the categories (this is where we'll store the dictionaries for the books)
# categories = site_soup.find('ul', {'class': 'nav nav-list'}).find('li').find('ul').find_all('li')
# for category in categories:
#     cat_text = category.text
#     strip_cat_text = cat_text.replace('\n', "").replace(" ", "")
#     len_cat_text = len(strip_cat_text)
#     if len_cat_text > 3:
#         category_list.append(strip_cat_text)

cat1 = site_soup.find('ul', {'class': 'nav nav-list'}).find('li').find('ul').find_all('li')
for cat in cat1:
    cat2 = cat.find('a')['href']
    cat_url = root_url + cat2
    response = requests.get(cat_url)
    cat_soup = BeautifulSoup(response.text, "html.parser")

    # Determine the page number of current and the page number total
    page = cat_soup.find('li', class_="current")
    if page == None: # there's just one page of books.
        total_page = 1
        current_page = 1
    else: # there's multiple pages of books
        pager = page.text
        words = pager.split()
        if len(words) >= 4:
            current_page = int(words[1])
            total_page = int(words[3])

    # When current page = 1, don't add one to it.
    if current_page == 1:
        next_page = 1

    while current_page <= total_page:
        if current_page > 1:
            page_url = f'{cat_url}catalogue/page-{next_page}.html'
        else:
            page_url = cat_url

        response = requests.get(page_url)
        page_soup = BeautifulSoup(response.text, "html.parser")
        # Visit each of the book pages and capture individual data
        books = page_soup.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        for book in books:
            table_data = dict()
            book_url = book.find('a')['href']
            if "catalogue" in book_url:
                book_url_full = root_url + book_url
            else:
                book_url = book_url.replace("../../../", "")
                book_url_full = root_url + 'catalogue/' + book_url
            table_data['product_page_url'] = book_url_full

            # Go to the book page and scrape the data
            book_soup = BeautifulSoup(requests.get(book_url_full).text, "html.parser")

            # find the table of data on the book page
            Information_Table = book_soup.find("table")
            if Information_Table is None:
                print("Information table not found")
                exit()

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
            image_url = book_soup.find("img")["src"].replace("../../", "https://books.toscrape.com/")
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
                else:
                    rating_int = 'whoops'
            table_data['rating'] = rating_int

            # Extract the Category
            for category in book_soup.find_all('ul', class_='breadcrumb'):
                for li in category.find_all("a"):
                    category2 = li.text
                    table_data['category'] = category2

            # append the book dictionary to the list of dictionaries
            book_dict_list.append(table_data)

        # iterate to the next page of books
        end_time = time.time()
        elapsed_time = int(end_time) - int(start_time)
        books_scraped = len(book_dict_list)
        print(f' {books_scraped} book scrapes completed after: {elapsed_time} seconds')
        next_page = next_page + 1
        current_page = next_page

print('The requested scrape is now complete')
