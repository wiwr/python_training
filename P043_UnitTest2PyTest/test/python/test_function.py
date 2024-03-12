'''
Created on Mar 12, 2024

@author: witek
'''
import unittest
from main.python import function

class Test(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(function.factorial(5),120)
        
    
    def test_is_leap_year(self):
        self.assertEqual(function.is_leap_year(2002),False)
        
        
if __name__ == "__main__":
    unittest.main()