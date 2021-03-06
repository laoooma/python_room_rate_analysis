# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GraduationProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    lease_mode = scrapy.Field()
    apartment = scrapy.Field()
    area = scrapy.Field()
    orientation = scrapy.Field()
    floor = scrapy.Field()
    renovation = scrapy.Field()
    quarters = scrapy.Field()