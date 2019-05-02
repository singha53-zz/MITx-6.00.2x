#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:12:37 2019

@author: asingh
"""

# =============================================================================
# Exercise 1-1
# 6/6 points (graded)
# For the following explanations of different types of programmatic models, fill in the blank with the appropriate model the definition describes.
# 
# A ______ model is one whose behavior is entirely predictable. Every set of variable states is uniquely determined by parameters in the model and by sets of previous states of these variables. Therefore, these models perform the same way for a given set of initial conditions, and it is possible to predict precisely what will happen.
# 
#  correct  deterministic
# A ________ model is one in which randomness is present, and variable states are not described by unique values, but rather by probability distributions. The behavior of this model cannot be entirely predicted.
# 
#  correct  stochasticv
# A _______ model does not account for the element of time. In this type of model, a simulation will give us a snapshot at a single point in time.
# 
#  correct  static
# A _______ model does account for the element of time. This type of model often contains state variables that change over time.
# 
#  correct  dynamic
# A _______ model does not take into account the function of time. The state variables change only at a countable number of points in time, abruptly from one state to another.
# 
#  correct  discrete
# A ______ model does take into account the function of time, typically by modelling a function f(t) and the changes reflected over time intervals. The state variables change in an unbroken way through an infinite number of states.
# 
#  correct  continuous
# =============================================================================

# =============================================================================
# Exercise 2
# 0.0/5.0 points (graded)
# This problem asks you to write a short function that uses the the random module. Click on the above link to be taken to the Python docs on the random module, where you can see all sorts of cool functions the module provides.
# 
# The random module has many useful functions - play around with them in your interpreter to see how much you can do! To test this code yourself, put the line import random at the top of your code file, to import all of the functions in the random module. To call random module methods, preface them with random., as in this sample interpreter session:
# 
# >>> import random
# >>> random.randint(1, 5)
# 4
# >>> random.choice(['apple', 'banana', 'cat'])
# 'cat'
# How would you randomly generate an even number x, 0 <= x < 100? Fill out the definition for the function genEven(). Please generate a uniform distribution over the even numbers between 0 and 100 (not including 100).
# 
# =============================================================================
import random

def genEven():
    '''
    Returns a random number x, where 0 <= x < 100
    '''
    return 10
    
# =============================================================================
# Exercise 3-1
# 0.0/5.0 points (graded)
# Write a deterministic program, deterministicNumber, that returns an even number between 9 and 21.
# 
# =============================================================================
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return random.randrange(8, 21, 2)
       
# =============================================================================
# Exercise 4
# 3/3 points (graded)
# Are the following two distributions equivalent?
# 
# import random
# def dist1():
#     return random.random() * 2 - 1
# 
# def dist2():
#     if random.random() > 0.5:
#         return random.random()
#     else:
#         return random.random() - 1 
# 
# Yes correct
# No
# Explanation:
# 
# The random.random() distribution is uniform, so both dist1 and dist2 are a uniform distribution over [-1.0, 1.0).
# 
# Are the following two distributions equivalent?
# 
# import random
# def dist3():
#     return int(random.random() * 10)
# 
# def dist4():
#     return random.randrange(0, 10)
# 
# Yes correct
# No
# Explanation:
# 
# The random.random() distribution is uniform, and so is the random.randrange() distribution, so both dist3 and dist4 are a discrete uniform distribution over [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].
# 
# Are the following two distributions equivalent?
# 
# import random
# def dist5():
#     return int(random.random() * 10)
# 
# def dist6():
#     return random.randint(0, 10)
# 
# Yes
# No correct
# Explanation:
# 
# The random.random() distribution is uniform, and so is the random.randint() distribution. However unlike random.randrange(start, end), random.randint(start, end) returns a distribution that is inclusive of both the given start and end points.
# 
# Thus dist5 is a discrete uniform distribution over [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], but dist6 is a discrete uniform distribution over [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# 
# You can code a simple simulation to see what a distribution looks like using dictionaries:
# 
# d1 = {}
# for i in range(10000):
#     x = random.randrange(10) 
#     d1[x] = d1.get(x, 0) + 1
# d2 = {}
# for i in range(10000):
#     x = int(random.random()*10)
#     d2[x] = d2.get(x, 0) + 1
# d3 = {}
# for i in range(10000):
#     x = random.randint(0, 10)
#     d3[x] = d3.get(x, 0) + 1
# Examine the values of the three dictionaries to see what sort of distribution results!
# 
# Question to ponder: Should all the values of the dictionaries be equal? That is, should d1[x] == d1[y] for all values of x and y, where x != y and both x and y are values in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]?    
#     
# =============================================================================
    