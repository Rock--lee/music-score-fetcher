# -*- coding: utf-8 -*-
import scrapy
import json

from my_crawler.items import MusicScoreItem

class WebSpider(scrapy.spiders.Spider):
    name = "WebSpider"

    allowed_domains = ['ccguitar.cn']
    start_urls = [
        "http://so.ccguitar.cn/tosearch.aspx?searchname=%B5%C8%C4%E3%CF%C2%BF%CE&searchtype=1&submit=%BC%EC%CB%F7"
    ]



    def parse(self, response):
        articles = response.xpath('//*[@id="headline_block"]/ul/li')
        for article in articles:
            item = MusicScoreItem()
            item['title'] = article.xpath('a/text()').extract()[0]
            item['url'] = article.xpath('a[1]/@href').extract()[0]
            #item['summary'] = article.xpath('p[@class="post_item_summary"]/text()').extract()[0]
            yield item



class testSpider(scrapy.spiders.Spider):
    name = "testSpider"

    allowed_domains = ['ccguitar.cn']
    start_urls = [
        "http://www.ccguitar.cn/pu_list.htm"
    ]

    #主站连接 用来拼接url
    base_site = "http://www.ccguitar.cn/"
    current_page = 1

    def parse(self, response):
        musicScore_urls = response.xpath('//li[@class="puname"]/a/@href').extract()

        for musicScore_url in musicScore_urls:
            url = self.base_site + musicScore_url
            yield scrapy.Request(url, callback=self.getDetails)

        #获取下一页
        if self.current_page < 2:
            self.current_page = self.current_page + 1
            next_page_url = self.base_site + response.xpath('//div[@class="pg"]//a[contains(text(),"下一页")]/@href').extract()[0]
            yield scrapy.Request(next_page_url, callback=self.parse)

    def getDetails(self, response):
        item = MusicScoreItem()

        #提取信息
        item['title'] = response.xpath('//*[@id="navigation"]/p/text()[4]').extract()[0]
        item['author'] = response.xpath('//*[@id="navigation"]/p/a/text()').extract()[2]
        item['src'] = response.xpath('//*[@class="swiper-wrapper"]//img/@src').extract()
        item['alt'] = response.xpath('//*[@class="swiper-wrapper"]//img/@alt').extract()

        yield item


