# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AncientPoetryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PoemsItem(scrapy.Item):
    title = scrapy.Field()  # 标题
    author = scrapy.Field()  # 作者
    dynasty = scrapy.Field()  # 作者所属朝代
    content = scrapy.Field()  # 诗歌正文
