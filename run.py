from scrapy.cmdline import execute
import schedule
import time
import subprocess
from os.path import join, abspath, dirname


def pecl():
    execute(['scrapy', 'crawl', 'pecl'])
    push_pecl()


def php():
    execute(['scrapy', 'crawl', 'php'])


def push_pecl():
    dir = abspath(dirname(__file__))
    git_dir = join(dir, 'downloads/pecl/get/.git')
    subprocess.check_output(['git', '--git-dir=' + git_dir, 'add', '*'])
    subprocess.check_output(['git', '--git-dir=' + git_dir, 'commit', '-m', 'update'])
    subprocess.check_output(['git', '--git-dir=' + git_dir, 'push', 'gitee', 'master'])
    subprocess.check_output(['git', '--git-dir=' + git_dir, 'push', 'github', 'master'])


if __name__ == '__main__':
    #schedule.every().day.at("2:30").do(pecl)
    schedule.every(1).minutes.do(push_pecl)

    while True:
        schedule.run_pending()
        time.sleep(1)
