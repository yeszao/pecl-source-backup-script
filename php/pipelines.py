# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline
from urllib.parse import urlparse
from os.path import join


class PeclPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        return join('pecl', urlparse(request.url).path)


class PhpPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        return join('php', urlparse(request.url).path)
