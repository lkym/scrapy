# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import os

from itemadapter import ItemAdapter


class JdscrapyPipeline(object):
    def process_item(self, item, spider):
        print("图片路径：{0}".format(item['b_pic'][0]))
        print("商品名称：{0}".format(item['b_title'][0]))
        # print("图片路径：{0}".format(item['b_pic'][0]))
        # print("图片路径：{0}".format(item['b_pic'][0]))
        return item

class JsonPipeline(object):
    def __init__(self):
        self.folder = 'jsonFile'
        if not os.path.exists(self.folder):
            os.mkdir(self.folder)

    def process_item(self, item, spider):
        folder = 'jsonFile'
        file_name = 'businessInfo.json'
        # 去空格
        item['b_title'][0] = item['b_title'][0].strip()
        with open(folder+os.sep+file_name,"a",encoding="utf-8") as f:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(line)
        return item
