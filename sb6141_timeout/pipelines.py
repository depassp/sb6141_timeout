# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem
from peewee import *

db = SqliteDatabase('timeouts.sqlite')

class Item(Model):
    date = DateTimeField()
    message = CharField()

    class Meta:
        database = db

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class TimeoutPipeline(object):
    def process_item(self, item, spider):
        if (u'T4 time out' in item['message'] or
            u'T3 time-out' in item['message']):
                return item
        else:
                raise DropItem("Not a T3 nor T4 time out")

#class DuplicatesPipeline(object):
#    def __init__(self):
#        self.ids_seen = set()
#
#    def process_item(self, item, spider):
#        if item['date'] in self.ids_seen:
#            raise DropItem("Duplicate item found: %s" % item)
#        else:
#            self.ids_seen.add(item['date'])
#            return item

class PeeweePipeline(object):
    def open_spider(self, spider):
        self.db = db
        self.db.connect()
        self.db.create_tables([Item], safe=True)

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        try:
            i = Item.get(Item.date == item['date'])
        except Item.DoesNotExist:
            i = None
        if i:
            raise DropItem("This item is already in the DB")
        else:
            i = Item(date=item['date'], message=item['message'])
            i.save()
            return item

