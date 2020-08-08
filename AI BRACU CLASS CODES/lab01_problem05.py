# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 06:28:38 2020

@author: salman
"""
year = int(input("Please enter a year value: "))
if(year%100==0 and year%400==0):
    print(year," is a leap year")
    
elif(year%100==0 and year%400!=0):
     print(year," is not a leap year")
     
    
    