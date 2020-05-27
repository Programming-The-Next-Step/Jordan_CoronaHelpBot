# -*- coding: utf-8 -*-
"""
Created on Tue May 26 12:18:17 2020

@author: User
"""
import re # import regular expressions for the appropriate access to the libraries
import random # import random to pick a random answer for Jordan from the libraries
from Jordan_Libraries import library_cursing # import libraries



def testing_Jordan(): 
    keys_cursing = list(map(lambda x:re.compile(x[0], re.IGNORECASE), library_cursing)) 
    # list(map()) applies a function to all elements of a specified object, in this case the small-talk library
    # lambda makes sure that re.compile is applied in a certain way to all elements of the library without being case-sensitive
    # re.compile makes sure that the elemets are turned into objects that can be matched later to another item in the library    
    values_cursing = list(map(lambda x:x[1],library_cursing))
    # same here, but here we pick the second argument in the list x[1], which entails Jordan's answers
    
    
    while True:
        userInput = input(">>> ") # this allows for the user to type in keys
        resp = "I did not understand what you said. Also, I am sensitive to punctuation." # initalize response variable
        counter = 0  # initalize counter
        while resp == "I did not understand what you said. Also, I am sensitive to punctuation." and counter < len(keys_cursing): # determine when to start my loop
            for i in range(0, len(keys_cursing)): # loop through the indexed library
                match = keys_cursing[i].match(userInput) # look if input of the user matches with one of the words in the library
                if match:
                    word = keys_cursing[i].split(userInput)[1]  # We have to take the first element of this list
                    resp = random.choice(values_cursing[i]) # if there is a match, pick a random answer from x[1]
                counter += 1 # make sure that the counter is now + 1 so it does not write the initialized response from the beginning but continues with the loop
                             # if there is no match though, then it will write the initialized answer
        
        if userInput == 'q':
            print(random.choice(values_cursing[i]))
            print("---------------------------------")
            print("Do you want to choose another topic? Pick below or press 'q' to quit for realsies.")
            print("---------------------------------")
            break
        resp = resp.format(word)
        print(resp) # print Jordan's answer

while True:
    print("Welcome. My name is Jordan. You can now choose a topic that we can talk about.")
    print("Press '1' to have some good old-fashioned smalltalk.")
    print("Press '2' to tell me about your deepest sorrows and your destroyed soul.")
    print("Press '3' to curse with me.")
    print("Press '4' to talk about Corona.")
    # execute this welcome text and tell user what to press in order to pick a topic.
    
    choice = input(">>> ")
    # initialize input
    
    
    if choice == '3' : # determine which key to press to initiate the specific topic
        print("Alrighty, let's insult each other.") # introduction text for specific topic
        print("Don't forget that I am sensitive to punctuation.")
        testing_Jordan() # initiate method
    elif choice == 'q': # if user wants to quit
        print("Goodbye then.")
        break
    else: # if user pressed the wrong key.
        print("Try again.")
        