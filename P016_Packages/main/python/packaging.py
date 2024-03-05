'''
Created on Mar 5, 2024

@author: witek
'''
import math as m
import sys

print("Square root of 16:", m.sqrt(16))
print("Square root of 25:", m.sqrt(25))
print("Value of pi:", m.pi)
print("Square root of 36:", m.sqrt(36))
print("Value of pi:", m.pi)

class MyClass:
    def __init__(self):
        self.name = "John"
        self.age = 30
    def greet(self):
        print("Hello, I'm",self.name)
        
obj = MyClass()

print("Attributes and methods of obj:", dir(obj))

print("List of directories in sys.path:")
for directory in sys.path:
    print(directory)