# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# import pymongo
import pymongo

# scrapy configurations
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

class HwzscraperMongoDBPipeline(object):
    def __init__(self):
        # specify the connection for mongoDB
        connection = pymongo.MongoClient(settings["localhost"], settings["27017"])  
        db = connection[settings["HwzPosts"]]
        self.collection = db[settings[["threads"]]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            log.msg("Thread post added to MOngoDB database!", 
            level=log.DEBUG, spider=spider)
        return item
