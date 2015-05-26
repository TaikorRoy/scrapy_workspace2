# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem


class TutorialSpider(scrapy.Spider):
    name = "sephora"
    allowed_domains = ["sephora.cn"]
    start_urls = (
        'https://www.sephora.cn/login.html',
    )

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formname = 'Logon',
            formdata={'logonId': 'furaoing', 'logonPassword': 'ttstream0'},
            callback=self.after_login
        )

    def after_login(self, response):
        item = TutorialItem()
        #base_xpath = "/html/body/div[@id='main']/div[@class='spriteLine clearFix']/div[@id='contentRight']/div[@id='globalFilterFacetProductDIV']/div[@id='rightCategoryFilterResultDiv']/div[@class='productList productBox cagegoryList mt20 mMt10 clearFix']"
        item['id'] = response.body
        # item['id'] = response.xpath("/html/body/div[@id='topFix']/div[@class='topBox']/div[@class='topDetial']/div[@id='headerLoginDisplay']/div[@id='afterUserLogin']/div[@class='topMemMobile']/div[@class='topMemDetail floatL']/a[1]/b[@id='afterLoginID']").extract()
        return item
