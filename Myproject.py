# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 14:04:56 2021

@author: omaho
"""

import pandas as pd
print("This is a new file")
file='C:\\Users\\omaho\\downloads\public-register-03052021.xlsx'
xls=pd.ExcelFile(file) 
print(xls.sheet_names)
df1=xls.parse('Public Register', skiprows=1)
df2=xls.parse('Annual Reports', skiprows=1)
print(df1.sort_values('CHY Number'))
