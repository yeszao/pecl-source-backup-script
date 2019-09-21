# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline
from scrapy.http.request import Request
from scrapy.exceptions import DropItem
import os


class DownloadPipeline(FilesPipeline):
    # 生成下载请求
    def get_media_requests(self, item, info):
        for image_url in item['file_urls']:
            # 配合 get_media_requests 传递 meta，不然拿不到item
            # referer 处理防盗链
            yield Request(image_url, meta={'item': item}, headers={'referer': item['referer']})

    def file_path(self, request, response=None, info=None):
        package_name = request.meta['item']['name']
        package_version_name = request.url.split('/')[-1]

        return os.path.join(package_name, package_version_name)

    def item_completed(self, results, item, info):
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item contains no files")
        item['file_paths'] = file_paths
        return item



