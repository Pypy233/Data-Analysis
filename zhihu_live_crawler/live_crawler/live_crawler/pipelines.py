# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class LiveCrawlerPipeline(object):
    def open_spider(self, spider):
        self.con = sqlite3.connect('live.db')
        self.cur = self.con.cursor()

    def process_item(self, item, spider):
        title = item['title']
        tag = item['tag']
        author = item['author']
        score = item['score']
        comment = item['comment']
        participant = item['participant']
        price = item['price']
        gratitude = item['gratitude']
        collection = item['collection']
        praise = item['praise']
        followed = item['followed']

        sql_command = "INSERT INTO live " \
                      "(title, tag, author, score, comment, participant," \
                      " price, gratitude, collection, praise, followed) " \
                      "VALUES ('{title}', '{tag}', '{author}', '{score}'," \
                      " '{comment}', '{participant}', '{price}', '{gratitude}'," \
                      "'{collection}', '{praise}', '{followed}')".\
            format(title=title, tag=tag, author=author, score=score, comment=comment,
                   participant=participant, price=price, gratitude=gratitude, collection=collection,
                   praise=praise, followed=followed)
        self.cur.execute(sql_command)
        self.con.commit()
        return item


def close_spider(self, spider):  # 关闭数据库或者数据文件
    self.con.close()
