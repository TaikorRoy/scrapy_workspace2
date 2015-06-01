# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem


class TutorialSpider(scrapy.Spider):
    name = "jumei"
    allowed_domains = [""]
    start_urls = ('http://search.jumei.com/?filter=0-11-'+str(i)+'&search=&cat=3&cat=38,383,55,143&bid=2_m' for i in range(27))
    #start_urls = ('http://search.jumei.com/?filter=0-11-1&search=%E9%9D%A2%E8%86%9C&bid=4&site=sh',)
    def parse(self, response):
        base_xpath = "/html/body[@class='J_body_301']/div[@id='container']/div[@id='body']/div[@id='search_result_wrap']/div[@id='search_list_wrap']/div[@class='products_wrap']"
        for sel in response.xpath(base_xpath + r"//div[@class='s_l_name']"):
            item = TutorialItem()
            item['title'] = sel.xpath(r"a").extract()[0]
            yield item

