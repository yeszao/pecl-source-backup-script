# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline
from urllib.parse import urlparse
from os.path import join
from scrapy.http.request import Request
import re


class PathPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        for url in item['file_urls']:
            yield Request(url, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        return urlparse(request.url).path.lstrip('/')


class PeclPipeline(PathPipeline):
    def file_path(self, request, response=None, info=None):
        pecl_name = request.meta['item']['name']
        pecl_version_name = request.url.split('/')[-1]

        return join('pecl', pecl_name, pecl_version_name)


class PhpPipeline(PathPipeline):
    def file_path(self, request, response=None, info=None):
        php_version_name = request.url.split('/')[-1]
        second_version = re.findall('php-(\d+\.\d+)', php_version_name)[0]

        return join('php', second_version, php_version_name)
