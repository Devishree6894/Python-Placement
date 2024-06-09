# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:08:40 2024

@author: user
"""

n=int(input("Enter the number"))
sum=0
fib1=0
fib2=1

print("Fibonacci series:",n,"is")
print(fib1,fib2,end=" ")
for i in range(2,n):
    fib3=fib1+fib2
    print(fib3,end=" ")
    fib1=fib2
    fib2=fib3
