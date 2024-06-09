# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 14:24:29 2024

@author: user
"""

n=int(input("Enter the number"))
rev=int(str(n)[::-1])

if n==rev:
    print("Palindrome")
else:
    print("Not palindrome")