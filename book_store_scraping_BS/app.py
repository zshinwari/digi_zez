import logging
import requests
from pages.all_books_page import Page

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.WARNING,
                    filename='logs.txt')

logger = logging.getLogger('scraping')
request = requests.get('http://books.toscrape.com/catalogue/page-1.html').content
page = Page(request)
books = page.book_list


for p in range(1, page.page_number):
    url = requests.get(f'http://books.toscrape.com/catalogue/page-{p+1}.html').content
    url_page = Page(url)
    books.extend(url_page.book_list)
