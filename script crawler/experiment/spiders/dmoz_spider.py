from helper import *

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    start_urls = [each.split()[0] for each in open("links_client.txt",'r').readlines()]
    allowed_domain = [each.split()[0] for each in open("allowed_domains.txt",'r').readlines()]
    
    def download_errback(self,e,url):
	print "Error!",url
        
    def parse(self, response):
        print response.url
        hrefs = response.xpath("//a/@href")
        scripts = response.xpath("//script/@src")
        for peach in hrefs:
	        url = peach.extract()
                u = urljoin(response.url,url)
                try:
                        d = get_tld(u)
                        if can_make_req(d,u):
                                #print u
                                yield scrapy.Request(u, callback=self.parse,errback = lambda x:self.download_errback(x,url))
                except:
                        print "Error in tld", u
                               
        #item_h = DmozItem()
        #item_h['link'] = response.url     
        #item_h['contents'] = response.body+'\n'
        #item_h['hash'] = find_hash(response.body+'\n')
        #item_h['type'] = "html"
        #item_h['time'] = ctime()
        #item_h['count'] = 1
        #item_h['path'] = ""
        #item_h['visited'] = 1
        #if item_h['hash']:
        #     yield item_h
        
        #print "Script Collection!"
        for each in scripts:
                url = each.extract()
                if not url:
                   continue
	        item_s = DmozItem()
	        item_s['link'] = urljoin(response.url,url)                
                item_s['contents'],item_s['hash'] = get_url_response_hash(item_s['link'])
                item_s['type'] = "script"
                item_s['time'] = ctime()
                item_s['count'] = 1
	        item_s['path'] = ""
	        item_s['visited'] = 1
	        if item_s['hash']:
                   yield item_s            
                   
