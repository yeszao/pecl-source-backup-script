# -*- coding: utf-8 -*-
import scrapy

from ..items import DownloadItem
from urllib.parse import urljoin, urlparse
import os


class PhpSpider(scrapy.Spider):
    name = 'php'
    allowed_domains = ['www.php.net', 'museum.php.net']
    start_urls = ['https://www.php.net/releases/']

    base_url = 'https://www.php.net/'

    custom_settings = {
        'ITEM_PIPELINES': {'php.pipelines.PhpPipeline': 1}
    }

    def parse(self, response):
        item = DownloadItem()
        urls = response.xpath('//section[@id="layout-content"]//ul/li/a[contains(text(), "PHP") or contains(text(), "Source")]/@href').getall()
        item['file_urls'] = []
        for url in urls:
            url = url.strip()
            if url:
                file_ext = os.path.splitext(url)[-1]
                if file_ext in ('.tgz', '.gz', 'bz2', 'xz'):
                    scheme = urlparse(url).scheme
                    if scheme:
                        item['file_urls'].append(url)
                    else:
                        item['file_urls'].append(urljoin(self.base_url, url))

        return item
