# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 14:19:35 2024

@author: user
"""

n=int(input("Enter the starting range"))
m=int(input("Enter the ending number"))
count=0
l=[]

print("Prime numbers are:\n")
for num in range(n,m+1):
    if num==2:
        print("Prime")

    for i in range(2,num):
        if (num%i==0):
            break
        else:
            if num not in l:
                l.append(num)
                count=count+1
                
print(l)
            
print("No. of prime numbers:"+str(count))