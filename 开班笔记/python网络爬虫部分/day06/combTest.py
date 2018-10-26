# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 14:46:21 2018

@author: Python
"""

def CombinationNum(n, m):
    # n >= m, n,m都是自然数
    if m == 0 or n == m:
        return 1
    return CombinationNum(n-1,m-1)\
            +CombinationNum(n-1,m)

print(CombinationNum(5,3)) # 10
print(CombinationNum(5,2)) # 10

#TODO: 怎么使用动态规划来改进这个算法？








