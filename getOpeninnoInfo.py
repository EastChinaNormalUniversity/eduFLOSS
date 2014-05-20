#! \usr\bin\python
# coding:utf8
import lxml.html
import urllib
from lxml.cssselect import CSSSelector

page = urllib.urlopen('http://www.openinnovation.cn/node/9664')
html = page.read()
page_html = lxml.html.fromstring(html)

def get():
    fl_selector = page_html.cssselect(".field-label")
    fi_selector = page_html.cssselect(".field-items, .field-item even")
    for e in fl_selector:
        print e.text_content() 

    for e in fi_selector:
        print e.text_content() 
get()
