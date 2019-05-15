#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 17:25:08 2019

@author: asingh
"""

# =============================================================================
# Inferential Statistics
# Exercise 1
# 3/3 points (graded)
# A fair two-sided coin is flipped 4 times. It comes up heads all four times. What is the probability that it comes up heads on the fifth flip? Answer in reduced fraction form - eg 1/5 instead of 2/10.
# 
# 1/2
#   correct  1/2
# Explanation:
# 
# Answer: 1/2 - Previous tosses don't influence the result of the next toss.
# 
# A fair two-sided coin is flipped 1000 times. It comes up heads every time. Which is correct?
# 
# 
# Regression to the mean tells us that the next 1000 tosses will be almost all tails.
# Regression to the mean tells us that the next few tosses will be not as extreme as the first 1000. correct
# Next we toss a huge ball with 1,000 dots on it. Half the dots are red and the other half are blue. We roll the ball and when it stops, we note the color of the dot on the very top of the ball.
# 
# True or False? If we roll it four times, and it comes up red once and blue three times, then we have proved that the ball is biased.
# 
# 
# True
# False correct
# Explanation:
# 
# Answer: False - We don't know if it is a fair or biased ball at this point; the sample size is too small.
# 
# =============================================================================

# =============================================================================
# Exercise 2
# 5/5 points (graded)
# For the questions below, please try to think about the solution in your head before using an IDE or a calculator to compute it. The goal of these questions is to give you some intuition about the topics we've been discussing.
# 
# Which of the following populations has the largest variance?
# 
# 
# [0, 1, 2, 3, 4, 5, 6]
# [3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 3, 6, 6, 6] correct
# Explanation:
# 
# In all three sequences, the mean is 3, but the elements in C are, on average, farther away from the mean, so it has the largest variance.
# 
# Which of the following populations has the largest variance?
# 
# 
# [3, 3, 5, 7, 7]
# [1, 5, 5, 5, 9] correct
# Explanation:
# 
# In both A and B, the sum of the absolute difference is 8 (A: 5-3 + 5-3 + 5-5 + 7-5 + 7-5 = 8; B: 5-1 + 5-5 + 5-5 + 5-5 + 9-5 = 8), but the variance is computed by taking the square of the difference - A: (5-3)^2 + (5-3)^2 + (5-5)^2 + (7-5)^2 + (7-5)^2 = 4 + 4 + 0 + 4 + 4 = 16; B: (1-5)^2 + (5-5)^2 + (5-5)^2 + (5-5)^2 + (9-5)^2 = 16 + 0 + 0 + 0 + 16 = 32.
# 
# So they both have the same average absolute value deviation, but in B, the variance is higher.
# 
# If a number is removed from a population, the standard deviation of that population will always decrease.
# 
# 
# True
# False correct
# Explanation:
# 
# Consider the population [1, 3, 5, 7, 9]. Removing 5 will increase the standard deviation.
# 
# You are taking samples of the ages of two populations, A and B. Population A is all the residents of San Francisco, while Population B is all the residents of Los Angeles.
# 
# The sample from Population A has a mean of 35 and a standard deviation of 1. The sample from Population B has a mean of 45 and a standard deviation of 15. Which of the following are certain?
# 
# 
# You will not find an individual in Population A that is over the age of 37.
# The average age of Population A is lower than the average age of Population B.
# The average age of the sample of Population A is lower than the average age of the sample of Population B. correct
# If the sample size of each population is 10, then you can conclude that your sample accurately represents the population.
# A sample size of 1 million is more appropriate than a sample size of 10 for these populations. correct
# correct
# The 95% confidence interval for a normal distribution of data with a mean of 5 and a standard deviation of 2 is 5 +/- ________
# 
# 4
#   correct  3.92
#  
# We accept answers between 2*1.96 = 3.92 and 2*2 = 4
# =============================================================================
def stdDevOfLengths(L):
    import math
    
    if not L:
        return float('NaN')
    L = list(map(lambda x: len(x), L))
    mean = sum(L)/len(L)
    center_sq = list(map(lambda x: (x - mean)*(x - mean), L))
    var = sum(center_sq)/len(L)
    return math.sqrt(var)

stdDevOfLengths(['ab', 'a', 'abd'])

# =============================================================================
# Exercise 4
# 3/3 points (graded)
# The coefficient of variation is the standard deviation divided by the mean. Loosely, it's a measure of how variable the population is in relation to the mean.
# 
# Figure 1 shows the skyline of Pythonland, and Figure 2 shows the skyline of Montyland.
# 
# histogram with 4 bars, heights h1, h2, h3, h4 histogram with 4 bars, heights relative to previous graph, but are smaller
# Considering the heights of buildings in Pythonland and Montyland, which has a larger coefficient of variation?
# 
# 
# Pythonland
# Montyland correct
# Explanation:
# 
# Both have the same standard deviation (the heights are just shifted, which means the means are different, but the standard deviation is the same).
# 
# Montyland's buildings are short, but Pythonland's buildings are tall. So the coefficient of variation for Pythonland and Montyland have the same numerator, but a large denominator for Pythonland, and a small one for Montyland. That makes Montyland's coefficient of variation larger.
# 
# Which of the following populations has the highest coefficient of variation?
# 
# 
# [1, 2, 3] correct
# [11, 12, 13]
# [0.1, 0.1, 0.1]
# Explanation:
# 
# Both A and B have the same standard deviation, but B has a larger mean. So, A has a higher coefficient of variation. Despite having the smallest mean, C has a standard deviation of 0, and so its coefficient of variation is 0 as well.
# 
# Compute the coefficient of variation of [10, 4, 12, 15, 20, 5] to 3 decimal places.
# 
# 0.503
#   correct  .503
# =============================================================================

L = [10, 4, 12, 15, 20, 5]
mean = sum(L)/len(L)
center_sq = list(map(lambda x: (x - mean)*(x - mean), L))
var = sum(center_sq)/len(L)
std = math.sqrt(var)
std/mean
    
# =============================================================================
# Exercise 5
# 8/8 points (graded)
# In the lecture, you saw a uniform and a normal distribution. There is another type of distribution, called an exponential distribution. For the following real-life situations, fill in the blank with the appropriate distribution model (normal, uniform, or exponential) that would best simulate the situation.
# 
# Rolling a fair 6-sided die
# 
#  correct  uniform
# Sum of rolling 2 fair 6-sided dice
# 
#  correct  normal
# Women's shoe sizes
# 
#  correct  normal
# Human intelligence (IQ) scores
# 
#  correct  normal
# Amount of mold on bread, assuming an infinite supply of bread
# 
#  correct  exponential
# The winning lottery numbers
# 
#  correct  uniform
# Skilled person throwing darts at a dart board
# 
#  correct  normal
# Radioactive decay (time between successive atom decays)
# 
#  correct  exponential
# =============================================================================
    
# =============================================================================
#  Exercise 6
# 4/4 points (graded)
# Samples were taken from a distribution, and the histogram of those samples is shown here:
#  bell curve centered around 2, 0
# Which of the following distributions were the samples taken from?
# 
# 
# Uniform Distribution
# Exponential Distribution
# Normal Distribution correct
# Explanation:
# 
# This is a normal (aka Gaussian) distribution.
# 
# Which of the following histograms best matches samples taken from a uniform distribution between 0 and 2?
#  bell curve centered around 1, 0 and max height at 300
# Figure 1
# 
#  equal height bars starting from 0 to 2 and each approx 100 height
# Figure 2
# 
#  equal height bars starting from 0 to 1 and each approx 200 height
# Figure 3
# 
#  exponentially decreasing bars starting from 0 with the tail at 2
# Figure 4
# 
# 
# Figure 1
# Figure 2 correct
# Figure 3
# Figure 4
# Each of the following histograms was generated by sampling a different normal distribution. Which histogram best matches the normal distribution with the highest variance of the three?
#  bell curve centered around 1.5, tails at -1 and 3, max height at 700
# Figure 1
# 
#  bell curve centered around 2, tails at -1 and 5, max height at 400
# Figure 2
# 
#  bell curve centered around 0, tails at -5 and 5, max height at 200
# Figure 3
# 
# 
# Figure 1
# Figure 2
# Figure 3 correct
# Mary's Clothes Shoppe is a moderatly busy store. Which of the following histograms best matches observations of how much time (in minutes) there is between customer arrivals? That is, which histogram helps best predict how much time until the next customer comes into the Clothes Shoppe.
# For each histogram, 1000 observations were made. The x-axis is measured in minutes, and the height of each bar at minute m corresponds to how many times there was an m minute wait until the next customer arrived.
# 
#  exponentially decreasing bars starting from 0 with the tail at 20 max height 450
# Figure 1
# 
#  bell curve centered around 10, tails at 0 and 20, max height at 350
# Figure 2
# 
#  equal height bars starting from 0 to 20 and each approx 100 height
# Figure 3
# 
# 
# Figure 1 correct
# Figure 2
# Figure 3
# Explanation:
# 
# The best match is Figure 1. It is common for a busy store to have frequent customers and it is most common that the next customer arrives shortly after the previous customer. It is rare - but not impossible - for there to be a 15+ minute gap between one customer and the next; but typically we see 1-5 minute gaps.
# 
# Generally, inter-arrival time problems are modeled well by exponential distributions.   
#     
# =============================================================================
    
    
    
    
    
    
    
    
    
    
    