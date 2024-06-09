# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 14:50:37 2024

@author: user
"""

str=input()
n=len(str)
a=""
for i in range(0,n,2):
    a=a+str[i]
print(a)


""" OR 

str=input("Enter the string")
n=len(str)
a=""
for i in range(0,n):
    if(i%2==0):
        a=a+str[i]
        
print(a)
    """

