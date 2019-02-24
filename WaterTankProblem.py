#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 14:51:37 2019

@author: catsymptote
"""

# Imports.
import math
import numpy as np
import matplotlib.pyplot as plt


# Initial constants.
h = 9
g = 9.81


def v(y):
    """ Velocity function. """
    return math.sqrt(2*g*(h - y))



def t(y):
    """
    Time function.
    d = vt + 1/2 at^2
    d = 1/2 at^2
    t^2 = 2d/g
    t = sqrt(2d/g)
    """
    return math.sqrt(2*y/g)



def d(y):
    """
    Distance function.
    d = vt + 1/2 at^2
    d = vt
    """
    return v(y) * t(y)


# Make x-values and empty max-values.
x = np.arange(0, 9, 0.01)
f = []
x_max = 0
fx_max = 0

# Loop through every x-value.
for i in range(len(x)):
    # Add point to list.
    fx = d(x[i])
    f.append(fx)

    # Find most optimal y (x).
    if fx > fx_max:
        x_max = x[i]
        fx_max = fx

# Print optimal point and its respective distance.
print(x_max, "|", round(fx_max, 2))

# Plot function
plt.plot(x, f)#, [0, 9], [9, 9])
plt.grid()
plt.show()
