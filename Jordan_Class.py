# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:15:13 2020

@author: User
"""
# importing regular expression operations, which we need later to access the libraries

import re 
import random # later we want to pick a chatbot answer to a statement by random
from Jordan_Library import dict_smalltalk, dict_caring, dict_cursing, dict_meditating, dict_corona  # import libraries
# and here we imported all the topic libraries      
      
class JordanBot:
    """
    A class that represents the abilities of Jordan the chatbot.
    ...
    
    Attributes
    ----------
    name : str
        user can insert name, which will later be shown in the chat.
 
    Methods 
    ----------
    name : str
        user can insert name, which will later be shown in the chat.
        
    """
    
    
    def __init__(self, name): # this function is always called when a new object of the class is called
        """
        Constructing topics for Jordan. Takes the user's name as an argument. 
        
        """        
        
        self.name = name
        
        
    def chat(self): 
        """
        A function that enables chatting with Jordan after picking a topic.
        Take no arguments.
        
        """       
        
        topics = [dict_smalltalk, dict_caring, dict_cursing, dict_meditating, dict_corona]
                
        while True:
            print("Welcome. My name is Jordan. You can now choose a topic that we can talk about.")
            print("Press '0' to have some good old-fashioned smalltalk.")
            print("Press '1' to tell me about your deepest sorrows and your destroyed soul.")
            print("Press '2' to curse with me.")
            print("Press '3' to meditate with me.")
            print("Press '4' to talk about Corona.")
            # execute this welcome text and tell user what to press in order to pick a topic.
            
            choice = input(">>> ")
            # initialize input
            
            if choice == '0': # determine which key to press to initiate the specific topic
                print("Alrighty, let's do some chitchatting.")# initiate welcome text for specific topic
                print("Don't forget that I am sensitive to punctuation.")
            elif choice == '1':
                print("Please tell me about your deepest sorrows and your destroyed soul.")
                print("Don't forget that I am sensitive to punctuation.")  
            elif choice == '2':
                print("Make yourself ready. let's insult each other!")
                print("Don't forget that I am sensitive to punctuation.")
            elif choice == '3':
                print("Ok then, let's meditate.")
                print("Don't forget that I am sensitive to punctuation..")
            elif choice == '4':
                print("Let's talk about Corona.")
                print("Don't forget that I am sensitive to punctuation..")
            elif choice == 'q': # if user wants to quit
                break
            else: # if user pressed the wrong key.
                print("Try again.")
            
            edition = topics[int(choice)]
            statement = list(map(lambda x:re.compile(x[0], re.IGNORECASE), edition)) 
            # list(map()) applies a function to all elements of a specified object, in this case the cursing library
            # lambda makes sure that re.compile is applied in a certain way to all elements of the library without being case-sensitive
            # re.compile makes sure that the elemets are turned into objects that can be matched later to another item in the library    
            answer = list(map(lambda x:x[1], edition))
            # same here, but here we pick the second argument in the list x[1], which entails Jordan's answers
            
        
            while True:
                userInput = input(' ' + self.name + ' >>> ') # this allows for the user to type in keys
                resp = "I did not understand what you said. Also, I am sensitive to punctuation." # initalize response variable
                counter = 0  # initalize counter
                while resp == "I did not understand what you said. Also, I am sensitive to punctuation." and counter < len(statement): # determine when to start my loop
                    for i in range(0, len(statement)): # loop through the indexed library
                        match = statement[i].match(userInput) # look if input of the user matches with one of the words in the library
                        if match:
                            word = statement[i].split(userInput)[1]  # We have to take the first element of this list
                            resp = random.choice(answer[i]) # if there is a match, pick a random answer from x[1]
                        counter += 1 # make sure that the counter is now + 1 so it does not write the initialized response from the beginning but continues with the loop
                                     # if there is no match though, then it will write the initialized answer
                if userInput == 'q':
                    print(random.choice(answer[i]))
                    print("---------------------------------")
                    print("Do you want to choose another topic? Pick below or press 'q' to quit for realsies.")
                    print("---------------------------------")
                    break
                resp = resp.format(word)
                print('____________')
                print('                                                    ')
                print('Jordan >>> ' + resp) # print Jordan's answer
                


        
    
            