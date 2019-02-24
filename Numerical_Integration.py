#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 13:12:02 2019

@author: catsymptote
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt

# Function f
def f(x):
    return x*np.sin(np.sqrt(x))


# Rectanle method setup
a = 0
b = 10
N = 100
delta = (b-a)/100
x = a + delta/2
area = 0


# Rectangle method
for i in range(N):
    height = f(x)
    rectangle = height * delta
    area += rectangle
    x = x + delta

print(area)


# Graphing
x = np.arange(0, 10, 0.01)
plt.plot(x, f(x))
plt.grid()
plt.show()
