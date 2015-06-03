# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
import os

relative_path = "C:\workspace\WebCrawler\scrapy_workspace2\data\catalog"  # For portability, use relative path is a must, her for the proceed of a test use absolute path instead
job_list = os.listdir(relative_path)  # a job is the crawling task for all items listed on the XXX(job).json file


class TutorialPipeline(object):
    jobs = job_list

    def __init__(self):
        self.file = {job: codecs.open(job, 'wb', encoding='utf-8') for job in TutorialPipeline.jobs}
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def process_item(self, item, spider):
        line = json.dumps(dict(item))
        line = line.replace('\\r', '')
        line = line.replace('\\n', '')
        line = line.replace('\\t', '')
        line = line.replace(' ', '')
        line = line.replace('}', '},')
        line += '\n'
        if spider.name == "MianMo":
            self.file["MianMo.json"].write(line.decode("unicode_escape"))
        if spider.name == "JingHua":
            self.file["JingHua.json"].write(line.decode("unicode_escape"))
        return item

    def spider_closed(self, spider):
        for spider_name, file_obj in self.file.items():
            file_obj.close()
        for key in self.file.keys():
            with open(key, 'r') as f:
                s = f.read()
                s = s.rstrip(',\n')
                s = '[' + s + ']'
            with open(key, 'w') as f:
                f.write(s)
