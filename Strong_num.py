# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 14:28:37 2024

@author: user
"""

sum=0
num=int(input("Enter the number"))
temp=num
while(num):
    i=1
    f=1
    r=num%10
    while(i<=r):
        f=f*i
        i=i+1
        
    sum=sum+f
    num=num//10
if(sum==temp):
    print("Strong num")
else:
    print("Not strong num")
    
