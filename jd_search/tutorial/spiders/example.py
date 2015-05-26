# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem


class TutorialSpider(scrapy.Spider):
    name = "sephora"
    allowed_domains = [""]
    start_urls = (
        'http://search.jd.com/Search?keyword=面膜&enc=utf-8',
        'http://search.jd.com/Search?keyword=面霜&enc=utf-8'
    )

    def parse(self, response):
        base_xpath = "/html/body[@class='root61']/div[@class='w main']/div[@class='right-extra']/div[@id='plist']/ul[@class='list-h clearfix']"
        for sel in response.xpath(base_xpath + r"//div[@class='lh-wrap']"):
            item = TutorialItem()
            item['brand'] = sel.xpath("div[@class='p-price']/strong/@data-price").extract()
            item['title'] = response.url
            yield item