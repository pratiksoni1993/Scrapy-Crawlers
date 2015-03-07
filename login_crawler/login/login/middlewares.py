import base64

class ProxyMiddleware(object):
    # overwrite process request
    def process_request(self, request, spider):
        # Set the location of the proxy
        request.meta['proxy'] = "http://127.0.0.1:8888"

class RedirectMiddleware(object):
        def process_request(self,request,spider):
                print "this is a redirect request to"        
                print request.url
                        
        
