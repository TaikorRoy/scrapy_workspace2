# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem


class TutorialSpider(scrapy.Spider):
    name = "jumei"
    allowed_domains = [""]
    start_urls = ('http://search.jumei.com/?filter=0-11-'+str(i+1)+'&search=&cat=3&cat=38,383,55,143&bid=2_m' for i in range(31))

    def parse(self, response):
        base_xpath = "/html/body[@class='J_body_301']/div[@id='container']/div[@id='body']/div[@id='search_result_wrap']/div[@id='search_list_wrap']/div[@class='products_wrap']"
        for sel in response.xpath(base_xpath + r"//div[@class='s_l_name']/a"):
            item = TutorialItem()
            item['title'] = sel.xpath('text()').extract()
            yield item
