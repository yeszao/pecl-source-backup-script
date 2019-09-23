from scrapy.cmdline import execute
import schedule
import time
import oss2
from config import *
from php.settings import FILES_STORE
import os
import logging
import sys


def pecl():
    execute(['scrapy', 'crawl', 'pecl'])


def php():
    execute(['scrapy', 'crawl', 'php'])


def upload():
    auth = oss2.Auth(OSS_ACCESS_KEY_ID, OSS_ACCESS_KEY_SECRET)
    bucket = oss2.Bucket(auth, OSS_URL, OSS_BUCKET_NAME)

    files_info = os.walk(FILES_STORE)

    for path, dirs, names in files_info:
        if names:
            for filename in names:
                if filename.startswith('.'):
                    continue

                local_path = os.path.join(path, filename).lstrip()
                remote_key = os.path.join(path[(path.find('/') + 1):], filename)

                logging.info("Uploading %s --> %s" % (local_path, remote_key))

                if bucket.object_exists(remote_key):
                    logging.info('File exist (@-@)')
                else:
                    bucket.put_object_from_file(remote_key, local_path)
                    logging.info('Upload success (^_^)')


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    #schedule.every().day.at("2:30").do(pecl)
    #schedule.every(1).minutes.do(upload)
    upload()

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
