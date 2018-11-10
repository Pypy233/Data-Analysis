# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item


class TaobaoItem(Item):
    GOODS_URL = scrapy.Field()
    GOODS_PRICE = scrapy.Field()
    GOODS_NAME = scrapy.Field()
    SHOP_NAME = scrapy.Field()
    SHOP_URL = scrapy.Field()

