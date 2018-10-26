# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 17:45:47 2018

@author: jyb
"""

from bs4 import BeautifulSoup

doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is first paragraph <b>one</b>',
       '<p id="secondpara" align="blah">This is second paragraph <b>two</b>',
       '</html>'
       ]
soup = BeautifulSoup(''.join(doc), 'html.parser')
print(soup)

print(soup.prettify())

print(soup.contents)
print(soup.findAll('p', align='blah'))