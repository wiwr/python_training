'''
Created on Mar 8, 2024

@author: witek
'''
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "is a Leap year")
                return True
            else:
                print(year, "is not a Leap year")
                return False
        else:
            print(year, "is a Leap year")
            return True
    else:
        print(year, "is not a Leap year")
        return False 


def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number-1)


if __name__ == "__main__":    
    is_leap_year(2001)
    print("The factorial of 5 is",factorial(5))