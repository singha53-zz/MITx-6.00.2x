#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 21:26:51 2019

@author: asingh
"""

import pylab

# Problem 7

dist = [4, 10, 5, 1, 1, 6]
income = [10, 30, 90, 100, 120, 60]
pylab.scatter(dist, income)

def get_ManhattanDist(L1, L2):
    return sum([abs(i-j) for i,j in zip(L1, L2)])

p1 = []
for i in range(len(dist)):
    p2 = []
    for j in range(len(dist)):
        L1 = [dist[i], income[i]]
        L2 = [dist[j], income[j]]
        p2.append(get_ManhattanDist(L1, L2))
    p1.append(p2)
