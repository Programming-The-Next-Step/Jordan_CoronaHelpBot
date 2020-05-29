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
    meditating_Jordan(userInput)
        function that initiates cursing with Jordan
    caring_Jordan(userInput)
        function that initiates a talk with Jordan about your sorrows
    corona_Jordan(userInput)    
        function that initiates a talk with Jordan about corona
    """
    
    def __init__(self): # this function is always called when a new object of the class is called
        """
        Constructing topics for Jordan. Takes no arguments.
        
        """
        self.library_keys = str('library' + self.i)
        self.library_values = str('library' + self.i)
        
        self.keys = list(map(lambda x:re.compile(x[0], re.IGNORECASE), self.library_keys)) 
            # list(map()) applies a function to all elements of a specified object, in this case the small-talk library
            # lambda makes sure that re.compile is applied in a certain way to all elements of the library without being case-sensitive
            # re.compile makes sure that the elemets are turned into objects that can be matched later to another item in the library
        self.values = list(map(lambda x:x[1],self.library_values))
            # same here, but here we pick the second argument in the list x[1], which entails Jordan's answers
        
    def chooseTopic(self):             
        
            while True:
                userInput = input(">>> ") # this allows for the user to type in keys
                resp = "I did not understand what you said. Also, I am sensitive to punctuation." # initalize response variable
                counter = 0  # initalize counter
                while resp == "I did not understand what you said. Also, I am sensitive to punctuation." and counter < len(self.keys): # determine when to start my loop
                    for i in range(0, len(self.keys)): # loop through the indexed library
                        match = self.keys[i].match(userInput) # look if input of the user matches with one of the words in the library
                        if match:
                            word = self.keys[i].split(userInput)[1]  # We have to take the first element of this list
                            resp = random.choice(self.values)[i] # if there is a match, pick a random answer from x[1]
                        counter += 1 # make sure that the counter is now + 1 so it does not write the initialized response from the beginning but continues with the loop
                                     # if there is no match though, then it will write the initialized answer
                
                if userInput == 'q':
                    print(random.choice(self.values[i]))
                    print("---------------------------------")
                    print("Do you want to choose another topic? Pick below or press 'q' to quit for realsies.")
                    print("---------------------------------")
                    break
                resp = resp.format(word)
                print(resp) # print Jordan's answer
            

# playsound("C:/Users/User/Downloads/Meditation.mp3")


class execute_Jordan():
    """
    A class that lets you execute Jordan.'
    ...
    
    Attributes 
    ----------)
    keys_smalltalk : list

    Methods 
    ----------
    execute
    """
        
    def execute(self, Jordan, chooseJordan):
        """
        
        A method to execute Jordan.
        
        """
        j = Jordan()
        topics = ['smalltalk', 'caring', 'cursing', 'meditating', 'corona']
        i = []
        while True:
            print("Welcome. My name is Jordan. You can now choose a topic that we can talk about.")
            print("Press '1' to have some good old-fashioned smalltalk.")
            print("Press '2' to tell me about your deepest sorrows and your destroyed soul.")
            print("Press '3' to curse with me.")
            print("Press '4' to talk about Corona.")
            print("Press '5' for a quick meditation.")
            print("Press 'q' to quit.")
            # execute this welcome text and tell user what to press in order to pick a topic.
            
            choice = input(">>> ") # initialize input
            
            if choice == '1': # determine which key to press to initiate the specific topic
                i = topics[0]
                print("Alrighty, let's do some chitchatting.")# initiate welcome text for specific topic
                print("Don't forget that I am sensitive to punctuation.")
                j.chooseJordan() # initiate method
            if choice == '2':
                i = topics[1]
                print("Please tell me about your deepest sorrows and your destroyed soul.")
                print("Don't forget that I am sensitive to punctuation.")
                j.chooseJordan()   
            if choice == '3':
                i = topics[2]
                print("Make yourself ready. let's insult each other!")
                print("Don't forget that I am sensitive to punctuation.")
                j.chooseJordan()
            if choice == '4':
                i = topics[3]
                print("Ok then, let's talk about Corona.")
                print("Don't forget that I am sensitive to punctuation..")
                j.chooseJordan()
            if choice == '5':
                i = topics[4]
                print("I will be your guide in this meditation.")
                print("Don't forget that I am sensitive to punctuation..")
                j.chooseJordan()
            if choice == 'q': # if user wants to quit
                break
            else: # if user pressed the wrong key.
                print("Try again.")
                