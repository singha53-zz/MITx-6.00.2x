#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 08:42:51 2019

@author: asingh
"""

# Unit1
## Lecture 1 - Optimization and the Knapsack Problem
# =============================================================================
# Exercise 1
# 6/6 points (graded)
# As a burgler robs a house, she finds the following items:
# 
# Dirt - Weight: 4, Value: 0
# Computer - Weight: 10, Value: 30
# Fork - Weight: 5, Value: 1
# Problem Set - Weight: 0, Value: -10
# This time, she can only carry a weight of 14, and wishes to maximize the value to weight ratio of the things she carries. She employs three different metrics in an attempt to do this, and writes an algorithm in Python to determine which loot to take.
# 
# The algorithm works as follows:
# 
# Evaluate the metric of each item. Each metric returns a numerical value for each item.
# For each item, from highest metric value to lowest, add the item if there is room in the bag.
# Describe the heuristic that each of the following 3 metrics uses, and choose the result of running the algorithm with each metric.
# 
# Metric 1:
# 
def metric1(item):
    return item.getValue() / item.getWeight() 
# Which heuristic does Metric 1 employ?
# 
# 
# Choose the lightest object first.
# Choose the most valuable object first.
# Choose the item with the best value to weight ratio first. correct
# What will be the result of running the burgler's algorithm with Metric 1?
# 
# 
# The algorithm runs and returns the optimal solution.
# The algorithm runs and returns a non-optimal solution.
# The algorithm does not run. correct
# Metric 2:
# 
def metric2(item):
    return  -item.getWeight()
# Which heuristic does Metric 2 employ?
# 
# 
# Choose the lightest object first. correct
# Choose the most valuable object first.
# Choose the item with the best value to weight ratio first.
# What will be the result of running the burgler's algorithm with Metric 2?
# 
# 
# The algorithm runs and returns the optimal solution.
# The algorithm runs and returns a non-optimal solution. correct
# The algorithm does not run.
# Metric 3:
# 
def metric3(item):
    return item.getValue()
# Which heuristic does Metric 3 employ?
# 
# 
# Choose the lightest object first.
# Choose the most valuable object first. correct
# Choose the item with the best value to weight ratio first.
# What will be the result of running the burgler's algorithm with Metric 3?
# 
# 
# The algorithm runs and returns the optimal solution.
# The algorithm runs and returns a non-optimal solution. correct
# The algorithm does not run.
# =============================================================================

# =============================================================================
# Exercise 2
#  Bookmark this page
# Exercise 2
# 6/6 points (graded)
# Please help the burglar out! For each of the following greedy metrics, what should be the burglar's first two choices of items? Here's a table of the items from the slides:
# 
# item	$	kg	$/kg
# clock	175	10	17.5
# picture	90	9	10
# radio	20	4	5
# vase	50	2	25
# book	10	1	10
# computer	200	20	10
# For this problem, assume that the maximum weight the burglar can carry is 20.
# 
# Metric: max value
# 
# The burglar should first pick:
# 
#  correct  computer
# and should next pick:
# 
#  correct  no more space
# Metric: min weight
# 
# The burglar should first pick:
# 
#  correct  book
# and should next pick:
# 
#  correct  vase
# Metric: max value/weight ratio
# 
# The burglar should first pick:
# 
#  correct  vase
# and should next pick:
# 
#  correct  clock
# =============================================================================

# =============================================================================
# Exercise 3
#  Bookmark this page
# Exercise 3
# 3/3 points (graded)
# For these questions, you'll be asked to give the big-O upper bound runtime for some Python functions. In your answer, please omit the "O( )" portion of the answer and simply write a mathematical expression.
# 
# Use +, -, / signs to indicate addition, subtraction, and division. Explicitly indicate multiplication with a * (ie say "6*n" rather than "6n"). Indicate exponentiation with a caret (^) (ie "n^4" for ). Indicate base-2 logarithms with the word log2 followed by parenthesis (ie "log2(n)").
# 
# What this all means is if an answer is, for example, , please simply write "n^4" in the box.
# 
# What is the big-O upper bound runtime for the function look_for_things, where n is defined as the number of elements in myList?
# 
NUMBER = 3
def look_for_things(myList):
    """Looks at all elements"""
    for n in myList:
        if n == NUMBER:
            return True
    return False
# n
#   correct  n
#  
# What is the big-O upper bound runtime for the function look_for_other_things, where n is defined as the number of elements in myList?
# 
NUMBER = 3
def look_for_other_things(myList):
    """Looks at all pairs of elements"""
    for n in myList:
        for m in myList:
            if n - m == NUMBER or m - n == NUMBER:
                return True
    return False
# n^2
#   correct  n^2
#  
# What is the big-O upper bound runtime for the function look_for_all_the_things, where n is defined as the number of elements in myList?
# 
# You do not need to account for the runtime of get_all_subsets; the code is provided so you can see how many subsets it generates, as that will be a factor in your answer.
# 
def get_all_subsets(some_list):
    """Returns all subsets of size 0 - len(some_list) for some_list"""
    if len(some_list) == 0:
        # If the list is empty, return the empty list
        return [[]]
    subsets = []
    first_elt = some_list[0]
    rest_list = some_list[1:]
    # Strategy: Get all the subsets of rest_list; for each
    # of those subsets, a full subset list will contain both
    # the original subset as well as a version of the subset
    # that contains first_elt
    for partial_subset in get_all_subsets(rest_list):
        subsets.append(partial_subset)
        next_subset = partial_subset[:] + [first_elt]
        subsets.append(next_subset)
    return subsets
# 
NUMBER = 3
def look_for_all_the_things(myList):
    """Looks at all subsets of this list"""
    # Make subsets
    all_subsets = get_all_subsets(myList)
    for subset in all_subsets:
        if sum(subset) == NUMBER:
            return True
    return False
# 2^n
#   correct  2^n
#  
# Explanation:
# 
# The point of this exercise was to get you thinking about the complexity of functions, specifically the complexity of different ways to enumerate items. Keep these complexities in mind as you continue throughout this lecture sequence. It might sound great to always get the very best solution by enumerating all possible choices - but the downside to this approach is the terribly high complexity!
# 
#  is the complexity for the final question because we are enumerating all possible subsets of a set, known as the "power set" of a set. We will talk about power sets more in the next videos. Technically, the complexity is actually  because the sum() is , but  is already large enough that we can ignore the  multiplier.
# =============================================================================
