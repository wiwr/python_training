'''
Created on Mar 5, 2024

@author: witek
'''
from math import * 
from random import *

print("ceil(4.3) =", ceil(4.3))
print("floor(4.7) =", floor(4.7))
print("trunc(4.9) =", trunc(4.9))
print("factorial(5) =", factorial(5))
print("hypot(3,4) =", hypot(3,4))
print("sqrt(25) =", sqrt(25))

seed(123)
print("Random number:",random())
colors = ['red','blue','green','yellow']
print("Random choice from colors:",choice(colors))
print("Random sample from colors:",sample(colors,2))
print("Randow choices from colors with replacement:",choices(colors,k=3))