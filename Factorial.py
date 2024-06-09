# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:21:13 2024

@author: user
"""

num=int(input("Enter the number"))
fact=1
n=num+1
if num==0:
    fact=1
    
elif num<0:
    print("Factorial doenot exist for Negetive number")

else:
    for i in range(1,n):
        fact=fact*i
    
print(fact)