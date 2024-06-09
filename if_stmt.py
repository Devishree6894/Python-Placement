# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:36:27 2024

@author: user
"""

#Read the marks of a student. If marks > 80 then distinction;
# btw 60 and 80 is pass; less than 60 is fail; otherwise invlaid

marks=int(input("Enter the marks \n"))

if marks >= 80 and marks<=100:
    print("Distinction")
elif marks>=60 and marks<80:
    print("Pass")
elif marks<60:
    print("Fail")
else:
    print("Invalid")
    