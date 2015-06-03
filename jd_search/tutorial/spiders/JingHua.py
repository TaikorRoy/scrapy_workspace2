# -*- coding: utf-8 -*-
import os
import scrapy
from tutorial.items import TutorialItem
from scrapy.selector import Selector
from tutorial.spiders.load_product_obj import load_product_obj

local_path = os.getcwd()
base_path = local_path.rstrip(r"jd_search/tutorial/spiders")
products = load_product_obj(base_path+r'/data/catalog/JingHua.json')

kw_list = list()
for product in products:
    kw_list.append(product["title"][0])


class JingHuaSpider(scrapy.Spider):
    name = "JingHua"
    allowed_domains = ["http://search.jd.com"]
    start_urls = ('http://search.jd.com/Search?keyword='+kw+'&enc=utf-8' for kw in kw_list)

    def parse(self, response):
        for sel in response.xpath("//ul[@class='list-h clearfix']/li/div[@class='lh-wrap']"):
            item = TutorialItem()
            item['sku'] = 'None'  # placeholder
            item['brand'] = 'None'   # placeholder
            item['title'] = sel.xpath("div[@class='p-name']/a/font[1]/text()").extract()
            item['type'] = 'None'
            item['price'] = sel.xpath("div[@class='p-price']/strong/text()").extract()
            yield item
