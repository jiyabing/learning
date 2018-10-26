# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 17:20:25 2018

@author: jyb
"""

from lxml import etree

lxmlStr = '''
<bookstore>
<book>
  <title lang="en">Harry Potter</title>
  <author>J K. Rowling</author> 
  <year>2005</year>
  <price>29.99</price>
</book>
<book>
  <title lang="zh">hello world</title>
  <author>J K. Rowling</author> 
  <year>2005</year>
  <price>29.99</price>
</book>
</bookstore>
'''

# 根节点
root = etree.fromstring(lxmlStr)
print(root)

elements = root.xpath('//book/title')
print(elements[0].text)
print(elements[0].attrib)


attrs = root.xpath('//@lang')
print(attrs)