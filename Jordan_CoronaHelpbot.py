# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:15:13 2020

@author: User
"""
import re # importing regular expression operations, which we need later to access the libraries
import random # later we want to pick a chatbot answer to a statement by random
from libraries import library_smalltalk, library_caring, library_cursing, library_corona
# and here we imported all the topic libraries
      
      
class Jordan:
    """
    A class containing Jordans skills.
    
    ...
    
    Attributes 
    ----------)
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
    
    def smalltalk_Jordan(self):
        """
        
        A function for chitchatting with Jordan.
        
        """
        while True:
            # I think it would be nice (but not necessary) to have something like while user_wants_to_quit == False:
            userInput = input(">>> ")
            resp = "I did not understand what you said" # initalize this
            counter = 0  # initalize this
            while resp == "I did not understand what you said" and counter < len(Jordan.keys_smalltalk):
                for i in range(0, len(Jordan.keys_smalltalk)):
                    match = Jordan.keys_smalltalk[i].match(userInput)
                    if match:
                        resp = random.choice(Jordan.values_smalltalk[i])
                    counter += 1
                        
            print(resp)
                
    def caring_Jordan(self):
        """
        
        A function to talk with Jordan about your deepest sorrows
        and your destroyed soul.
        
        """
        
        while True:
            userInput = input(">>>")
            resp = "I did not understand what you said" # initalize this
            counter = 0  # initalize this
            while resp == "I did not understand what you said" and counter < len(Jordan.keys_caring):
                for i in range(0, len(Jordan.keys_caring)):
                    match = Jordan.keys_caringg[i].match(userInput)
                    if match:
                        resp = random.choice(Jordan.values_caring[i])
                    counter += 1
                        
            print(resp)
            
    def cursing_Jordan(self):
        """
        
        A function to insult Jordan and get insults back.
        
        """
        while True:
            userInput = input(">>> ")
            resp = "I did not understand what you said" # initalize this
            counter = 0  # initalize this
            while resp == "I did not understand what you said" and counter < len(Jordan.keys_cursing):
                for i in range(0, len(Jordan.keys_cursing)):
                    match = Jordan.keys_cursing[i].match(userInput)
                    if match:
                        resp = random.choice(Jordan.values_cursing[i])
                    counter += 1
                        
            print(resp)
                
    def corona_Jordan(self):

        """
        
        A function to talk with Jordan about the corona-crisis
        and potentially get some suggestions on how to stay sane.
        
        """
        while True:
            userInput = input(">>> ")
            resp = "I did not understand what you said" # initalize this
            counter = 0  # initalize this
            while resp == "I did not understand what you said" and counter < len(Jordan.keys_corona):
                for i in range(0, len(Jordan.keys_corona)):
                    match = Jordan.keys_corona[i].match(userInput)
                    if match:
                        resp = random.choice(Jordan.values_corona[i])
                    counter += 1
                        
            print(resp)

Jordan.caring_Jordan('')