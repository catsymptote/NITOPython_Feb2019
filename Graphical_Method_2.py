#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 12:35:17 2019

@author: catsymptote
"""

import numpy as np
import matplotlib.pyplot as plt
#%matplotlib notebook

# Grafical methods works best with only 1 variable.

x = np.arange(-3, 3, 0.1)
f = 0.4*x**3 + 3 - 2*np.cos(2*x)
#print(x)

plt.plot(x, f)
plt.plot([-4, 4], [0, 0])   # for horizontal line at f=0
plt.grid()
plt.show()
