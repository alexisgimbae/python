#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author agimenez
# subtractring numbers by adding.

def subtract(x, y):
    acumulator = 0
    while (x > y):
        y += 1
        acumulator += 1
    return acumulator
    
print(subtract(100,2))
