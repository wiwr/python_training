'''
Created on Mar 8, 2024

@author: witek
'''
import unittest
from main.python import function

class Test(unittest.TestCase):
    
    def test_factorial(self):
        self.assertEqual(function.factorial(5),121)
        
    def test_is_leap_year(self):
        self.assertEqual(function.is_leap_year(2002), True)
        
if __name__ == "__main__":
    unittest.main()