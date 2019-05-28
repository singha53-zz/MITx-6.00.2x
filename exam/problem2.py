#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:11:01 2019

@author: asingh
"""

import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals

# Problem 2-1
pylab.hist(tVals)

# Problem 2-2
pylab.hist(xVals)

# Problem 2-3
pylab.plot(xVals, zVals)

# Problem 2-4
pylab.plot(xVals, yVals)

# Problem 2-5
pylab.plot(xVals, sorted(yVals))

# Problem 2-6
pylab.plot(sorted(xVals), yVals)

# Problem 2-7
pylab.plot(sorted(xVals), sorted(yVals))
