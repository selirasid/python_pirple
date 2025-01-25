"""
Homework 2: Functions 
"""
import sys
import os

sys.path.append('/Users/selghiulrasid/Documents/Proiecte_Python_pirple/python_pirple')

from main import Song, Artist, Released_year

def getSongName():
    print(Song)

def getArtistName():
    print("Artist name: " + Artist)

def getYear():
    return Released_year
    
name = getSongName()
artist = getArtistName()
year = getYear()
print("The released year is: ", year)

