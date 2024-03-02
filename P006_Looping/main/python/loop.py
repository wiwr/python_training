'''
Created on Feb 29, 2024

@author: witek
'''
for year in range(2000,2004):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "is a Leap year")
            else:
                print(year, "is not a Leap year")
        else:
            print(year, "is a Leap year")
    else:
        print(year, "is a Leap year")
else:
    print(year, "is not a Leap year")
    
year=int(input("Enter year or type 0 to exit\n"))
while year != 0:
    if year % 4 ==0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "is a Leap year")
            else:
                print(year, "is not a Leap year")
        else:
            print(year, "is a Leap year")
    else:
        print(year, "is not a Leap year")
    year = int(input("Enter year or type 0 to exit\n"))
    
print()
for value in range(5,3,-1):
    print(value, "is even",(value %2 ==0))
print()
for value in range(5):
    print(value, "is even",(value%2 ==0))
print()
for value in range(1,10):
    print(value, "is even",(value%2==0))