'''
Created on Feb 29, 2024

@author: witek
'''
num1=int(input("Provide number\n"))
num2=int(input("Provide value 1 or 0\n"))
for index in range(2,num1-num2):
    if num1 % index !=0:
        continue
    print(num1, "is not a prime number")
    break
else:
    print(num1, "is a prime number")