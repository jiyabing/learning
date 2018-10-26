# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:14:57 2018

@author: Python
"""

def removeSame(L):
    # 用一个新的list，来保存L中唯一的元素
    L1=[]
    for i in L:
        if i not in L1:
            L1.append(i)
    return L1

def removeSame2(L):
    #先转换成set,由于set
    #元素的唯一性，这时已经去重
    #再转回成list    
    L = list(set(L))
    return L

def removeSame3(L):
    #巧妙的利用字典key的唯一性，
    #从而达到去重的效果
    myDict = {}
    for i in L:
        myDict[i] = 1
    L = list(myDict.keys())
    return L
    
#第四种方法：
#首先对L进行排序
#1,2,3,3,3,4,5,6,6
#每次找个基准的比较对象，如果下一个对象
#与其相同，则去掉；否则基准对象将向下走一位；
#L=[1,3,2,3,3,4,6,5,6]
#print(removeSame3(L))

#内排序：
#O(n^2)    冒泡排序，插入排序，选择排序   
#O(nlgn)   快速排序（比较点），希尔排序，堆排序
#外排序O(nlng):
#  归并排序: 分治思想，递归；

def findNum(L1, L2):
    sum1 = sum(L1)
    sum2 = sum(L2)
    if sum1 > sum2:
        return sum1- sum2
    else:
        return sum2 -sum1

L1 = [1,2,3,4,6,7,8,9]
L2 = [1,2,3,4,6,7,9]
print(findNum(L1,L2))





























