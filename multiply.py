#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author agimenez
# multyply by adding numbers.

def multiply(x, y):
    value = 0
    while (x):
        x -= 1 
        value  += y
    return value
    
print(multiply(4,2))
