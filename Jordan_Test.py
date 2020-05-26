# -*- coding: utf-8 -*-
"""
Created on Tue May 26 12:18:17 2020

@author: User
"""
import re
import random
from libraries import library_cursing



def testing_Jordan():
    # I'm not sure if it is good practice to leave the input empty but the userInput is not necessary as an argument
    keys_cursing = list(map(lambda x:re.compile(x[0], re.IGNORECASE), library_cursing))
    values_cursing = list(map(lambda x:x[1],library_cursing))
    
    while True:
        # I think it would be nice (but not necessary) to have something like while user_wants_to_quit == False:
        userInput = input(">>> ")
        resp = "I did not understand what you said" # initalize this
        counter = 0  # initalize this
        while resp == "I did not understand what you said" and counter < len(keys_cursing):
            for i in range(0, len(keys_cursing)):
                match = keys_cursing[i].match(userInput)
                if match:
                    resp = random.choice(values_cursing[i])
                counter += 1
                    
        print(resp)

while True:
    print("Welcome. My name is Jordan. You can now choose a topic that we can talk about.")
    print("Press '1' to have some good old-fashioned smalltalk.")
    print("Press '2' to tell me about your deepest sorrows and your destroyed soul.")
    print("Press '3' to curse with me.")
    print("Press '4' to talk about Corona.")
    
    choice = input(">>> ")
    
    
    if choice == '3' :
        print("Alrighty, let's insult each other.")
        testing_Jordan()
    else:
        break