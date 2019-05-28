#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 22:39:54 2019

@author: asingh
"""

# Problem 8 Part A
# =============================================================================
# 
# For this problem you are going to simulate growth of fox and rabbit population in a forest!
# 
# The following facts are true about the fox and rabbit population:
# 
# The maximum population of rabbits is determined by the amount of vegetation in the forest, which is relatively stable.
# 
# There are never fewer than 10 rabbits; the maximum population of rabbits is 1000.
# 
# For each rabbit during each time step, a new rabbit will be born with a probability of  𝑝rabbit reproduction 
# 𝑝rabbit reproduction=1.0−current rabbit populationmax rabbit population 
# In other words, when the current population is near the maximum, the probability of giving birth is very low, and when the current population is small, the probability of giving birth is very high.
# 
# The population of foxes is constrained by number of rabbits.
# 
# There are never fewer than 10 foxes.
# 
# At each time step, after the rabbits have finished reproducing, a fox will try to hunt a rabbit with success rate of  𝑝fox eats rabbit 
# 𝑝fox eats rabbit=current rabbit populationmax rabbit population 
# In other words, the more rabbits, the more likely a fox will eat one.
# 
# If a fox succeeds in hunting, it will decrease the number of rabbits by 1 immediately. Remember that the population of rabbits is never lower than 10.
# 
# Additionally, if a fox succeeds in hunting, then it has a 1/3 probability of giving birth in the current time-step.
# 
# If a fox fails in hunting then it has a 10 percent chance of dying in the current time-step.
# 
# If the starting population is below 10 then you should do nothing. You should not increase the population nor set the population to 10. 
# Start with 500 rabbits and 30 foxes.
# 
# At the end of each time step, record the number of foxes and rabbits.
# 
# Run the simulation for 200 time steps, and then plot the population of rabbits and the population of foxes as a function of time step. (You do not need to paste your code for plotting for Part A of this problem).
# 
# Use the following steps, and the template file rabbits.py (click to download .py file), as guides in your implementation of this simulation.
# 
# Step 1: Write the procedure, rabbitGrowth, that updates the number of rabbits during the first part of a time step
# 
# Step 2: Write the procedure, foxGrowth, that updates the number of rabbits and foxes during the second part of a time step
# 
# Step 3: Write the master procedure, runSimulation, that loops for some amount of time steps, doing the first part and then the second part of the simulation. Record the two populations in two different lists, and return those lists.
# 
# Paste your code for the three functions rabbitGrowth, foxGrowth, and runSimulation in the following box.
# 
# WARNING
# DO NOT define the global variables MAXRABBITPOP, CURRENTRABBITPOP, or CURRENTFOXPOP in this box. We alter the values of these variables to test your code. If you define the variables in this box, you may overwrite our values, causing your code to be marked incorrect.
# 
# CLARIFICATIONS / HINTS
# "See Full Output": If you are getting the line "0 10" in your output for "Test 4 foxGrowth" then for this particular test, your code changes the CURRENTFOXPOP (increases it if the fox population has gone below the minimum fox population), which is not the right behavior -- the code should not reset CURRENTFOXPOP.
# It is not correct to assume that there is a 1/3 chance that the population increases in "Test 3 foxGrowth". Pay special attention to the following statement in the docstring of foxGrowth(): "Each fox, based on the probabilities in the problem statement, may eat one rabbit (but only if there are more than 10 rabbits)."
# 
# =============================================================================

