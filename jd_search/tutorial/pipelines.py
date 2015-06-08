# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sys
import json
import codecs
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals


class LocalFilePipeline(object):
    base_path = sys.path[0]
    relative_path = r'tutorial\data\catalog'
    real_path = os.path.join(base_path, relative_path)
    job_list = os.listdir(relative_path)
    jobs = job_list

    def __init__(self):
        self.file = {job: codecs.open(job, 'wb', encoding='utf-8') for job in LocalFilePipeline.jobs}
        # create empty files named as the file names listed in the relative_path
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def process_item(self, item, spider):
        if len(item.keys()) == 8:
            line = json.dumps(dict(item))
            line = line.replace('}', '},')
            line += '\n'
            self.file[spider.name].write(line.decode("unicode_escape"))
            # write data into a file, the name of the file is given by the name attribute of spider object (spider.name)
        return item

    def spider_closed(self, spider):
        self.file[spider.name].close()
        # close the file: spider.name
        with open(spider.name, 'r') as f:
            s = f.read()
            s = s.rstrip(',\n')
            s = '[' + s + ']'
        with open(spider.name, 'w') as f:
            f.write(s)
