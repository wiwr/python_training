'''
Created on Feb 29, 2024

@author: witek
'''
for year in 2000,2001,2002.2003,2004:
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
    
year=""
while year != 0:
    year = input("Enter year or type 0\n")
    year = int(year)
    if year != 0:
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