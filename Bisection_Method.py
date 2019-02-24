#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 12:03:17 2019

@author: catsymptote
"""

import math

def f(x):
    return 0.4*x**3 + 3 - 2*math.cos(2*x)


presisjon = 0.001

a = -3
b = 3
c = (a+b)/2

while abs(f(c)) >= presisjon:
    if f(a)*f(c) > 0:
        a = c
    else:
        b = c
    
    c = (a+b)/2
    
    #print()
    #print(a,b,c)
    #print(f(a), f(b), f(c))

print(c)
