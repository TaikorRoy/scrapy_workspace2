# -*- coding: utf-8 -*-
__author__ = 'Taikor'


import json
import codecs


def load_product_obj(file):
    with codecs.open(file, 'r', encoding='utf-8') as f:
        s = f.read()
    json_obj = json.loads(s)
    return json_obj

