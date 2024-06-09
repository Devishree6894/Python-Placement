# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 16:22:35 2024

@author: user
"""

m1=int(input())
m2=int(input())
m3=int(input())

avg1=(m1+m2)/2
avg2=(m2+m3)/2
avg3=(m3+m1)/2

print("Best average is:")

if(avg1>avg2 and avg1>avg3):
    print(avg1)
elif(avg2>avg1 and avg2>avg3):
    print(avg2)
else:
    print(avg3)

