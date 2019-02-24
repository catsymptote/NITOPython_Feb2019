#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 10:22:03 2019

@author: catsymptote
"""

import math # for e


# f(x) = x^2 + 3x - e^x = 0
def f(x):
    return x**2 + 3*x - math.e**x

# f'(x) = 2x + 3 - e^x = 0
def df(x):
    return 2*x + 3 - math.e**x


def newtons_method():
    x = 5 # initial value
    x_prev = x - 100
    rel_error = 0.0001  # acceptable error (1-)
    iterations = 0
    max_iterations = 1000
        
    #while math.fabs(x_prev - x) > 0.0000000001:
    while math.fabs(1 - math.fabs(x_prev/x)) > rel_error and iterations < max_iterations:
        x_prev = x
        x = x - f(x)/df(x)
        iterations += 1

    print("Solutions \tx =",x)
    print("Iterations \ti =", iterations)
    print("Error \t\te =", math.fabs(1 - math.fabs(x_prev/x)))


newtons_method()