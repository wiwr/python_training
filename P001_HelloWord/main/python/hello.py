'''
Created on Feb 28, 2024

@author: witek
'''
from main.python.functions import helloName, printMark, printT
 
print("Hello Word\n")
helloName()
printMark()

t = ("apple","banana","orange")
printT(t)

print("apple","banana","orange\n",sep=",")
print("Hello",end=" ")
print("Word")