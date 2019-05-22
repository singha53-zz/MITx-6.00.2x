#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:40:03 2019

@author: asingh
"""

# =============================================================================
# Exercise 1-1
# 1/1 point (graded)
# Suppose we have an experiment. We toss a coin  times. Each time we collect results from a sample of size  and compute this sample's mean  and standard deviation . This experiment has an underlying distribution with mean  and standard deviation .
# 
# Which of the following does the Central Limit Theorem (CLT) guarantee (for large enough  and ):
# 
# 
# The sample means will be approximately normally distributed. correct
# The sample means will have a mean close to the mean of the original distribution . correct
# The sample means will have a variance close to the variance of the original distribution divided by the sample size . correct
# correct
# Submit
# =============================================================================

# =============================================================================
# Exercise 2
# 2/2 points (graded)
# If you wanted to run a simulation that estimates the value of  in a way similar to the Pi estimation shown in lecture, what geometric shape would you throw needles at?
# 
# 
# A square, with a smaller square drawn inside it. The smaller square is formed by connecting the larger square's midpoints.
# A cube with a sphere inscribed inside it.
# A flat line ranging from 0 to root 2 and with a subsection that spans from 0 to 1. correct
# What introduced the error for Archimedes' method of calculating Pi?
# 
# 
# Incorrect conceptual model. correct
# Calculation error.
# Not enough samples. correct
# Explanation:
# 
# For Q1, we can approximate using the following code:
# 
# def throwNeedles(numNeedles):
#     success = 0
#     for n in range(numNeedles):
#         x = random.random()
#         if (1+x)**2 < 2.0:
#             success += 1
#     sqrt2 = 1+(float(success)/numNeedles)
#     return sqrt2                  
#                 
# If the needles fall in the section from 1 to 2 then the ratio of the square of the successful random throws in the unit section between 1 and 2 to the total number of throws will approximate the decimal fraction of root 2. Since we started the lower bound at 1, we have to add 1 to the fraction to get the actual approximation of root 2.
# For Q2, Archimedes' method of calculating was not a simulation but a calculation from using polygons. The error came from the fact that Archimedes used polygon approximations instead of circles.
# 
# =============================================================================

# =============================================================================
# Exercise 3
# 2/2 points (graded)
# If you remember the Buffon Needle Problem, the ratio of the areas of a circle and a square are used to estimate the value of  by dropping needles onto the shapes, like so:
# 
# We can imagine that using different area ratios results in the estimation of different constants.
# 
# In the following boxes, you will be asked to enter in mathematical expressions. To enter in addition, multiplication, subtraction, or division, use the operators: +, *, -, /. To enter in exponentiation, use the caret (^) key. To enter in the constant , simply type pi.
# 
# What constant can you estimate using the following picture?
# 
#  rectangle height 1 and length 2 with th ebottom half of a semicircle transcibed in it
# 
# pi/2
#   correct  pi/2
#  
# Download the code used in the lecture "Finding Pi". If we now want to estimate the constant from the picture above, what should the number '4' in the line: return 4*(inCircle/float(numNeedles)) be changed to?
# 
# 2
#   correct  2
#  
# Explanation:
# 
# There are only two quadrants you want to count in the estimate of the constant, and the operation (inCircle/numNeedles) only counts needles dropped in one quadrant of the circle.
# 
# =============================================================================

# =============================================================================
# Exercise 4
# 0.0/5.0 points (graded)
# You have a bucket with 3 red balls and 3 green balls. Assume that once you draw a ball out of the bucket, you don't replace it. What is the probability of drawing 3 balls of the same color?
# 
# Write a Monte Carlo simulation to solve the above problem. Feel free to write a helper function if you wish.
# 
# import random as random
# def drawBalls(draws, L):
#     result = []
#     if not L:
#         return ''
#     for choose in range(draws):
#         draw = random.choice(L)
#         result.append(draw)
#         L.remove(draw)
#     return result
# 
# def noReplacementSimulation(numTrials):
#     '''
#     Runs numTrials trials of a Monte Carlo simulation
#     of drawing 3 balls out of a bucket containing
#     3 red and 3 green balls. Balls are not replaced once
#     drawn. Returns the a decimal - the fraction of times 3 
#     balls of the same color were drawn.
#     '''
#     count = 0
#     if numTrials == 0:
#         return null
#     L = ['R','R','R','G','G','G']
#     for i in range(numTrials):
#         if len(set(drawBalls(3, ['R','R','R','G','G','G']))) == 1:
#             count += 1
#     return count/numTrials
#     
# 
# noReplacementSimulation(numTrials = 10)
# =============================================================================


