# -*- coding: utf-8 -*-

# Scrapy settings for doubanmoive project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'doubanmoive'

SPIDER_MODULES = ['doubanmoive.spiders']
NEWSPIDER_MODULE = 'doubanmoive.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'doubanmoive (+http://www.yourdomain.com)'
ITEM_PIPELINES = {
    'doubanmoive.pipelines.DoubanmoivePipeline':300
}