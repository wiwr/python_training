'''
Created on Mar 11, 2024

@author: witek
'''
def is_leap_year(year):
    if year % 4 ==0:
        if year % 100 ==0:
            if year % 400 ==0:
                print(year,"is a Leap year")
                return True
            else:
                print(year, "is not a leap year")
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


def validate_marks(marks):
    if marks >= 60:
        return "passed"
    return "missed"


if __name__ == "__main__":
    print(validate_marks(50))    
    is_leap_year(2001)
    print("The factorial of 5 is", factorial(5))

