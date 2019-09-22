# -*- coding: utf-8 -*-
import scrapy

from ..items import DownloadItem
from urllib.parse import urljoin, urlparse
import os


class PeclSpider(scrapy.Spider):
    name = 'pecl'
    allowed_domains = ['pecl.php.net']
    start_urls = ['https://pecl.php.net/package-stats.php']

    base_url = 'https://pecl.php.net/'

    def parse(self, response):
        package_urls = response.xpath('//td[@class="content"]/table[3]//td[1]/a/@href').getall()

        for url in package_urls:
            yield scrapy.Request(
                urljoin(self.base_url, url),
                callback=self.parse_detail,
            )

    def parse_detail(self, response):
        item = DownloadItem()

        item['name'] = response.xpath("//h2/text()").get().strip()

        urls = response.xpath('//td[@class="content"]/table[3]//tr/td[3]/a/@href').getall()
        item['file_urls'] = []
        for url in urls:
            url = url.strip()
            if url:
                file_ext = os.path.splitext(url)[-1]
                if file_ext in ('.tgz', '.gz', 'bz2', 'xz'):
                    scheme = urlparse(url).scheme
                    if scheme:
                        item['file_urls'] = url
                    else:
                        item['file_urls'].append(urljoin(self.base_url, url))

        return item
