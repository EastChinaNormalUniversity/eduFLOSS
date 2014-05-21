#! \usr\bin\python
# coding:utf8
import lxml.html
import urllib
from lxml.cssselect import CSSSelector

def getInfo(infoURL):
    page = urllib.urlopen(infoURL)
    html = page.read()
    page_html = lxml.html.fromstring(html)
    label = page_html.cssselect(".field-label")
    items = page_html.cssselect(".field-items, .field-item even")
    for e in label:
        print e.text_content() 

    for e in items:
        print e.text_content() 

def main():
    for j in range(58,64):
        listURL = 'http://www.openinnovation.cn/opentools/function/'+str(j)
        listPage = urllib.urlopen(listURL)
        listhtml = listPage.read()
	page_html = lxml.html.fromstring(listhtml)
	# get the information page url from the list page:
        #infoURL = page_html.cssselect("a.ttrib['href']")

        infoURL = page_html.cssselect("a[href*='openinnovation.cn/node/']")
	for URLnode in infoURL:
            getInfo(URLnode.get("href")) 
main()
