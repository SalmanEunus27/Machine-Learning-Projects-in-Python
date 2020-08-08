# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 05:33:49 2020

@author: salman
"""
c = int(input("Number of copies: "))
if (c<=100):
    TC = 50*c
else:
    TC = 50*100+30*(c-100)
    
print("The Total cost of the copies: ",TC)
    
    

