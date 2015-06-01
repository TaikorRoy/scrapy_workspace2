# -*- coding: utf-8 -*-
"""
Created on Thu May 14 17:27:01 2015

@author: Taikor
"""

import os
import json

folder_path = r'C:\workspace\化妆品电商\商品目录jumei\修正后\json'
files = os.listdir(folder_path)
for i in range(len(files)):
    files[i] = os.path.join(folder_path, files[i])
    
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read() 
        
    lines = list()
    products = json.loads(content)

    for product in products:
        lines.append(product["title"])
    s = '\n'.join(lines)
    
    with open(file+'.txt', 'w', encoding='utf-8') as f:
        f.write(s)        

        
    

        