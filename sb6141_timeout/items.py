# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SB6141TimeoutItem(scrapy.Item):
    # name = scrapy.Field()
    date = scrapy.Field()
    message = scrapy.Field()
