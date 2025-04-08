# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import re

class CalscapescraperPipeline:
    def process_item(self, item, spider):
        for field in item.fields:
            if isinstance(item.get(field), str):
                cleaned = re.sub(r'\s+', ' ', item[field]).strip()
                item[field] = cleaned
        return item