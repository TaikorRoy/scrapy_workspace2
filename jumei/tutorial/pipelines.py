# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
import re


def html_stripper(str_a):
    line = str_a
    patterns = ['' for i in range(5)]
    patterns[0] = r'<ahref.+?>'
    patterns[1] = r'<span.+?</span>'
    patterns[2] = r'<em.+?>'
    patterns[3] = r'</em>'
    patterns[4] = r'</a>'
    for pattern in patterns:
        line = re.sub(pattern, "", line, re.DOTALL)
    return line


class TutorialPipeline(object):
    json_file_name = 'MianBuDiShuang.json'

    def __init__(self):
        self.file = codecs.open(TutorialPipeline.json_file_name, 'wb', encoding='utf-8')
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def process_item(self, item, spider):
        line = json.dumps(dict(item))
        line = line.replace('\\r', '')
        line = line.replace('\\n', '')
        line = line.replace('\\t', '')
        line = line.replace(' ','')
        line = html_stripper(line)
        line = line.replace('}', '},')
        self.file.write(line.decode("unicode_escape"))
        return item

    def spider_closed(self, spider):
        self.file.close()
        with open(TutorialPipeline.json_file_name, 'r') as f:
            s = f.read()
            s = s.rstrip(',')
            s = '[' + s + ']'
        with open(TutorialPipeline.json_file_name, 'w') as f:
            f.write(s)