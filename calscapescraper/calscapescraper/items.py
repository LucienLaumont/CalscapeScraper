# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field

class CalscapescraperItem(scrapy.Item):
    name = Field()
    adress = Field()
    phone = Field()
    mail = Field()
    website_url = Field()
    inventory = Field()