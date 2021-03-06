from helper import *

class DmozSpider(scrapy.Spider):
    name = "dmoz123"
    start_urls = ["https://youtube.com"]
    #start_urls = [each.split()[0] for each in open("links_client.txt",'r').readlines()][:3]
    def download_errback(self,e,url):
	pass
        
    def parse(self, response):
                    #store the html page
                    print response.url
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
                    #         yield item_h

		    #print "Yielded html",response.url
		    	
                    #print "Moving to scripts!"
                    try:
                    #if(1):
		            for each in response.xpath('//script/@src'):
                                url = each.extract()
                                if not url:
                                        continue
                                #print url        
                                #print "Inside response path and looking at", url
			        #item_s = DmozItem()
			        #item_s['link'] = urljoin(response.url,url)                
                                #item_s['contents'],item_s['hash'] = get_url_response_hash(item_s['link'])
                                #item_s['type'] = "script"
                                #item_s['time'] = ctime()
                                #item_s['count'] = 1
			        #item_s['path'] = ""
			        #item_s['visited'] = 1
			        #if item_s['hash']:
			        #   print "Yielding script"
                                #   yield item_s
			        #print "Yielded scriptYielded scriptYielded scriptYielded scriptYielded scriptYielded script"	

		    except:
		                #pass
		                print "Problems with xpath and hence  no scripts"

                    try:           
                            #extract all href on the page and crawl them
                            print len(response.xpath('*//a/@href'))
                           
                            t = response.xpath('*//a/@href') 
                            for each in t:
                                print each.extract()
		            for peach in t:
		                        print "In once"
				        global domain,visited_urls
				        url = peach.extract() 
                                        print url
		                        u = urljoin(response.url,url)
		                        #print u
				        d = urlparse.urlparse(u)[1]
			
				        #new domain found, Init the DS
				        if d not in domain.keys():
					        #print "New Domain found",d
					        domain[d]=1
					        visited_urls[d] = [u]
			
				        #exhausted max links from a domain
				        elif domain[d]>=MAX_LINKS:
					        #print "Enough Already from ",d

					        if d in visited_urls.keys():				
						        remove_urls(d)
					        break

				        #check if already visited
				        elif u in visited_urls[d]:
					        #print "Already Visited",u
				                break
			
				        #visit
		                        #print "Visiting a new url:", u
				        visited_urls[d].append(u)
				        domain[d]+=1
				        #print "New Visit ",d,u

			        #	print "Domain",d,"#urls:", domain[d]
		                        yield scrapy.Request(u, callback=self.parse,errback = lambda x:self.download_errback(x,url))
                    except:
				        pass
	        



                  
