# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:22:43 2020

@author: User
"""

import re # importing regular expression operations, which we need later to access the libraries
import random # later we want to pick a chatbot answer to a statement by random
from Jordan_Libraries import library_smalltalk, library_caring, library_cursing, library_corona, library_meditating
# and here we imported all the topic libraries   

from Jordan_Class import Jordan, execute_Jordan

execute_Jordan()