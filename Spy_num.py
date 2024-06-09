# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:05:03 2024

@author: user
"""

n=int(input("Enter the number"))
sum=0
mul=1
while(n):
    r=n%10
    sum=sum+r
    mul=mul*r
    n=n//10
    
if(sum==mul):
    print("Spy Number")
else:
    print("Not a spy number")
    
