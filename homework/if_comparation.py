"""
 Homework 3: if statements
"""

import os
import sys

def isEqual(a,b,c):
    if(int(a) == int(b) or int(a) == int(c) or int(b) == int(c)):
        return True
    else:
        return False
    
no1 = input("Please enter the first value: ")
no2 = input("Please enter the second value: ")
no3 = "2"

print(isEqual(no1, no2, no3))