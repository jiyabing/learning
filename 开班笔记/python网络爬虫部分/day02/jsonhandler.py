# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 16:55:19 2018

@author: jyb
"""

import json

jsonDict = {'One': "1", 'Two': "2"}
for key, value in jsonDict.items():
    print(key, value)

# dict ---> json str
# json encode
jsonDumps = json.dumps(jsonDict)
print(jsonDumps)

# json str ---> dict
# json decode
jsonLoads = json.loads(jsonDumps)
for key, value in jsonLoads.items():
    print(key, value)