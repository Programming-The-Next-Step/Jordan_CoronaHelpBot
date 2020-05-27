# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:30:07 2020

@author: User
"""
import Jordan_Class # import methods of the Jordan class

j = Jordan_Class()

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
        print("Alrighty, let's do some chitchatting.")# initiate welcome text for specific topic
        print("Don't forget that I am sensitive to punctuation.")
        j.smalltalk_Jordan() # initiate method
    if choice == '2':
        print("Please tell me about your deepest sorrows and your destroyed soul.")
        print("Don't forget that I am sensitive to punctuation.")
        j.caring_Jordan()   
    if choice == '3':
        print("Make yourself ready. let's insult each other!")
        print("Don't forget that I am sensitive to punctuation.")
        j.cursing_Jordan()
    if choice == '4':
        print("Ok then, let's talk about Corona.")
        print("Don't forget that I am sensitive to punctuation..")
        j.testing_Jordan()
    if choice == '5':
        print("I will be your guide in this meditation.")
        print("Don't forget that I am sensitive to punctuation..")
        j.testing_Jordan()
    if choice == 'q': # if user wants to quit
        break
    else: # if user pressed the wrong key.
        print("Try again.")