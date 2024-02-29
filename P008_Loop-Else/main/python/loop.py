'''
Created on Feb 29, 2024

@author: witek
'''
num1=29
for index in range(2,num1):
    if num1 % index !=0:
        continue
    print(num1, "is not a prime number")
    break
else:
    print(num1, "is a prime number")