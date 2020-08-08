# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 21:36:10 2020

@author: salman
"""
list = [2,19,3,14,9,25,35,17,12,6]
sum = 0
a = max(list)
b = min(list)
for i in list:
    sum = sum+i
    
average = sum/len(list)
print("The difference between average and smallest number: ",average-b)
print("The difference between average and largest number: ",a-average)
