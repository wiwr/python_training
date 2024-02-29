'''
Created on Feb 29, 2024

@author: witek
'''
num1=20
flag=True
for index in range(2,num1):
    if num1 % index != 0:
        continue
    print(num1, "is not a prime number")
    flag = False
    break
if flag:
    print(num1, "is a prime number")