# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 14:34:45 2018

@author: jyb
"""
from urllib import request
import hashlib
#默认的user-agent的设置
#print(request.urlopen(request.Request(
#        'http://www.baidu.com')).read().decode('utf8'))

def myMinMax(L):
    # 对输入参数进行判断，可以使用assert断言
    assert(len(L)>0)
    # 在参数合法的情况下，做真正的逻辑
#    if len(L) <= 0:
#        print('Input Error')
#        return None
    return minMax(L, 0, len(L)-1)

def minMax(L, start, end):
    '''
    返回一个元组，用来记录List的最大值和最小值
    '''
    if end - start <= 1:
        return (max(L[start],L[end]),min(L[start],L[end]))
    else:
        # 把L分成两部分，分别调用这个方法minMax
        middle = (start + end)//2
        # 得到(max1,min1)和(max2,min2)
        t1 = minMax(L, start, middle)
        t2 = minMax(L, middle, end)
        # 比较max1,max2可以得到最终的最大值
        # 比较min1,min2可以得到最终的最小值
        return (max(t1[0], t2[0]), min(t1[1], t2[1]))



def hashFile(fileName):
    '''
    对文件做hash
    '''
    CHUNKSIZE = 2048
    h = hashlib.sha256()
    with open(fileName, 'rb') as f:
        while True:
            chunk = f.read(CHUNKSIZE)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


if __name__ == '__main__':
    print(hashFile('note.txt'))
        