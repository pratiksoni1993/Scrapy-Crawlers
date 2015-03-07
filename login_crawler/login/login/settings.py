# -*- coding: utf-8 -*-

# Scrapy settings for login project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'login'

SPIDER_MODULES = ['login.spiders']
NEWSPIDER_MODULE = 'login.spiders'
COOKIES_ENABLED = True
COOKIES_DEBUG = True
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    #'login.middlewares.ProxyMiddleware': 100,
    #'login.middlewares.RedirectMiddleware' : 100
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'login (+http://www.yourdomain.com)'
