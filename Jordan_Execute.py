# -*- coding: utf-8 -*-
"""
Created on Sun May 31 14:47:15 2020

@author: User
"""

import re # import regular expressions for the appropriate access to the libraries
import random # import random to pick a random answer for Jordan from the libraries
from playsound import playsound
from Jordan_Library import dict_smalltalk, dict_caring, dict_cursing, dict_meditating, dict_corona # import dictionairies
from Jordan_Class import JordanBot

test = JordanBot('Marla')

test.chat()