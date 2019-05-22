#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:22:28 2019

@author: asingh
"""

# =============================================================================
# Part A
# 0.0/8.0 points (graded)
# Part A: probabilities
# This part of the problem set involves some pencil-and-paper exercises. It will help you practice and understand simple probability and statistics.
# 
# Let's say Alvin will catch the flu with probability of 1/10 during any given month. Let's also assume that Alvin can catch the flu only once per month, and that if he has caught the flu, the flu virus will die by the end of the month. What is the probability of the following events?
# 
# Answer each question in reduced fraction form - eg 1/5 instead of 2/10.
# 
# He catches the flu in September, October and November.
# (1/10)*(1/10)*(1/10) = 1/1000
# 
# He catches the flu in September and then again in November, but not in October.
# (1/10)*(1- (1/10))*(1/10)
# p_getFlu * p_notFlu * p_getFlu
# (1/10)*(9/10)*(1/10) = 9/1000
#  
# He catches the flu exactly once in the three months from September through November.
# p_getFlu * p_notFlu * p_notFlu * 3 (either sept, oct or nov)
# (1/10000)*(9/1000)*(9/1000)*3 = 243/1000
# 
# He catches the flu in two or more of the three months from September through November.
# p_catchFlu_2months + p_catchFlu_3months
# 9/1000 * 3 (which of the two months?) + 1/1000 = 7/250
# =============================================================================

