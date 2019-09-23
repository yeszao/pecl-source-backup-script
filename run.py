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
    pecl()
