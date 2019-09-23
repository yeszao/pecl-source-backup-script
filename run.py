from scrapy.cmdline import execute
import schedule
import time
import subprocess


def pecl():
    execute(['scrapy', 'crawl', 'pecl'])
    push_pecl()


def php():
    execute(['scrapy', 'crawl', 'php'])


def push_pecl():
    subprocess.check_output(['git', '--git-dir=downloads/pecl/get/.git', 'add', '*'])
    subprocess.check_output(['git', '--git-dir=downloads/pecl/get/.git', 'commit', '-m', 'update'])
    subprocess.check_output(['git', '--git-dir=downloads/pecl/get/.git', 'pull', 'origin', 'gitee'])
    subprocess.check_output(['git', '--git-dir=downloads/pecl/get/.git', 'pull', 'origin', 'github'])


if __name__ == '__main__':
    #schedule.every().day.at("2:30").do(pecl)
    schedule.every(1).minutes.do(push_pecl)

    while True:
        schedule.run_pending()
        time.sleep(1)
