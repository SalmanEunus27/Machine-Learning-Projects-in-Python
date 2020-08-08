# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 19:59:44 2020

@author: salman
"""
list = [2,7,1,19,15,12]
a = max(list)
b = min(list)
sum1 = a+b
new_list = set(list)
new_list.remove(max(new_list))
new_list.remove(min(new_list))
sum2 = max(new_list)+min(new_list)
new_list1 = set(new_list)
new_list1.remove(max(new_list1))
new_list1.remove(min(new_list1))
sum3 = max(new_list1)+min(new_list1)
print("The sum of the smallest and largest number is: ",sum1)
print("The sum of the second smallest and second largest number is: ",sum2)
print("The sum of the third smallest and third largest number is: ",sum3)