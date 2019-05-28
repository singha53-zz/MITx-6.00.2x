#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:34:56 2019

@author: asingh
"""

# =============================================================================
# Problem 4-1
# 0.0/10.0 points (graded)
# You are given the following function and class and function specifications for the two coding problems on this page (also available in this file, die.py):
# 
# =============================================================================
import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title != None:
        pylab.title(title)
    pylab.show()
    
die = Die([1,2,3,4,5,6,6,6,7])
numRolls = 1
numTrials = 1000

# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    longest_run = []
    for i in range(numTrials):
        iter = 1
        max_number = 0
        rolls = [die.roll() for j in range(numRolls)]
        for j in range(len(rolls)-1):
            if rolls[j+1] == rolls[j]:
                iter += 1
            else:
                iter = 1
            if max_number < iter:
                max_number = iter
        longest_run.append(max_number) if max_number > 0 else longest_run.append(1)
    makeHistogram(longest_run, numBins=10, 
                  xLabel='numTrails', yLabel='longest run', title=None)
    return sum(longest_run)/len(longest_run)
            
    
# One test case
print(getAverage(Die([1,2,3,4,5,6]), 50, 1000))
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 1, 1000))

def getAverage2(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated to 3 decimal places
    """
    # TODO
    longest_runs = []
    for i in range(numTrials):
        rolls = [die.roll() for j in range(numRolls)]
        size = 1
        max_size = 0
        for i in range(len(rolls)-1):
            if rolls[i+1] == rolls[i]:
                size += 1
            else: 
                size = 1
            if max_size < size:
                max_size = size
        if max_size > 0:
            longest_runs.append(max_size)
        else:
            longest_runs.append(1)
    makeHistogram(longest_runs, numBins = 10, xLabel = 'Length of longest run', yLabel = 'frequency', title = 'Histogram of longest runs')
    return sum(longest_runs)/len(longest_runs)

# One test case
print(getAverage2(Die([1,2,3,4,5,6]), 50, 1000))
print(getAverage2(Die([1,2,3,4,5,6,6,6,7]), 1, 1000))



