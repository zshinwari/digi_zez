import logging
logger = logging.getLogger('scrap.site_page')


class AllBooksPage:
    BOOK_PAGE_LOCATOR = 'div section ol.row li.col-xs-6'
    logger.info(f"page site tag {BOOK_PAGE_LOCATOR}")
    PAGE_NUMBER_LOCATOR = 'div section div ul.pager li.current'
    logger.info(f"page number tag {PAGE_NUMBER_LOCATOR}")