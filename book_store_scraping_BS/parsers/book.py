import re
import logging
from locators.book_locators import BooksLocators

logger = logging.getLogger('scraping.books_parser')


class Parsers:

    convert_to_number = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

    def __init__(self, return_value):
        self.return_value = return_value

    def __repr__(self):
        logger.debug('repr method')
        logger.info('returns book title, books price and rating stars')
        return f"<{self.title}, Price: {self.price} ({self.star_rating} {'stars' if self.star_rating > 1 else 'star'})>"

    @property
    def star_rating(self):
        logger.debug('creating star rating')
        star_rating = BooksLocators.STAR_RATING_LOCATOR
        select_star = self.return_value.select_one(star_rating).attrs.get('class')[1]
        logger.info('return stars rating')
        return Parsers.convert_to_number[select_star]

    @property
    def price(self):
        logger.debug('creating book price object')
        price_locator = BooksLocators.PRICE_LOCATOR
        select_price_locator = self.return_value.select_one(price_locator).string
        pattern = '£([0-9]+\.[0-9]+)'
        return_price = re.search(pattern, select_price_locator)[1]
        logger.info('return book price as float')
        return float(return_price)

    @property
    def title(self):
        logger.debug('creating title')
        title = BooksLocators.TITLE_LOCATOR
        title_locator = self.return_value.select_one(title).attrs.get('title')
        logger.info('return title')
        return title_locator

    @property
    def link(self):
        logger.debug('creating link locator')
        link = BooksLocators.LINK_LOCATOR
        link_locator = self.return_value.select_one(link).attrs.get('href')
        logger.info('return link locator')
        return link_locator

