import sys
f = open(sys.argv[1],'r')
urls = f.readlines()
f.close()
import urllib2

for i in range(len(urls)):
        t = urls[i].strip()
        if t[0]>='A':
                t = chr(ord(t[0])-ord('A')+ord('a')) + t[1:]
        u = "http://"+t     
        try:
            response = urllib2.urlopen(u)
        except:
            print i,"Can't Visit",t
        print i,"Visited:",t       
