'''
Created on Mar 4, 2024

@author: witek
'''
my_list = [1,2,3]
try:
    print(my_list[5])
except IndexError as e:
    print("IndexError occurred:",e)
    
my_dict = {'a':1,'b':2}
try:
    print(my_dict['c'])
except KeyError as e:
    print("KeyError occurred:",e)
    
try:
    x = 10 + "5"
except TypeError as e:
    print("TypeError occurred",e)
    
try:
    num = int("hello")
except ValueError as e:
    print("ValueError occurred:",e)
    
try:
    my_list =[1,2,3]
    print(my_list[4])
except LookupError as e:
    print("LookupError occurred:",e)
    
try:
    while True:
        user_input = input("Enter something: ")
        print("You entered:", user_input)
except KeyboardInterrupt:
    print("\nProgram interrupted by the user.Exiting gracefully.")
    
import sys
try:
    sys.exit("Exiting the program")
except SystemExit as e:
    print("SystemExit occurred:",e)