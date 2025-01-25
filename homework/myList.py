"""
 Homework 4: lists
"""

import sys
import os

myUniqueList = []
myLeftovers = []

def addItem(new_value):
    if new_value in myUniqueList:
        myLeftovers.append(new_value)
        return False
    else:
        myUniqueList.append(new_value)
        return True

if __name__ == "__main__":
    a = 3
    print(addItem(a))

    b = 3
    print(addItem(b))

    c = 4
    print(addItem(c))

    print("My unique list: ", myUniqueList)
    print("My leftovers list: ", myLeftovers)

        