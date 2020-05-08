# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 23:35:20 2020

@author: salman
"""
import torch
x = torch.Tensor([2,3])
y = torch.Tensor([5,1])
print(x*y)
#This happened on CPU , for large calculations GPU will be used
x = torch.zeros([2,5])
x.shape
print(x)



y = torch.rand([2,5])
y  = y.view([1,10])
print(y)