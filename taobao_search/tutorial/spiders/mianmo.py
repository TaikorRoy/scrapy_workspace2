# -*- coding: utf-8 -*-
import os
import scrapy
from tutorial.items import TutorialItem
from scrapy.selector import Selector
from tutorial.spiders.load_product_obj import load_product_obj

local_path = os.getcwd()
base_path = local_path.rstrip(r"taobao_search/tutorial/spiders")
products = load_product_obj(base_path+r'/data/catalog/MianMo.json')

kw_list = list()
for product in products:
    kw_list.append(product["title"][0])



class TutorialSpider(scrapy.Spider):
    name = "taobao"
    allowed_domains = [""]
    start_urls = ('http://s.taobao.com/search?q='+kw+'&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=1.7274553.1997520841.1&initiative_id=tbindexz_20150602' for kw in kw_list)

    def parse(self, response):
        for sel in response.xpath("//ul[@class='list-h clearfix']/li/div[@class='lh-wrap']"):
            item = TutorialItem()
            item['sku'] = 'None'  # placeholder
            item['brand'] = 'None'   # placeholder
            item['title'] = sel.xpath("div[@class='p-name']/a/font[1]/text()").extract()
            item['type'] = 'None'
            item['price'] = sel.xpath("div[@class='p-price']/strong/text()").extract()
            yield item
