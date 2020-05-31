# -*- coding: utf-8 -*-
"""
Created on Sun May 31 17:04:58 2020

@author: salman
"""
fhand = open('romeo.txt')
counts = dict() 
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
        

lst = list()
for key,val in counts.items():        
   newtup = (val,key)
   lst.append(newtup)
   

lst = sorted(lst,reverse = True)

for val,key in lst [:10]:
    print(key,val)