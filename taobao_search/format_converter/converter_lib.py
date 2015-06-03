# -*- coding: utf-8 -*-
__author__ = 'Taikor'

import os
import json
from file_converter_baseClass import converter


def json_to_txt(file):
    with open(file, 'r') as f:
        content = f.read()

    lines = list()
    products = json.loads(content)

    for product in products:
        sku, brand, title, type, price = '','','','',''
        if len(product["title"]) > 0:
            title = product["title"][0]
        else:
            title = "Error"
        if len(product["price"]) > 0:
            price = product["price"][0]
        else:
            price = "Error"
        l_buffer = (sku, brand, title, type, price)
        line = '\t'.join(l_buffer)
        lines.append(line)
    s = '\n'.join(lines)

    with open(file+'.txt', 'w') as f:
        f.write(s.encode('utf-8'))
    return(file+'.txt')


def txt_to_excel(file):
    excel_to_txt_con = converter(file, "Txt", "Excel")
    new_path = excel_to_txt_con()
