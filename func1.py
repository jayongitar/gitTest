# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 09:44:51 2018

@author: jay smith
"""

def f(x): return x % 3 == 0 or x % 5 == 0

values = list(filter(f, range(2,30)))
print(values)