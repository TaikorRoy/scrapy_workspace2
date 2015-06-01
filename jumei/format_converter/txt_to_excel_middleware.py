# -*- coding: utf-8 -*-
"""
Created on Mon May 25 11:52:27 2015

@author: Taikor
"""
import os
from spam_killer.file_converter_baseClass import converter

folder_path = r'C:\workspace\化妆品电商\商品目录jumei\修正后\json'
files = os.listdir(folder_path)
for i in range(len(files)):
    files[i] = os.path.join(folder_path, files[i])

for file in files:
    excel_to_txt_con = converter(file, "Txt", "Excel")
    new_path = excel_to_txt_con()
   