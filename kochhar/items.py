# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KochharItem(scrapy.Item):
    # define the fields for your item here like:
    Title = scrapy.Field()
    Publication_Date = scrapy.Field()
    URL = scrapy.Field()
    pass
