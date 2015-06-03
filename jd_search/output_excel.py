__author__ = 'Taikor'

from tutorial.pipelines import TutorialPipeline
from format_converter.converter_lib import json_to_txt
from format_converter.converter_lib import txt_to_excel

def output_excel():
    raw_output = TutorialPipeline.json_file_name
    txt = json_to_txt(raw_output)
    print('txt OK')
    txt_to_excel(txt)
    print('excel OK')

if __name__ == "__main__":
    output_excel()
