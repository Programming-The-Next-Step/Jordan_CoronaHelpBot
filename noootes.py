# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:13:06 2020

@author: User
"""
import random

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey']

question = ['How are you', 'How are you doing']
responses = ['Okay', "I'm fine"]
    
while True:
    userInput = input(">>> ")
    if userInput in greetings: 
        random_greeting = random.choice(greetings)
        print(random_greeting)
    elif userInput in question:
        random_response = random.choice(responses)
        print(random_response)
    else:
        print("I did not understand what you said")
        
        
