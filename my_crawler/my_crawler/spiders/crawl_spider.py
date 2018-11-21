# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from my_crawler.items import MyCrawlerItem

class WebSpider(scrapy.spiders.Spider):
    name = "WebSpider"
    allowed_domains = ['cnblogs.com']
    start_urls = [
        "https://www.cnblogs.com"
    ]



    def parse(self, response):
        articles = response.xpath('//*[@id="headline_block"]/ul/li')
        for article in articles:
            item = MyCrawlerItem()
            item['title'] = article.xpath('a/text()').extract()[0]
            item['url'] = article.xpath('a[1]/@href').extract()[0]
            #item['summary'] = article.xpath('p[@class="post_item_summary"]/text()').extract()[0]
            yield item

