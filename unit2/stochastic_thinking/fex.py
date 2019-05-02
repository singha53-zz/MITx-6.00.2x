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
    return random.randrandge(0, 100, 2)
    
    
    
    
    
    