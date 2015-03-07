import scrapy
from experiment.items import DmozItem
import base64
from Crypto.Hash import SHA256
import sys
from urlparse import urljoin
from time import ctime
import urllib2
import urlparse
from tld import get_tld

domain = {}
visited_urls = {}
MAX_LINKS = 5000

def can_make_req(d,u):

        global domain, visited_urls
        
        if d not in domain.keys():
                domain[d]=1
                visited_urls[d] = [u]
                return True

        elif domain[d]>=MAX_LINKS:
                if d in visited_urls.keys():				
	                remove_urls(d)
                return False

        elif u in visited_urls[d]:
                return False

        visited_urls[d].append(u)
        domain[d]+=1
        return True

def find_hash(message):
        if not message:
                return ""
                
        h = SHA256.new()
        h.update(message)
        return base64.urlsafe_b64encode(h.digest())[0:-1]
        
def get_url_response_hash(url):
        try:
                response = urllib2.urlopen(url)
        except:
                #print "Error occured for",url
                return "",""    

        r = response.read()+'\n'
        return r,find_hash(r)  
           
def remove_urls(d):
	global visited_urls
	del visited_urls[d]
	
	
