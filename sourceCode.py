## make a flow chart




## make a Jordan function
def Jordan(input)
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# open questions library

openQuestions = [
    []]

# open answers library 

# from first to second person translation library

2ndPersonPerspective = [
    ]



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


