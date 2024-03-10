'''
Created on Feb 29, 2024

@author: witek
'''
string1 = input("Provide name of first person\n")
string2 = input("Provide name of second person\n")
if string1 == string2:
    print("Strings are equal")
else:
    print("Strings are not equal")
    
num1 = int(input("Provide first number\n"))
num2 = int(input("Provide second number\n"))

if num1 < num2:
    print(num1, end=" ")
    print("is less than", num2)
elif num1 > num2:
    print(num1, end=" ")
    print("is greater than", num2)
elif num1 == num2:
    print(num1, end=" ")
    print("is equal to", num2)
else:
    print("Provided wrong values")
    
#condition = False
for condition in [True, False]:
    if condition:
        x, y =1, 0
    else:
        x, y = None, None
    print(x, y)    
    x, y = (1, 0) if condition else (None, None) 
    print(x, y)