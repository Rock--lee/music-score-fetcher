# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MusicScoreItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()    #乐谱标题
    #url = scrapy.Field()      #乐谱地址
    author = scrapy.Field()  #乐曲作者
    src = scrapy.Field()      #乐谱的图片连接
    alt = scrapy.Field()      #图片名称
    #summary = scrapy.Field()  #文章摘要
    pass
