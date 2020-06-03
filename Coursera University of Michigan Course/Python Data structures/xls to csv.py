# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 02:22:48 2020

@author: salman
"""
import pandas as pd

read_file = pd.read_excel (r'C:\\Users\\salma\\Downloads\\TTL.xlsx')
read_file.to_csv (r'C:\\Users\\salma\\Downloads\\TTL.csv', index = None, header=True)
