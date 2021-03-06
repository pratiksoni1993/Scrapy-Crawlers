# -*- coding: utf-8 -*-

# Scrapy settings for experiment project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'experiment'

SPIDER_MODULES = ['experiment.spiders']
NEWSPIDER_MODULE = 'experiment.spiders'

ITEM_PIPELINES = ['experiment.pipelines.MongoDBPipeline', ]

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "web_changing"
MONGODB_COLLECTION = "subresources"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'experiment (+http://www.yourdomain.com)'
