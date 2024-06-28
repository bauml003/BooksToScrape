Introduction
-
This program allows the user to obtain all data from a specific website (www.books.toscrape.com). The extracted information is as follows: 
The data is extracted, transformed, and loaded to .CSV files named after the book category. 
The extracted data is as follows:
- product_page_url
- UPC (universal product code)
- Product Type
- Price (excl. tax)
- Price (incl. tax)
- Tax
- Availability
- Number of reviews
- book_title
- product_description
- rating
- category

The script also downloads the cover art for each of the scraped entities. 
Each image file is named with the category to which it belongs as well as the name of the entity. 
An example would be "Travel - ItsOnlytheHimalayas.jpg"

Instructions
-
To run this program, the user must have Python installed on their machine. 
1. From the console (terminal) the user should clone this repository using: 
git clone https://github.com/bauml003/BooksToScrape.git

2. Within the cloned folder, create a virtual environment:
python -m venv env

3. Activate the virtual environment in terminal:
env\scripts\activate

4. Install the required packages
pip install -r requirements.txt

5. Run the script
python main.py

6. Review the outputs of the program from the folder titled 'results' 
7. Consult the folder titled cover_images for copies of the downloaded images 
