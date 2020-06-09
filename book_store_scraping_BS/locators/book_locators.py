import logging

logger = logging.getLogger('scraping.book_tags')


class BooksLocators:
    logger.info('book tags')
    STAR_RATING_LOCATOR = 'li.col-xs-6 article.product_pod p.star-rating'
    logger.info(f"rating locator {STAR_RATING_LOCATOR}")
    PRICE_LOCATOR = 'li.col-xs-6 article.product_pod div.product_price p.price_color'
    logger.info(f"price locator {PRICE_LOCATOR}")
    TITLE_LOCATOR = 'li.col-xs-6 article.product_pod h3 a'
    logger.info(f"title locator {TITLE_LOCATOR}")
    LINK_LOCATOR = 'li.col-xs-6 article.product_pod h3 a'
    logger.info(f"link locator {LINK_LOCATOR}")