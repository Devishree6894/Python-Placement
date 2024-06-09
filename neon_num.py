# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:58:22 2024

@author: user
"""

num=int(input("Enter the number"))
sum=0
temp=num
sq=num**2
while(sq):
    r=sq%10
    sum+=r
    
    sq//=10
    
if temp==sum:
    print("Neon")
else:
    print("Not Neon number")
    
