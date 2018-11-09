# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
# 标题 标签 作者 评分 评论 参与人数 价格 作者获得感谢 作者获得收藏 作者获得赞同 作者被关注
from scrapy import Field, Item


class LiveCrawlerItem(Item):
    title = Field()
    tag = Field()
    author = Field()
    score = Field()
    comment = Field()
    participant = Field()
    price = Field()
    gratitude = Field()
    collection = Field()
    praise = Field()
    followed = Field()

