# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:15:13 2020

@author: User
"""
import re # importing regular expression operations, which we need later to access the libraries
import random # later we want to pick a chatbot answer to a statement by random
from Jordan_Libraries import library_smalltalk, library_caring, library_cursing, library_corona, library_meditating
# and here we imported all the topic libraries      
      
class Jordan:
    """
    A class that enables different topics to chat about with Jordan.
    It's recommended to not set any different properties.'
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
    keys_meditating : list
        Nested lists with strings
    values_smalltalk : list
        Nested lists with strings
    values_cursing : list
        Nested lists with strings
    values_caring : list
        Nested lists with strings
    values_corona : list
        Nested lists with strings
    values_meditating : list
        Nested lists with strings  
    Methods 
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
    
    def __init__(self): # this function is always called when a new object of the class is called
        """
        Constructs the Jordan class. Takes no arguments.
        
        """
        
        self.keys_smalltalk = list(map(lambda x:re.compile(x[0], re.IGNORECASE), library_smalltalk)) 
            # list(map()) applies a function to all elements of a specified object, in this case the small-talk library
            # lambda makes sure that re.compile is applied in a certain way to all elements of the library without being case-sensitive
            # re.compile makes sure that the elemets are turned into objects that can be matched later to another item in the library
        self.values_smalltalk = list(map(lambda x:x[1],library_smalltalk))
            # same here, but here we pick the second argument in the list x[1], which entails Jordan's answers
        self.keys_caring = list(map(lambda x:re.compile(x[0], re.IGNORECASE), library_caring))
        self.values_caring = list(map(lambda x:x[1],library_caring))
        self.keys_cursing = list(map(lambda x:re.compile(x[0], re.IGNORECASE), library_cursing))
        self.values_cursing = list(map(lambda x:x[1],library_cursing))
        self.keys_corona = list(map(lambda x:re.compile(x[0], re.IGNORECASE), library_corona))
        self.values_corona = list(map(lambda x:x[1],library_corona))
        self.keys_meditating = list(map(lambda x:re.compile(x[0], re.IGNORECASE), library_meditating))
        self.values_meditating = list(map(lambda x:x[1],library_meditating))
        
    def smalltalk_Jordan(self):
        """
        
        A function for chitchatting with Jordan.
        
        """
        while True:
            userInput = input(">>> ") # allows for user to type in something
            resp = "I did not understand what you said. Also, I am sensitive to punctuation." # initalize response string in case Jordan does not recognize the words
            counter = 0  # initialize counter 
            while resp == "I did not understand what you said. Also, I am sensitive to punctuation." and counter < len(self.keys_smalltalk):
                for i in range(0, len(self.keys_smalltalk)):  # loop through the indexed library
                    match = self.keys_smalltalk[i].match(userInput) # look if input of the user matches with one of the words in the library
                    if match: 
                        word = self.keys_smalltalk[i].split(userInput)[1]  # We have to take the first element of this list                        
                        resp = random.choice(self.values_smalltalk[i]) # if there is a match, pick a random answer from x[1]
                    counter += 1 # make sure that the counter is now + 1 so it does not write the initialized response from the beginning but continues with the loop.
                                 # if there is no match though, then it will write the initialized answer
            if userInput == 'q':
                print(random.choice(self.values_smalltalk[i]))
                print("---------------------------------")
                print("Do you want to choose another topic? Pick below or press 'q' to quit for realsies.")
                print("---------------------------------")
                break                                
            resp = resp.format(word) # replace if applicable      
            print(resp) # print response
                
    def caring_Jordan(self):
        """
        
        A function to talk with Jordan about your deepest sorrows
        and your destroyed soul.
        
        """
        
        while True:
            userInput = input(">>>")
            resp = "I did not understand what you said. Also, I am sensitive to punctuation." # initalize this
            counter = 0  # initalize this
            while resp == "I did not understand what you said. Also, I am sensitive to punctuation." and counter < len(self.keys_caring):
                for i in range(0, len(self.keys_caring)):
                    match = self.keys_caring[i].match(userInput)
                    if match:
                        word = self.keys_caring[i].split(userInput)[1]  # We have to take the first element of this list
                        resp = random.choice(self.values_caring[i])
                    counter += 1
            if userInput == 'q':
                print(random.choice(self.values_caring[i]))
                print("---------------------------------")
                print("Do you want to choose another topic? Pick below or press 'q' to quit for realsies.")
                print("---------------------------------")
                break
            resp = resp.format(word) # replace if applicable                   
            print(resp)
            
    def cursing_Jordan(self):
        """
        
        A function to insult Jordan and get insults back.
        
        """
        while True:
            userInput = input(">>> ")
            resp = "I did not understand what you said. Also, I am sensitive to punctuation." # initalize this
            counter = 0  # initalize this
            while resp == "I did not understand what you said. Also, I am sensitive to punctuation." and counter < len(self.keys_cursing):
                for i in range(0, len(self.keys_cursing)):
                    match = self.keys_cursing[i].match(userInput)
                    if match:
                        word = self.keys_caring[i].split(userInput)[1]  # We have to take the first element of this list                        
                        resp = random.choice(self.values_cursing[i])
                    counter += 1
            if userInput == 'q':
                print(random.choice(self.values_cursing[i]))
                print("---------------------------------")
                print("Do you want to choose another topic? Pick below or press 'q' to quit for realsies.")
                print("---------------------------------")
                break                   
            resp = resp.format(word) # replace if applicable                     
            print(resp)
                
    def corona_Jordan(self):

        """
        
        A function to talk with Jordan about the corona-crisis
        and potentially get some suggestions on how to stay sane.
        
        """
        while True:
            userInput = input(">>> ")
            resp = "I did not understand what you said. Also, I am sensitive to punctuation." # initalize this
            counter = 0  # initalize this
            while resp == "I did not understand what you said. Also, I am sensitive to punctuation." and counter < len(self.keys_corona):
                for i in range(0, len(self.keys_corona)):
                    match = self.keys_corona[i].match(userInput)
                    if match:
                        word = self.keys_caring[i].split(userInput)[1]  # We have to take the first element of this list                        
                        resp = random.choice(self.values_corona[i])
                    counter += 1
            if userInput == 'q':
                print(random.choice(self.values_corona[i]))
                print("---------------------------------")
                print("Do you want to choose another topic? Pick below or press 'q' to quit for realsies.")
                print("---------------------------------")
                break
            resp = resp.format(word) # replace if applicable            
            print(resp)

    def meditating_Jordan(self):

        """
        
        A function to meditate with Jordan as your guide.
        
        """
        while True:
            userInput = input(">>> ")
            resp = "I did not understand what you said. Also, I am sensitive to punctuation." # initalize this
            counter = 0  # initalize this
            while resp == "I did not understand what you said. Also, I am sensitive to punctuation." and counter < len(self.keys_meditating):
                for i in range(0, len(self.keys_meditating)):
                    match = self.keys_meditating[i].match(userInput)
                    if match:
                        word = self.keys_caring[i].split(userInput)[1]  # We have to take the first element of this list                        
                        resp = random.choice(self.values_meditating[i])
                    counter += 1
            if userInput == 'q':
                print(random.choice(self.values_meditating[i]))
                print("---------------------------------")
                print("Do you want to choose another topic? Pick below or press 'q' to quit for realsies.")
                print("---------------------------------")
                break
            resp = resp.format(word) # replace if applicable
            print(resp)
            

# playsound("C:/Users/User/Downloads/Meditation.mp3")