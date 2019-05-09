# -*- coding: utf-8 -*-
"""
Created on Fri May  3 18:44:27 2019

@author: kdoyl
"""



from urllib import request 
snapchaturl = "http://www.bbc.com/news/business-39135278" 
html = request.urlopen(snapchaturl).read().decode('utf8') 

from bs4 import BeautifulSoup 
htmlsoup = BeautifulSoup(html, 'html.parser') 
type(htmlsoup) 
firsttitle = htmlsoup.title 

firsttitle.get_text() 

anchors = htmlsoup.find_all('a') 
type(anchors)

links = [str(link.get('href')) for link in htmlsoup.find_all('a')] 
print(links[ :4])

outlinks = [link for link in links if link.startswith('http')]
len(outlinks)
print(outlinks[:4])




import urllib.request 
url = "http://feeds.bbci.co.uk/news/rss.xml" 
xmlstring = urllib.request.urlopen(url).read().decode('utf8') 
import xml.etree.ElementTree as etree 
import io 
xmlfile = io.StringIO(xmlstring) 
tree = etree.parse(xmlfile) 
type(tree) 
root = tree.getroot() 
type(root) 
root.tag 
root.attrib 
root.text 
len(root) 
for child in root: 
    print(child)
firstchild = root[0] 
type(firstchild) 
firstchild.attrib 
{}
firstchild.text 
len(firstchild) 
firstgrandchild = firstchild[0] 
firstgrandchild.tag 
firstgrandchild.attrib 
{}
firstgrandchild.text 
itemlist = firstchild.findall('item') 
len(itemlist) 
firstitem = itemlist[0] 
firstitem.attrib 
{} 
firstitem.text 
len(firstitem) 
for element in firstitem:     
    print(element.tag, element.attrib, element.text) 