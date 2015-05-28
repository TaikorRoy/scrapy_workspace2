# -*- coding: utf-8 -*-
__author__ = 'Taikor'

from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from tutorial.spiders.example import TutorialSpider
from scrapy.utils.project import get_project_settings


def crawl():
    spider = TutorialSpider(domain='search.jd.com')
    settings = get_project_settings()
    crawler = Crawler(settings)
    crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
    crawler.configure()
    crawler.crawl(spider)
    crawler.start()
    log.start()
    reactor.run() # the script will block here until the spider_closed signal was sent



