'''
Created on Mar 8, 2024

@author: witek
'''
from main.python import function

def test_factorial():
    assert function.factorial(5) == 120
    
def test_is_leap_year():
    assert function.is_leap_year(2002) is False