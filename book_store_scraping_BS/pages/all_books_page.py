import re
import logging
from bs4 import BeautifulSoup
from locators.all_books_page import AllBooksPage
from parsers.book import Parsers

logger = logging.getLogger('scarp.book_page')


class Page:
    def __init__(self, page):
        logger.debug('creating soup object')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def book_list(self):
        logger.debug('creating a list of books')
        logger.info('creating a list of books that return book title, link, star and price')
        page_locator = self.soup.select(AllBooksPage.BOOK_PAGE_LOCATOR)
        logger.info('return book title, price and star rating')
        return [Parsers(e) for e in page_locator]

    @property
    def page_number(self):
        logger.debug('Number of pages in the website')
        page_number = self.soup.select_one(AllBooksPage.PAGE_NUMBER_LOCATOR).string
        pattern = 'Page [0-9]+ of ([0-9]+)'
        number_range = re.search(pattern, page_number)[1]
        logger.info('return the number of pages in the website, in this case 50 page but this may change in future')
        return int(number_range)
