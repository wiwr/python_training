'''
Created on Feb 28, 2024

@author: witek
'''

import math
import random

full_name = "John Wick"
print("Full name is ", full_name)
num1=50
num2=12
print("Addition: ",num1+num2)
print("Subtraction: ",num1-num2)
print("Multiplication:",num1*num2)
print("Division: ",round(num1/num2,2))
print("Integer division: ", num1//num2)
print("Modulus: ",num1%num2)
print("Exponential",2**4)

first_name = "John"
last_name = "Wick"

print("String Concatenation: ", first_name + last_name)
binary_num1 = 0b1010
binary_num2 = 0b1111
print("And Operation: ",end=" ")
print(bin(binary_num1 & binary_num2))
print("Or Operation: ",end=" ")
print(bin(binary_num1 | binary_num2))

print("num1 and num2 are equal")
print("num1 and num2 are not equal")
print("num1 is less than num2")
print("num1 is less than or equal to num2")
print("num1 is greater than num2")
print("num1 is greater than or equal to num2")

print("And Operator: ", True and True)
print("Or Operation: " , True or False)
print("Not Operator: ", not True)

print("--------------")
print("123 + 222 = ", 123 + 222)
print("1.5 * 4 = ", 1.5 * 4)
print("2 ** 100 = ", 2 ** 100)
print("Length of  10 000 is ",len(str(2 ** 10000)))
print("3.1415 * 2 = ", 3.1415 * 2)

print("pi = ", math.pi)
print("sqrt = ", math.sqrt(85))

print("Random value: ",random.random())
print("Random from list: ", random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]))