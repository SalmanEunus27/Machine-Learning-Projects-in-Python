# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 10:12:27 2020

@author: salman
"""
import math
a=1
b = -1
c = -1980
x1 = (-b+math.sqrt((b*b)-(4*a*c)))/(2*a)
x2 = (-b-math.sqrt((b*b)-(4*a*c)))/(2*a)
print("The possible values of x are: ",x1,x2)
