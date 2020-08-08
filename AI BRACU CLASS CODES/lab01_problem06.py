# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:09:27 2020

@author: salman
"""
sum = 0;
k = 0
for i in range(1,100):
    if(i%3==0):
        sum = sum+i
        k = k+1
        
avg = sum/k
print(avg)

