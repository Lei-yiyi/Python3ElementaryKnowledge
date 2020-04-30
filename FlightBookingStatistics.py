# -*- coding: utf-8 -*-

"""
Created on 2020/4/29

@author: xiaoxiaolei

@requirements: PyCharm 2017.2.3; Python 3.5.2 /Anaconda 3 (64-bit)

@decription: https://blog.csdn.net/betterzl/article/details/105847019
"""

import sys

n = int(input())
res = [0] * (n + 1)

for i in sys.stdin.readlines():
    l = i.strip().split()
    res[int(l[0])-1] += int(l[2])
    res[int(l[1])] -= int(l[2])

for j in range(1,n):
    res[j] += res[j-1]

print(res[:-1])
