# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:15:13 2020

@author: User
"""
import re # importing regular expression operations, which we need later to access the libraries
import random # later we want to pick a chatbot answer to a statement by random
from libraries import library_smalltalk, library_cursing, library_caring, library_corona
# and here we imported all the topic libraries

class Jordan:
    """
    A class containing Jordans skills.
    
    ...
    
    Attributes 
    ----------
    keys_smalltalk : list
        Nested lists with strings
    keys_cursing : list
        Nested lists with strings
    keys_caring : list
        Nested lists with strings
    keys_corona : list
        Nested lists with strings
    
    Methods (Functions)
    ----------
    smalltalk_Jordan(userInput)
        function that initiates small-talk with Jordan
    cursing_Jordan(userInput)
        function that initiates cursing with Jordan
    caring_Jordan(userInput)
        function that initiates a talk with Jordan about your sorrows
    corona_Jordan(userInput)    
        function that initiates a talk with Jordan about corona
    """
    
    def __init__(self):
        """
        This function is to determine attributes, 
        which can be applied in Jordan's topic functions.
        
        """
        
        self.keys_smalltalk = list(map(lambda x:re.compile(x[0], re.IGNORECASE), library_smalltalk)) 
        # list(map()) applies a function to all elements of a specified object, in this case the small-talk library
        # lambda makes sure that re.compile is applied in a certain way to all elements of the library without being case-sensitive
        # re.compile makes sure that the elemets are turned into objects that can be matched later to another item in the library
        self.values_smalltalk = list(map(lambda x:x[1],library_smalltalk))
        self.keys_caring = list(map(lambda x:re.compile(x[0], re.IGNORECASE), library_caring))
        self.values_caring = list(map(lambda x:x[1],library_caring))
        self.keys_cursing = list(map(lambda x:re.compile(x[0], re.IGNORECASE), library_cursing))
        self.values_cursing = list(map(lambda x:x[1],library_cursing))
        self.keys_corona = list(map(lambda x:re.compile(x[0], re.IGNORECASE), library_corona))
        self.values_corona = list(map(lambda x:x[1],library_corona))
    
    def smalltalk_Jordan(self, userInput = ''):
        """
        
        A function to engage in small-talk with Jordan.
        
        """
        
        while True:
            print("I am Jordan. Let's do some small-talk.")
            userInput = input("You >>> ")
            for i in range(0, len(Jordan.keys_smalltalk)):
                match = Jordan.keys_smalltalk[i].match(userInput)
                if match:
                    resp = random.choice(Jordan.values_smalltalk[i])
                    print(resp)
                else:
                    print("I did not understand what you said")
                    break
                
    def caring_Jordan(self, userInput = ''):
        """
        
        A function to talk with Jordan about your 
        deepest sorrows and your destroyed soul.
        
        """
        while True:
            print("I am Jordan. Let's talk about your deepest sorrows and your destroyed soul.")
            userInput = input("You >>> ")
            for i in range(0, len(Jordan.keys_caring)):
                match = Jordan.keys_caring[i].match(userInput)
                if match:
                    resp = random.choice(Jordan.values_caring[i])
                    print(resp)
                else:
                    print("I did not understand what you said")
                    break

    def cursing_Jordan(self, userInput = ''):
        """
        
        A function to curse with Jordan, because - let's be honest -
        this is what we want chatbots to do really.
        
        """
        while True:
            print("I am Jordan. Let's insult each other.")
            userInput = input("You >>> ")
            for i in range(0, len(Jordan.keys_cursing)):
                match = Jordan.keys_cursing[i].match(userInput)
                if match:
                    resp = random.choice(Jordan.values_cursing[i])
                    print(resp)
                else:
                    print("I did not understand what you said")
                    break
                
    def corona_Jordan(self, userInput = ''):
        """
        
        A function to talk with Jordan about the corona-crisis
        and potentially get some suggestions on how to stay sane.
        
        """
        
        while True:
            print("I am Jordan. Let's talk about corona and your mental health.")
            userInput = input("You >>> ")
            for i in range(0, len(Jordan.keys_corona)):
                match = Jordan.keys_corona[i].match(userInput)
                if match:
                    resp = random.choice(Jordan.values_corona[i])
                    print(resp)
                else:
                    print("I did not understand what you said")
                    break