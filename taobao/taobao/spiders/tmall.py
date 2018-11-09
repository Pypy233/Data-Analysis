# -*- coding: utf-8 -*-
import scrapy


class TmallSpider(scrapy.Spider):
    name = 'tmall'
    allowed_domains = ['https://www.tmall.com/']
    start_urls = ['http://https://www.tmall.com//']

    def parse(self, response):
        pass
