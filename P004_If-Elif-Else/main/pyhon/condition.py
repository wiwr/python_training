'''
Created on Feb 29, 2024

@author: witek
'''
marks=int(input("Provide mark\n"))
if marks >= 90 and marks <= 100:
    print("A grade")
elif marks >= 80 and marks < 90:
    print("B grade")
elif marks >= 70 and marks < 80:
    print("C grade")
elif marks >= 60 and marks < 70:
    print("D grade")
elif marks >= 50 and marks < 60:
    print("E grade")
elif marks >= 0 and marks < 30:
    print("F grade")
else:
    print("Mark out of range")