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
print("-------------------------------")
num1=11
flag=True
for factor in range(2,num1):
    if num1 % factor != 0:
        continue
    print("Not prime")
    flag = False
    break
if flag:
    print("prime")
print("-------------------------------")
for factor in range(2,num1):
    if num1 % factor != 0:
        continue
    print("Not prime")
    break
else:
    print("Prime")
    
print("-------------------------------")
s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
t = 11
i = 0
while i < len(s):
    e = s[i]
    if e == t:
        print("done by while")
        break
    i += 1
else:
    print("Not done while")

for e in s:
    if e == t:
        print('For found it')
        break
else:
    print("For didn't find it")
    
