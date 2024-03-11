'''
Created on Mar 11, 2024

@author: witek
'''
from main.python import function
import platform
import pytest
import sys

@pytest.mark.skip(reason = "testing skipping a test")
def test_skipping():
    assert False
    
@pytest.mark.skipif(platform.system() == "Linux", reason = "skipping test for demonstration")
def test_factorial():
    assert function.factorial(5) == 120

@pytest.mark.xfail(reson = "demonstrating failure")
def test_expected_failure():
    assert False
    
@pytest.mark.parametrize("year,result",[
                                        (2000,True),
                                        (2001,False), 
                                        (2024,True),
                                        (2020,True)
                                        ])

def test_is_leap_year(year,result):
    assert function.is_leap_year(year) is result
    
@pytest.mark.skipif(sys.version_info < (3,12),reason="requires python3.12 or higher")
@pytest.mark.parametrize("test_input,expected",
                         [(70, "passed"),
                          (40, "missed"),
                          (80, "passed")])
def test_something(test_input,expected):
    assert function.validate_marks(test_input) == expected