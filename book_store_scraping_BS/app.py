import aiohttp
import asyncio
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
loop = asyncio.get_event_loop()

async def get_session(session, url):
    async with session.get(url) as response:
        return await response.text()


async def session_creator(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url_link in urls:
            tasks.append(get_session(session, url_link))
        return await asyncio.gather(*tasks)


urls = [f'http://books.toscrape.com/catalogue/page-{x+1}.html' for x in range(1, page.page_number)]
page_loop = loop.run_until_complete(session_creator(loop, *urls))

for p_l in page_loop:
    page = Page(p_l)
    books.extend(page.book_list)
