# -*- coding: utf-8 -*-
"""
Created on Sun May 31 19:19:19 2020

@author: salman
"""
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d=dict()
count = 0
for line in handle:
    
    if not line.startswith('From'):continue
        
    line=line.split()
    
    if line[0]=='From':
        
        line =  line[5].split(':')
        
        for hrs in line[0].split():
            
            if hrs not in d:
                
                d[hrs]=1
            else:
                d[hrs]+=1
                
for key,value in sorted(d.items()):
    print(key,value)
