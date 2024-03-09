'''
Created on Mar 9, 2024

@author: witek
'''
def printMark():
    try:
        mark=int(input("Enter marks: "))
        print("Your mark is ", (mark),"\n")
    except ValueError:
        print("Provided mark is wrong.")   
        printMark()


def helloName():
    name=input("Provide your name: ")
    if name.isalpha():
        print("Hello",name.capitalize(),"\n")
    else:
        print("Provided value is wrong.")
        helloName()
        
def printT(t):
    for w in t:
        print(w)