from scrapy.cmdline import execute
import schedule
import time
from php.settings import FILES_STORE
import os
import logging
import sys
from upload import upload


def pecl():
    execute(['scrapy', 'crawl', 'pecl'])


def php():
    execute(['scrapy', 'crawl', 'php'])


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    #schedule.every().day.at("2:30").do(pecl)
    #schedule.every(1).minutes.do(upload)
    upload(FILES_STORE)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
