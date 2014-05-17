'http://www.openinnovation.cn/node/9660'#! \usr\bin\python
# coding:utf8
import lxml.html
import urllib
from lxml.cssselect import CSSSelector

page = urllib.urlopen('http://www.openinnovation.cn/node/9667')
html = page.read()
page_html = lxml.html.fromstring(html)

def get_label():
    fl_selector = page_html.cssselect(".field-label")
    for e in fl_selector:
        print e.text_content() 

def get_item():
    fi_selector = page_html.cssselect(".field-item even")
    for e1 in fi_selector:
        print e1.text_content() 

get_label()
get_item()
