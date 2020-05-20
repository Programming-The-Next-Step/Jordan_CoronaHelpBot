# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:11:07 2020

@author: User
"""

d={}
for x in range(1,10):
        d["Karton{0}".format(x)]=""
        
print(d)


# initiate introduction

from psychopy.event import waitKeys

def intro(word):
    word = 'ENTER'
    word.waitKeys(5)
    return 'Welcome. I am Jordan. What is your name?'

# open questions library

openQuestions = [
    []]

# curse words library



# open answers library 

openAnswers = [
    []]

# from first to second person translation library

2ndPersonPerspective = {
  "am"   : "are",
  "was"  : "were",
  "i"    : "you",
  "i'd"  : "you would",
  "i've"  : "you have",
  "i'll"  : "you will",
  "my"  : "your",
  "are"  : "am",
  "you've": "I have",
  "you'll": "I will",
  "your"  : "my",
  "yours"  : "mine",
  "you"  : "me",
  "me"  : "you"
}


## tokenize: part sentence into its single words
# 'and', cc = coordinating conjunction 
# 'now', rb = adverb 
# 'for', in = preposition 
# 'something', nn = noun
# 'different', jj = adjective 
# 'obtain', vb = verb
# 'they', = 
# 'the', dt = determiner
# 'to', to = 
sentence = 'something something'
tokens = nltk.word_tokenize(sentence)
tokens

# say what kind of word it is 
tagged = nltk.pos_tag(tokens)
tagged[0:2]

# say what kind if word it is
nltk.download('maxent_ne_chunker')
nltk.download('words')
entities = nltk.chunk.ne_chunk(tagged)
entities


# user interface

import tkinter
from tkinter import *


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
        
        
