from scrapy.spider import Spider
from scrapy.http import FormRequest
from loginform import fill_login_form
from urlparse import urljoin
import scrapy 
class LoginSpider(Spider):
    name = "login"
    start_urls = [
    #"http://zencart.com/index.php?main_page=login"
    #"http://192.168.56.102/phpScheduleIt/" #phpScheduleit
    #"http://192.168.56.106/index.php/customer/account/login/" #Magneto"
    #"http://192.168.56.101/profile.php?action=login" #Astrospaces
    #"http://192.168.56.102/CubeCart/index.php?_a=login"#Cubecart
    #"http://192.168.56.103/dokeos/index.php" #Dokeos
    #"http://192.168.56.104/efront/www/index.php?" #eFront
    #"http://192.168.56.105/elgg/" #Elgg
    #"http://192.168.56.107/owncloud/" #owncloud
    #"http://192.168.56.108/index.php?route=account/login" #opencart
    #"http://192.168.56.109/index.php/site/login" #x2crm
    #"http://192.168.56.110/src/login.php" #squirrelmail
    #"http://192.168.56.101/catalog/login.php" #osCommerce
    #"http://192.168.56.103/piwigo-2.0.0/identification.php" #piwigo
    #"http://192.168.56.102/login.php" #Phorum
    #"http://192.168.56.109/prestashop/authentication.php" #PrestaShop
    "http://192.168.56.106/cpg/login.php?referer=index.php" #Gallery
    ]
    
    credentials = {
        "http://zencart.com/index.php?main_page=login":['student@student.com','student'], #zencart
        "http://192.168.56.102/phpScheduleIt/":['student@email.com','student'], #phpscheduleit
        "http://192.168.56.106/index.php/customer/account/login/":['student@student.com','student'], #magneto
        "http://192.168.56.101/profile.php?action=login": ['student@student.com','student'], #Astrospaces
        "http://192.168.56.102/CubeCart/index.php?_a=login" : ['student@student.com','student'], #Cubecart
        "http://192.168.56.103/dokeos/index.php":['student','student'], #Dokeos
        "http://192.168.56.104/efront/www/index.php?":['student','student'], #eFront
        "http://192.168.56.105/elgg/":['student','student'], #Elgg
        "http://192.168.56.107/owncloud/":['student','student'], #owncloud
        "http://192.168.56.108/index.php?route=account/login":['student@student.com','student'], #opencart
        "http://192.168.56.109/index.php/site/login":['student','student'], #x2crm
        "http://192.168.56.110/src/login.php":['student','student'], #squirrelmail
        "http://192.168.56.101/catalog/login.php":['student@student.com','student'], #osCommerce
        "http://192.168.56.103/piwigo-2.0.0/identification.php":['student','student'], #Piwigo
        "http://192.168.56.102/login.php":['student','student'], #Phorum
        "http://192.168.56.109/prestashop/authentication.php":['student@student.com','student'], #PrestaShop
        "http://192.168.56.106/cpg/login.php?referer=index.php":['student','student'] #Gallery
    }    
    
    def parse(self,response):
        #print "Status:",response.status       
        #print "Request Headers"
        #print response.request.headers.items()
        #print "\n\n"
        #print "Response Headers"
        #print response.headers.items()
        #print "\n\n"
          
        login_user = self.credentials[response.request.url][0]
        login_pass = self.credentials[response.request.url][1]
        args, url, method, name , number = fill_login_form(response.url, response.body, login_user, login_pass)
       
        if name:
                yield FormRequest.from_response(response, method=method, formdata=args, formname=name, callback=self.after_login)        
        else:
                yield FormRequest.from_response(response, method=method, formdata=args, formnumber=number, callback=self.after_login)
        
                         
     
    def after_login(self, response):
                #print "Login Request Headers"
                #print response.request.headers
                #print "\n\n"
                #print "Login Response Headers"
                #print response.headers
                #print "\n\n"
                print "After Login Attempt"
                
                #print response.headers
                #print response.body
                if response.headers.get('Refresh'):
                
                        new_url = urljoin(response.url,response.headers.get('Refresh').split(';')[1].split("=")[1])
                        yield scrapy.Request(new_url,callback=self.after_login1)
                
                elif response.headers.get('Location'):
                        print "Have to make another request" 
                               
                else:
                        if "Log Out" in response.body or "Logout" in response.body or "Log out" in response.body or "Log Off" in response.body: 
                                print "Yes!!!"
                                #Crawl from here!!    
                        elif "administrator" in response.url: #This is for eFront
                                print "Yes!!!" 
                        elif "webmail.php" in response.url:
                                print "Yes!!"
                        else:        
                                print "Sorry"
                                
                        
                
    def after_login1(self,response):
                #print response.body
                if "Log Out" in response.body or "Logout" in response.body or "Log out" in response.body:
                        print "Yeess, in"  
                        #crawl from here
