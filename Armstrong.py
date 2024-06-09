# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:38:50 2024

@author: user
"""

num=int(input("Enter the number"))
ord=len(str(num))
sum=0
temp=num

while(num):
    r=num%10
    d=r**ord
    sum+=d
    num=num//10
    
if temp==sum:
    print("Armstrong")
else:
    print("Not armstrong")
    

    
