# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 20:47:33 2024

@author: user
"""
def isHappy(n):
    sum=0
    while(n):
        r=n%10
        sq=r**2
        sum+=sq
        n//=10
    return sum

num=int(input())
temp=num

while num != 1 and num != 4:
    num=isHappy(num)
    
if(num==1):
    print("True")
else:
    print("False")
    

    

