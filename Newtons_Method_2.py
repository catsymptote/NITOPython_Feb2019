#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 10:47:09 2019

@author: catsymptote
"""

import math

def f(x):
    return 0.4*x**3 + 3 - 2*math.cos(2*x)

def df(x):
    return 0.4*3*x**2 + 4*math.sin(2*x)

x = 1


for i in range(15):
    x = x - f(x) / df(x)

print(x)

### Feil og cut-off points:
# En kan se etter en funksjonsverdi som er nærme nok 0.
# I.e. når x=0.04 er y=0.001 (som er nesten 0).
# Eller et intervall som er lite nok.
# I.e. funksjonen er negativ på x=0.03 og positiv på x=0.06.
