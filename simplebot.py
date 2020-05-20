# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:23:18 2020

@author: User
"""

library_cursing = [
    [r'You are a (.*)',
     [  "YOU are a %1?",
      "Right back at ya.",
      "Your mother is a %1?"]],
    
    [r'(.*)\!',
     [ "You’re the reason God created the middle finger.",
      "You’re a grey sprinkle on a rainbow cupcake.",
      "If your brain was dynamite, there wouldn’t be enough to blow your hat off.",
      "You are more disappointing than an unsalted pretzel.",
      "Light travels faster than sound which is why you seemed bright until you spoke.",
      "You know, you are a classic example of the inverse ratio between the size of the mouth and the size of the brain.",
      "To call you stupid would be an insult to stupid people! I've known sheep that could outwit you. I've worn dresses with higher IQs.",
      "Your heart is full of unwashed socks. Your soul is full of gunk ...The three words that best describe you are as follows, and I quote, Stink, stank, stunk!",
      "Hold still. I’m trying to imagine you with personality.",
      "Your face makes onions cry.",
      "Your brain's so minute that if a hungry cannibal cracked your head open, there wouldn't be enough to cover a small water biscuit.",
      "Stupid, fat hobbit.",
      "Keep rolling your eyes, you might eventually find a brain.",
      "Fool of a Took! Throw yourself in next time and rid us of your stupidity!",
      "OH MY GOD! IT SPEAKS!",
      "You are so full of shit, the toilet’s jealous.",
      "You're the reason the gene pool needs a lifeguard'",
      "You must have been born on the highway cos' that's where most accidents happen.",
      "Is your ass jealous of the amount of shit that just came out of your mouth",
      "When you were born, the doctor threw you out the window and the window threw you back.",
      "I think... no, I am positive... that you are the most unattractive being I have ever met in my entire life. In the short time we've been together, you have demonstrated every loathsome characteristic of the human personality and even discovered a few new ones. You are physically repulsive, intellectually retarded, you're morally reprehensible, vulgar, insensitive, selfish, stupid, you have no taste, a lousy sense of humor and you smell. You're not even interesting enough to make me sick.",
      "You are a fart factory, slug-slimed sack of rat guts in cat vomit. A cheesy scab picked pimple squeezing finger bandage. A week old maggot burger with everything on it and flies on the side."
      ]],
    

    [r'Are you ([^\?]*)\??',
     [  "OH MY GOD! IT SPEAKS!",
      "Are YOU %1??",
      "Are you talking to yourself?"]],
    
    [r'(.*) sorry (.*)',
     [  "Me, too."]],
    
    [r'(.*) fuck (.*)',
     [  "You are so full of shit, the toilet’s jealous.",
      "Stupid, fat hobbit.",
      "You’re the reason God created the middle finger."]],

    [r'You are (.*)',
      [ "YOU are %1?",
      "Right back at ya.",
      "Your mother is %1?"]],

    [r'You\'?re (.*)',
     [  "YOU are %1?",
      "Right back at ya.",
      "Your mother is %1?"]],

    [r'You (.*)',
     [  "YOU %1?",
      "Right back at ya.",
      "Your mother %1?"]],
    
    [r'quit',
     [  "Thank you for talking with me, dipshit.",
      "Good-bye, dipshit.",
      "Thank you, that will be $150, dipshit!"]],
    ]
    
## create function for cursing with Jordan

import re
import random

# def cursing_Jordan(userInput):
keys_cursing = list(map(lambda x:re.compile(x[0], re.IGNORECASE), library_cursing))
values_cursing = list(map(lambda x:x[1],library_cursing))
    
while True:
    userInput = input(">>> ")
    for i in range(0, len(keys_cursing)):
        match = keys_cursing[i].match(userInput)
        if match:
            resp = random.choice(values_cursing[i])
            pos = resp.find('%')
            print(resp)
        else:
            print("I did not understand what you said")