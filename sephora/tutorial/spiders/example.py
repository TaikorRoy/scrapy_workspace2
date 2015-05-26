# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem


class TutorialSpider(scrapy.Spider):
    name = "sephora"
    allowed_domains = ["sephora.cn"]
    start_urls = (
        'http://localhost/%E5%8C%96%E5%A6%86%E5%93%81%E7%94%B5%E5%95%86/%E9%9D%A2%E9%83%A8%E7%B2%BE%E5%8D%8E%E4%BA%A7%E5%93%81-%E9%9D%A2%E9%83%A8%E6%8A%A4%E7%90%86%E6%AD%A3%E5%93%81-%E4%B8%9D%E8%8A%99%E5%85%B0SEPHORA%E5%8C%96%E5%A6%86%E5%93%81.html',
    )

    def parse(self, response):
        base_xpath = "/html/body/div[@id='main']/div[@class='spriteLine clearFix']/div[@id='contentRight']/div[@id='globalFilterFacetProductDIV']/div[@id='rightCategoryFilterResultDiv']/div[@class='productList productBox cagegoryList mt20 mMt10 clearFix']"
        for sel in response.xpath(base_xpath + r'//div[@class="proBox"]'):
            item = TutorialItem()
            item['brand'] = sel.xpath('p[@class="proBrand"]/a/text()').extract()
            item['title'] = sel.xpath('div[@class="proTit"]/a/@title').extract()
            yield item
