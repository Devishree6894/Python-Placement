# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 12:18:20 2024

@author: user
"""

n=int(input())

for i in range(0,n):
    for j in range(0,n):
        if(j>=i):
            print("*", end=" ")
            
    print( )