# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmozItem(scrapy.Item):
        hash = scrapy.Field()
        link = scrapy.Field()
        type = scrapy.Field()
        time = scrapy.Field()
        contents = scrapy.Field()
        count = scrapy.Field()
	path = scrapy.Field()
	visited = scrapy.Field()
    
