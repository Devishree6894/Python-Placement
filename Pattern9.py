# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 14:01:49 2024

@author: user
"""

n=int(input())
k=1
for i in range(0,n):
    for j in range(0,n):
        print(k,end=" ")
        k=k+1
    print("\n")