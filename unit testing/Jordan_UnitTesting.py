# -*- coding: utf-8 -*-
"""
Created on Sun May 31 11:01:24 2020

@author: Marla Dressel
"""
from Jordan_Library import dict_smalltalk
import unittest
from Jordan_Class import JordanBot

class testJordan(unittest.TestCase):
    """
    A class to test several units of Jordan to make sure everything is working correctly.
    """
        
    def test_match(self):
        
        j = JordanBot('StringName')
        j.chat()
        user_input = "What are you?"
        bot_output = list(map(lambda x:x[1], dict_smalltalk)) # this is how I access the right response in the right library
        matched = bot_output.match(user_input)
        self.assertIn("I am a chatbot, dude. What do you think?", matched)
        
    def test_regex(self):
        
        j = JordanBot('StringName')
        j.chat()
        text = 'something'
        regex = {}
        self.assertRegexpMatches(text, regex)

if __name__ == '__main__':
    unittest.main()
    
    
# basically you see if it runs a little line of your code rightly, and then run it with example

# change one little thing -> might fuck everything up

# basically you should do something like if jordan smalltalk when you write Hi, Jordan should answer HI