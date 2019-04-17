#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 08:49:05 2019

@author: asingh
"""

# Lecture 2 - Decision Trees and Dynamic Programming
# =============================================================================
# Exercise 1
#  Bookmark this page
# Exercise 1
# 0.0/10.0 points (graded)
# Here is the lecture from 6.00.1x on generators. Additionally, you can also take a look at Chapter 8.3 in the textbook.
# 
# For the following problem, consider the following way to write a power set generator. The number of possible combinations to put n items into one bag is . Here, items is a Python list. If need be, also check out the docs on bitwise operators (<<, >>, &, |, ~, ^).
# 
# # generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        print('i = ' + str(i))
        combo = []
        for j in range(N):
            print('j = ' + str(j))
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                print(i >> j)
                print((i >> j) % 2)
                print((i >> j) % 2 == 1)
                combo.append(items[j])
        yield combo

a = powerSet([1, 2, 3])
a.__next__()

# =============================================================================
# i >> j (bitwise operator)
# x >> y
# Returns x with the bits shifted to the right by y places. 
# This is the same as //'ing x by 2**y.
# =============================================================================


# As above, suppose we have a generator that returns every combination of objects in one bag. We can represent this as a list of 1s and 0s denoting whether each item is in the bag or not.
# 
# Write a generator that returns every arrangement of items such that each is in one or none of two different bags. Each combination should be given as a tuple of two lists, the first being the items in bag1, and the second being the items in bag2.
# 
def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        combo1 = []
        combo2 = []
        for j in range(N):
            # test bit jth of integer i
            if (i // 3**j) % 3 == 0:
                combo1.append(items[j])
            elif (i // 3**j) % 3 == 1:
                combo2.append(items[j])
        yield (combo1, combo2)
      
b = yieldAllCombos([1, 2, 3])
b.__next__()

# Note this generator should be pretty similar to the powerSet generator above.
# 
# We mentioned that the number of possible combinations for N items into one bag is . How many possible combinations exist when there are two bags? Think about this for a few minutes, then click the following hint to confirm if your guess is correct. Remember that a given item can only be in bag1, bag2, or neither bag -- it is not possible for an item to be present in both bags!
# =============================================================================

# =============================================================================
# How many possible combinations exist for N items into two bags?
# With two bags, there are 3^n possible combinations available.
# With one bag we determined there were 2^n possible combinations available
# by representing the bag as a list of binary bits, 0 or 1. 
# Since there are N bits, and they can be one of two possibilities, 
# there must be 2^n possibilities.
# With two bags there thus must be 3^n possible combinations. 
# You can imagine this by representing the two bags as a list of 
# "trinary" bits, 0, 1, or 2 (a 0 if an item is in neither bag; 
# 1 if it is in bag1; 2 if it is in bag2). 
# With the "trinary" bits, there are N bits that can each be 
# one of three possibilities - thus there must be 3^n possible 
# combinations.
# 
# =============================================================================

# =============================================================================
# Exercise 2
# 4/4 points (graded)
# Dynamic programming can be used to solve optimization problems where the size of the space of possible solutions is exponentially large.
# 
# True correct
# False
# Dynamic programming can be used to find an approximate solution to an optimization problem, but cannot be used to find a solution that is guaranteed to be optimal.
# 
# True
# False correct
# Recall that sorting a list of integers can take  using an algorithm like merge sort. Dynamic programming can be used to reduce the order of algorithmic complexity of sorting a list of integers to something below , where n is the length of the list to be sorted.
# 
# True
# False correct
# Problem: I need to go up a flight of  stairs. I can either go up 1 or 2 steps every time. How many different ways are there for me to traverse these steps? For example:
# 3 steps -> could be 1,1,1 or 1,2 or 2,1
# 4 steps -> could be 1,1,1,1 or 1,1,2 or 1,2,1 or 2,1,1 or 2,2
# 5 steps -> could be 1,1,1,1,1 or 1,1,1,2 or 1,1,2,1 or 1,2,1,1 or 2,1,1,1 or 2,2,1 or 1,2,2 or 2,1,2
# Does this problem have optimal substructure and overlapping subproblems?
# 
# 
# It has optimal substructure and overlapping subproblems correct
# It doe not have optimal substructure and does not have overlapping subproblems
# It has optimal substructure and does not have overlapping subproblems
# It does not have optimal substructure and it has overlapping subproblems
# Explanation to #4:
# 
# Optimal substructure: "Optimal solution" in this case is the number of possible ways of traversing k steps -- it’s a somewhat trivial sense of “optimal”, with one good (correct) answer and infinite bad (incorrect) answers. But we can indeed figure out the solution for k+1 or k+2 steps using the solution to k.
# 
# Overlapping subproblems: Say there are 8 steps. The solution for 5 steps is required at least three times, as you can do [1,1,1] or [1,2] or [2,1] to reduce the solution to 5 steps.
# 
# =============================================================================
