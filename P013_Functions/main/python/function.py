'''
Created on Mar 4, 2024

@author: witek
'''
def test_something(num2):
    global num1
    num1 = num2
    num1 +=100
    return num1

print(test_something(30))
num3= 400
def variable_args(*values):
    global num1
    num1 = 100
    print(num3)
    print(values)
    print(len(values))
    
variable_args(200,400)
print(num1)
print(test_something(30))
variable_args(200,400,600,800)
print(test_something(40))

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year,"is a Leap year")
            else:
                print(year, "is not a Leap year")
        else:
            print(year, "is a Leap year")
    else:
        print(year, "is not a Leap year")
        
def leap_year(*args):
    year_list = list(args)
    for year in year_list:
        if year %4 ==0:
            if year %100 == 0:
                if year % 400 == 0:
                    print(year, "is a Leap year")
                else:
                    print(year, "is not a Leap year")
            else:
                print(year, "is a Leap year")
        else:
            print(year, "is not a Leap year")
            
def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number -1)

is_leap_year(2024)
leap_year(200,2002,2003,2004,2024)
print("The factorial of 5 is",factorial(5))

def function1(arg1,arg2,arg3):
    print(arg1,arg2,arg3)

def function2(arg1=None,arg2=None,arg3=None):
    print(arg1, arg2, arg3)
    
args = [2, 2, 3]
kwargs = {"arg2": 2, "arg1": 1, "arg3":3}

function1(*args)
function2(**kwargs)