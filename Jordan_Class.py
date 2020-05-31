# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:15:13 2020

@author: Marla Dressel
"""

# ====================================================================== #
#                                                                        #
# This file contains the class of Jordan. It entails the functions that  #
# enable Jordan to chat with you about different topics. This class      #
# must be imported to activate Jordan.                                   #
#                                                                        #
# ====================================================================== #


import re 
import random 
# import conversational content
from Jordan_Library import dict_smalltalk, dict_caring, dict_cursing, dict_meditating, dict_corona  


class JordanBot:
    """
    A class that represents the abilities of Jordan the chatbot.
    With this class it is possible to choose a topic and chat with
    Jordan about this topic.
    ...
    
    Attributes
    ----------
    name : str
        user can insert name, which will later be shown in the chat.
 
    Methods 
    ----------
    chat()
        initiates chatbot: lets user pick a topic, gives instructions,
        initiates chat about the specific topic. 
    """  
    
    def __init__(self, name): # this function is always called when a new object of the class is called
        """
        Constructer for Jordan. Takes the user's name as an argument. 
        
        """               
        self.name = name    
        
    def chat(self): 
        """
        A function that enables chatting with Jordan after picking a topic.
        Takes no arguments.
        
        """               
        topics = [dict_smalltalk, dict_caring, dict_cursing, dict_meditating, dict_corona]
                
        while True:
            print("Welcome. My name is Jordan. You can now choose a topic that "
                   "we can talk about. \n Press '0' to have some good "
                   "old-fashioned smalltalk. \n Press '1' to tell me about your "
                   "deepest sorrows and your destroyed soul. \n Press '2' to "
                   "curse with me. \n Press '3' to meditate with me. \n "
                   "Press '4' to talk about Corona." )
            
            choice = input(">>> ") # initialize user input
            
            # link key presses to topic choice
            if choice == '0': 
                print("Alrighty, let's do some chitchatting.\n Don't forget "
                      "that I am sensitive to punctuation. \n _______________"
                      "_________________________________________ \n Hi there!")
            elif choice == '1':
                print("Please tell me about your deepest sorrows and your "
                      "destroyed soul. \n Don't forget that I am sensitive to "
                      "punctuation.\n _______________________________________"
                      "________________ \n Hey there!")
            elif choice == '2':
                print("Make yourself ready. let's insult each other! \n Don't " 
                      "forget that I am sensitive to punctuation.\n _________"
                      "_______________________________________________ \n Hey "
                      "idiot!")
            elif choice == '3':
                print("Ok then, let's meditate.\n Don't forget that I am "
                      "sensitive to punctuation.\n _________________________"
                      "_______________________________ \n Hello!")
            elif choice == '4':
                print("Let's talk about Corona. \n Don't forget that I am "
                      "sensitive to punctuation. \n ________________________"
                      "________________________________ \n Hi!")
            elif choice == 'q': # if user wants to quit
                break
            else: # if user presses the wrong key.
                print("Try again.")
                           
            edition = topics[int(choice)] # placeholder for chosen dictionairy
            
            # I am using a function (taken from: eliza.py) that implements
            # regular expressions and a lambda function to access the right
            # position in the corresponding dictionairy. For this, I use map()
            # in order to apply a function (lambda) to all elements of a list,
            # in this case, a dictionairy, without being case-sensitive. 
            # re-compile() makes sure that the elements can be matched later 
            # to another item in the library. 
            # x[0] : position of the user input keywords
            statement = list(map(lambda x:re.compile(x[0], re.IGNORECASE), edition)) 
            
            # x[1] : position of output sentences
            answer = list(map(lambda x:x[1], edition))
            
            
            failed_response = "I did not understand what you said. Also, I am "
            "sensitive to punctuation."
            while True:
                
                # initialize user input + name of user
                userInput = input(' ' + self.name + ' >>> ') 
                resp =  failed_response # initalize response variable
                counter = 0  # initalize counter
                
                # determine when to loop
                while resp == failed_response and counter < len(statement):              
                    for i in range(0, len(statement)): 
                        
                        # find input in dictionairy
                        match = statement[i].match(userInput) 
                        if match == False:
                            resp = failed_response
                        if match:
                            # if match, pick random answer from dictionairy
                            # and substitute regex for input word
                            word = statement[i].split(userInput)[1]  
                            resp = random.choice(answer[i]) 
                        counter += 1 

                if userInput == 'q':
                    print(random.choice(answer[i]))
                    print("--------------------------------- \n "
                          "Do you want to choose another topic? "
                          "Pick below or press 'q' to quit for realsies. \n "
                          "--------------------------------- ")
                    break
                
                # print Jordan's response and in case a regex ({}) was used
                # print substituted word additionally
                resp = resp.format(word)
                print(" ____________ \n "
                      "Jordan >>> " + resp) # print Jordan's answer
                