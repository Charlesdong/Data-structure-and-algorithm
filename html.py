#encoding: utf-8

import HTMLParser
import urllib
import os

class MyParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)     
        self.links = []
        self.img = []
        
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, value in attrs:
                if name == 'href':
                    self.links.append(value)
                    print value

        if tag == 'img':
            for name, value in attrs:
                if name == 'src':
                    self.img.append(value)

if __name__ == "__main__":
    url = "http://www.baidu.com/" 
    save_path = os.path.abspath("./downlaod")
    if not os.path.exists(save_path): 
        os.mkdir(save_path)

    my = MyParser()
    my.feed(urllib.urlopen(url).read())
    for i in my.img:
        urllib.urlretrieve(i, os.path.join(save_path, i.split('/')[-1]))
    my.close()
    
