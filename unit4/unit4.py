#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 14:29:00 2019

@author: asingh
"""

## Lecture 10 Experimental Data Part 1

m = 0.15
a = 9.81
F = m * a
x = 0.1015
k = F/x
k

# =============================================================================
# Exercise 2
# 2/2 points (graded)
# Which of the following lines will fit a parabola to the spring data given in the lecture file, springData.txt? Check all that work.
# 
# 
# a,b = pylab.polyfit(xVals, yVals, 2)
# model = pylab.polyfit(xVals, yVals, 2) correct
# a,b,c = pylab.polyfit(xVals, yVals, 2) correct
# correct
# Suppose the coefficients returned by polyval are in the tuple (c1, c2, c3). Which of the following lines calculate the estimated y values?
# 
# 
# estYVals = c1*xVals**2 + c2*xVals + c3 correct
# estYVals = c3*xVals**2 + c2*xVals + c1
# 
# =============================================================================

# =============================================================================
# Exercise 4
# 1/1 point (graded)
# Recall from the previous video the concept of the coefficient of determination, also known as the  value. This is computed by . The variability of the errors is computed by taking the sum of the squares of (observed - predicted) errors. We normalize this variablity by dividing it by the variability of the data, which is sum of the squares of (observation - average_observation) for each observation.
# 
# In this file, this  value is computed by the function rSquare.
# 
# In that file, revise fitData and fitData3 to report the coefficient of determination for the fitted line in each case. Did this measure of the "goodness of fit" improve when we eliminated the measurements after the spring reached its elastic limit and Hooke's Law no longer applied?
# 
# 
# Yes correct
# =============================================================================

# =============================================================================
# Lecture 11
# 
# Exercise 1
# 5/5 points (graded)
# To model data effectively, it is important to understand the underlying model that describes the data. This means that knowing the physical phenomenon or event that is being modeled is extremely important. For each of the following data/phenomena/events, describe what type of model (linear, quadratic, other) you would use to describe the underlying phenomena.
# 
# Hourly temperature from 7am to 7pm
# 
#  correct  quadratic
# Gravitational force on an object as mass increases
# 
#  correct  linear
# Displacement of a mass on a hanging spring from the ceiling
# 
#  correct  other
# Explanation:
# 
# The answer is 'other' because a spring doesn't follow a linear model once the spring goes near or past the elastic limit.
# 
# However in many situations, the mathematical model used for a spring will often be 'linear' if the elastic limit is ignored or considered to be a deviation from the model. That is an idealized spring might be modelled with a linear model, but realistically a spring requires a more complex model to take into account the behavior of the elastic limit.
# 
# It is also important to understand physical phenomena and their limitations when modeling data. Which of the following are true?
# 
# 
# Even though hourly temperature fluctuations throughout the day may oscillate for a variety of reasons (wind, cloud cover, etc), the underlying trend is quadratic and using a quadratic model is most appropriate. correct
# You can eliminate a small number of non-outlier data points in order to construct a model that has a better fit.
# At some point, some physical phenomena have limitations that do not fit their mathematical models (i.e. springs have an elastic limit). correct
# correct
# When modeling, the model that has the biggest R^2 value is always the best model.
# 
# 
# True
# False correct
# Explanation:
# 
# This statement is False. A model that explains every single point of data without error might be overfitting the data, which would not provide accurate description of the process behind the data.
# 
# =============================================================================

# =============================================================================
# Exercise 2
# 6/6 points (graded)
# Suppose you are given the following data and are asked to fit a curve to this data.
# 
# A = [1,2,3,4,5,6,7,8,9,10]
# L = [0.59,18.38, 33.01, 54.14, 72.48, 89.8, 97.07, 112.6, 142.87, 199.84]
#   
# Match each plot with the correct polynomial fit.
# 
#  linear
# Fit 1
# 
# 
# Linear correct
# Polynomial of degree 2
# Polynomial of degree 5
#  smooth polynomial
# Fit 2
# 
# 
# Linear
# Polynomial of degree 2 correct
# Polynomial of degree 5
#  looks linear until x=6 then dips down then back up
# Fit 3
# 
# 
# Linear
# Polynomial of degree 2
# Polynomial of degree 5 correct
# Is each fit an example of overfitting?
# 
#  linear
# Fit 1
# 
# 
# Yes
# No correct
#  smooth polynomial
# Fit 2
# 
# 
# Yes
# No correct
#  looks linear until x=6 then dips down then back up
# Fit 3
# 
# 
# Yes correct
# No
# 
# =============================================================================
 






















