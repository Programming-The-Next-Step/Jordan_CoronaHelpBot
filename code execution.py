# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:30:07 2020

@author: User
"""

import re
import random
from libraries import library_cursing
import Jordan


while True:
    print("Welcome. My name is Jordan. You can now choose a topic that we can talk about.")
    print("Press '1' to have some good old-fashioned smalltalk.")
    print("Press '2' to tell me about your deepest sorrows and your destroyed soul.")
    print("Press '3' to curse with me.")
    print("Press '4' to talk about Corona.")
    
    choice = input(">>> ")
    
    
    if choice == '1' :
        print("Alrighty, let's do some chitchatting.")
        Jordan.smalltalk_Jordan()
    if choice == '2' :
        print("Please tell me about your deepest sorrows and your destroyed soul.")
        Jordan.caring_Jordan()   
    if choice == '3' :
        print("Make yourself ready. let's insult each other!")
        Jordan.cursing_Jordan()
    if choice == '4' :
        print("Ok then, let's talk about Corona.")
        Jordan.testing_Jordan()
    else:
        break