# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:37:53 2020

@author: User
"""

import re # import regular expressions for the appropriate access to the libraries
import random # import random to pick a random answer for Jordan from the libraries
from Jordan_Libraries import library_smalltalk, library_caring, library_cursing, library_corona, library_meditating # import libraries
import Jordan_Class

class test(unittest.TestCase):
    
    def test_smalltalk_Jordan(self): # unittest 1
        j = jordan()
        j.smalltalk_Jordan()
        self.asserAlmostEqual(
            j.smalltalk_Jordan.tolist()
            )
    def test_meditating_Jordan(self):
        j = jordan()
        

if __name__ == '__main__':
    unittest.main()
    
    
# basically you see if it runs a little line of your code rightly, and then run it with example

# change one little thing -> might fuck everything up

# basically you should do something like if jordan smalltalk when you write Hi, Jordan should answer HI