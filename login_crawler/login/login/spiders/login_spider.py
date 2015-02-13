from scrapy.spider import BaseSpider
from scrapy.http import FormRequest
from loginform import fill_login_form
import scrapy 
class LoginSpider(BaseSpider):
    name = "login"
    start_urls = ["http://192.168.56.104/openemr/interface/login/login.php"]
    login_user = "student@student.com"
    login_pass = "student"
 
    def parse(self, response):
        print response.url
        #print "In parse"
        args, url, method = fill_login_form(response.url, response.body, self.login_user, self.login_pass)
        return FormRequest(url, method=method, formdata=args, callback=self.after_login)

     
    def parse_afterlogin(self,response):
        print "I am logged in now!!"
        print response.headers
        for url in response.xpath('//img/@src').extract(): 
               print url
        

    def after_login(self, response):
        
       
                print response.status
                #print "Logged in!" 
                for each in response.headers.keys():
                        print each,":",response.headers[each]
                
                for url in response.xpath('//a/@href').extract():
                        print url
                """        
                        if "pratik.soni" in url:
                                print "making request"
                                yield scrapy.Request(url,callback=self.parse_afterlogin)
                """                
