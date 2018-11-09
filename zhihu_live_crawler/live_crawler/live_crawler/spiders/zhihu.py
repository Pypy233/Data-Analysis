# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from live_crawler.items import LiveCrawlerItem
import json


class ZhihuSpider(Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/']

    def start_requests(self):
        start_url = 'https://api.zhihu.com/lives/homefeed?limit=10&offset=10&includes=live'
        yield Request(url=start_url, callback=self.parse)

    def parse(self, response):
        item = LiveCrawlerItem()
        result = json.loads(response.text)
        records = result['data']
        print(records[0])
        # for record in records:
        #     item['title'] = record['live']['subject']
        #     item['speaker'] = record['live']['speaker']['member']['name']
        #     yield item

        # next_page_url = result['paging']['next'] + '&includes=live'
        # yield Request(url=next_page_url, callback=self.parse)
