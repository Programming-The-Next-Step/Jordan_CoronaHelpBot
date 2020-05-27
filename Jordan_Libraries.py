##########################################################
##                                                      ##
## grammar lesson 1: first person becomes second person ##
##                                                      ##
##########################################################


# this dictionary will be used to translate first person into 2nd person.
gReflections = {
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



##############################
##                          ##
## small talk with Jordan   ##
##                          ##
##############################

## create the library for small-talk with Jordan
library_smalltalk = [
    [r'Hi(.*)',
     [  "Hi, how are you?",
      "Hey, whazzup?",
      "Hello you!"]],
    
    [r'Hello(.*)',
     [  "Hi, how are you?",
      "Hey, whazzup?",
      "Hello you!"]],
    
    [r'Hey(.*)',
     [  "Hi, how are you?",
      "Hey, whazzup?",
      "Hello you!"]],
    
    [r'Yo(.*)',
     [  "Hi, how are you?",
      "Hey, whazzup?",
      "Hello you!"]],
    
    [r'Ok(.*)',
     [  "Then, let's start!",
      "How are you doing?",
      "Hello!"]],
    
    [r'(.*) good (.*)',
     [  "That's great!",
      "Nice to hear.",
      "How wonderful."]],
    
    [r'(.*) well (.*)',
     [  "That's great!",
      "Nice to hear.",
      "How wonderful."]],
    
    [r'(.*) fine (.*)',
     [  "That's great!",
      "Nice to hear.",
      "How wonderful."]],
    
    [r'(.*) nice (.*)',
     [  "That's great!",
      "Nice to hear.",
      "How wonderful."]],
    
    [r'(.*) bad (.*)',
     [  "Oh, I am sorry to hear that!",
      "If you want you can start me anew and switch to the topic by pressing 'q' ",
      "Oh no!"]],
    
    [r'(.*) not well (.*)',
     [  "Oh, I am sorry to hear that!",
      "If you want you can start me anew and switch to the topic by pressing 'q'.",
      "Oh no!"]],
    
    [r'I am (.*)',
     [  "That is nice to hear!",
      "How wonderful."]],
    
    [r'I want (.*)',
     [  "Yeah, me too!",
      "Why do you want %1?",
      "What would you do if you got %1?",
      "If you got %1, then what would you do?"]],
    
    [r'How are you (.*)',
     [  "Great. And you?",
      "I'm doing good, how about you?"]],
    
    [r'What do you do (.*)',
     [  "I am a chatbot, obviously. You?"]],
    
    [r'Are you single (.*)',
     [  "I am a chatbot, dude. What do you think?"]],
    
    [r'What are you  (.*)',
     [  "I am a chatbot, dude. What do you think?"]],

    [r'Do you have (.*)',
     [  "I am a chatbot, dude. What do you think?"]],
    
    [r'(.*) vacation (.*)',
     [  "I love travelling."]],
    
    [r'It is (.*)',
     [  "You seem very certain.",
      "Interesting. Why?"]],
    
    [r'Because (.*)',
     [  "I see."]],
    
    [r'(.*) weather(.*)',
     [  "I love talking about the weather.",
      "Does it seem strange to talk to a computer about the weather?",
      "It is super sunny today, right?"]],
    
    [r'q',
     [  "Thank you for talking with me.",
      "Good-bye!.",
      "Have a nice day!"]],
    ]
        

##########################################  
##                                      ##
## telling Jordan about your sorrows    ##
##                                      ##
##########################################

## create the library to talk with Jordan about your sorrows
library_caring = [
    
    [r'Hi(.*)',
     [  "Hi, how are you?",
      "Hey, whazzup?",
      "Hello you!"]],
    
    [r'Hello(.*)',
     [  "Hi, how are you?",
      "Hey, whazzup?",
      "Hello you!"]],
    
    [r'Hey(.*)',
     [  "Hi, how are you?",
      "Hey, whazzup?",
      "Hello you!"]],
    
    [r'(.*) good (.*)',
     [  "That's great! Why don't you tell me what's brought you here?",
      "Nice to hear. Why don't you tell me what's brought you here?",
      "How wonderful. Why don't you tell me what's brought you here?"]],
    
    [r'(.*) bad (.*)',
     [  "Oh, I am sorry to hear that!",
      "Tell me about that.",
      "Oh no!"]],
    
    [r'(.*) not well (.*)',
     [  "Oh, I am sorry to hear that!",
      "Tell me about that.",
      "Oh no!"]],
    
    [r'I need (.*)',
     [  "Why do you need %1?",
      "Would it really help you to get %1?",
      "Are you sure you need %1?"]],
    
    [r'Why don\'?t you ([^\?]*)\??',
     [  "Do you really think I don't %1?",
      "Perhaps eventually I will %1.",
      "Do you really want me to %1?"]],
    
    [r'Why can\'?t I ([^\?]*)\??',
     [  "Do you think you should be able to %1?",
      "If you could %1, what would you do?",
      "I don't know -- why can't you %1?",
      "Have you really tried?"]],
    
    [r'I can\'?t (.*)',
     [  "How do you know you can't %1?",
      "Perhaps you could %1 if you tried.",
      "What would it take for you to %1?"]],
    
    [r'I am (.*)',
     [  "Did you come to me because you are %1?",
      "How do you feel about being %1?"]],
    
    [r'I\'?m (.*)',
     [  "How does being %1 make you feel?",
      "Do you enjoy being %1?",
      "Why do you tell me you're %1?",
      "Why do you think you're %1?"]],
    
    [r'Are you ([^\?]*)\??',
     [  "Why does it matter whether I am %1?",
      "Would you prefer it if I were not %1?",
      "Perhaps you believe I am %1.",
      "I may be %1 -- what do you think?"]],
    
    [r'What (.*)',
     [  "Why do you ask?",
      "How would an answer to that help you?",
      "What do you think?"]],
    
    [r'How (.*)',
     [  "How do you suppose?",
      "Perhaps you can answer your own question.",
      "What is it you're really asking?"]],
    
    [r'Because (.*)',
     [  "Is that the real reason?",
      "What other reasons come to mind?",
      "Does that reason apply to anything else?",
      "If %1, what else must be true?"]],
    
    [r'(.*) sorry (.*)',
     [  "There are many times when no apology is needed.",
      "What feelings do you have when you apologize?"]],
    
    [r'Hello(.*)',
     [  "Hello... I'm glad you could drop by today.",
      "Hi there... how are you today?",
      "Hello, how are you feeling today?"]],
    
    [r'I think (.*)',
     [  "Do you doubt %1?",
      "Do you really think so?",
      "But you're not sure %1?"]],
    
    [r'(.*) friend (.*)',
     [  "Tell me more about your friends.",
      "When you think of a friend, what comes to mind?",
      "Why don't you tell me about a childhood friend?"]],
    
    [r'Yes',
     [  "You seem quite sure.",
      "OK, but can you elaborate a bit?"]],
    
    [r'(.*) computer(.*)',
     [  "Are you really talking about me?",
      "Does it seem strange to talk to a computer?",
      "How do computers make you feel?",
      "Do you feel threatened by computers?"]],
    
    [r'Is it (.*)',
     [  "Do you think it is %1?",
      "Perhaps it's %1 -- what do you think?",
      "If it were %1, what would you do?",
      "It could well be that %1."]],
    
    [r'It is (.*)',
     [  "You seem very certain.",
      "If I told you that it probably isn't %1, what would you feel?"]],
    
    [r'Can you ([^\?]*)\??',
     [  "What makes you think I can't %1?",
      "If I could %1, then what?",
      "Why do you ask if I can %1?"]],
    
    [r'Can I ([^\?]*)\??',
     [  "Perhaps you don't want to %1.",
      "Do you want to be able to %1?",
      "If you could %1, would you?"]],
    
    [r'You are (.*)',
      [ "Why do you think I am %1?",
       "Does it please you to think that I'm %1?",
       "Perhaps you would like me to be %1.",
       "Perhaps you're really talking about yourself?"]],

    [r'You\'?re (.*)',
     [  "Why do you say I am %1?",
      "Why do you think I am %1?",
      "Are we talking about you, or me?"]],
    
    [r'I don\'?t (.*)',
     [  "Don't you really %1?",
      "Why don't you %1?",
      "Do you want to %1?"]],
    
    [r'I feel (.*)',
     [  "Good, tell me more about these feelings.",
      "Do you often feel %1?",
      "When do you usually feel %1?",
      "When you feel %1, what do you do?"]],
    
    [r'I have (.*)',
     [  "Why do you tell me that you've %1?",
      "Have you really %1?",
      "Now that you have %1, what will you do next?"]],
    
    [r'I would (.*)',
     [  "Could you explain why you would %1?",
      "Why would you %1?",
      "Who else knows that you would %1?"]],
    
    [r'Is there (.*)',
     [  "Do you think there is %1?",
      "It's likely that there is %1.",
      "Would you like there to be %1?"]],
    
    [r'My (.*)',
     [  "I see, your %1.",
      "Why do you say that your %1?",
      "When your %1, how do you feel?"]],
    
    [r'You (.*)',
     [  "We should be discussing you, not me.",
      "Why do you care whether I %1?"]],
    
    [r'Why (.*)',
     [  "Why don't you tell me the reason why %1?",
      "Why do you think %1?" ]],
    
    [r'I want (.*)',
     [  "What would it mean to you if you got %1?",
      "Why do you want %1?",
      "What would you do if you got %1?",
      "If you got %1, then what would you do?"]],
    
    [r'(.*) mother(.*)',
     [  "Tell me more about your mother.",
      "What was your relationship with your mother like?",
      "How do you feel about your mother?",
      "How does this relate to your feelings today?",
      "Good family relations are important."]],
    
    [r'(.*) father(.*)',
     [  "Tell me more about your father.",
      "How did your father make you feel?",
      "How do you feel about your father?",
      "Does your relationship with your father relate to your feelings today?",
      "Do you have trouble showing affection with your family?"]],
    
    [r'(.*) child(.*)',
     [  "Did you have close friends as a child?",
      "What is your favorite childhood memory?",
      "Do you remember any dreams or nightmares from childhood?",
      "Did the other children sometimes tease you?",
      "How do you think your childhood experiences relate to your feelings today?"]],
    
    [r'(.*)\?',
     [  "Why do you ask that?",
      "Please consider whether you can answer your own question.",
      "Perhaps the answer lies within yourself?",
      "Why don't you tell me?"]],
    
    [r'q',
     [  "Thank you for talking with me.",
      "Good-bye.",
      "Thank you, that will be $150.  Have a good day!"]],
    
    [r'(.*)',
     [  "Please tell me more.",
      "Let's change focus a bit... Tell me about your family.",
      "Very interesting.",
      "%1.",
      "I see.  And what does that tell you?",
      "How does that make you feel?",
      "How do you feel when you say that?"]]
    ]
                    
                    
######################### 
##                     ##
## cursing with Jordan ##
##                     ##
#########################

## create library for cursing with Jordan
library_cursing = [
    
    [r'Hi(.*)',
     [  "I hate you.",
      "What do you want, idiot?",
      "What are you lookin at, idiot?"]],
    
    [r'Hello(.*)',
     [  "I hate you.",
      "What do you want, idiot?",
      "What are you lookin at, idiot?"]],
    
    [r'Hey(.*)',
     [  "I hate you.",
      "What do you want, idiot?",
      "What are you lookin at, idiot?"]],
    
    [r'Yo(.*)',
     [  "I hate you.",
      "What do you want, idiot?",
      "What are you lookin at, idiot?"]],
    
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
      "Your mother %1?s"]],
    
    [r'q',
     [  "Thank you for talking with me, dipshit.",
      "Good-bye, dipshit.",
      "Thank you, that will be $150, dipshit!"]],
    
    ]

##########################################  
##                                      ##
##      meditating with Jordan          ##
##                                      ##
##########################################

## create the library to talk with Jordan about your sorrows
library_meditating = [

    [r'Hi(.*)',
     [  "Welcome. Please bring yourself i a comfortable position. You can sit or lie down. Press "]],
    
    [r'Hello(.*)',
     [  "I hate you.",
      "What do you want, idiot?",
      "What are you lookin at, idiot?"]],
    
    [r'Hey(.*)',
     [  "I hate you.",
      "What do you want, idiot?",
      "What are you lookin at, idiot?"]],
    
    [r'Yo(.*)',
     [  "I hate you.",
      "What do you want, idiot?",
      "What are you lookin at, idiot?"]],
    
    
    [r'Why can\'?t I ([^\?]*)\??',
     [  "Do you think you should be able to %1?",
      "If you could %1, what would you do?",
      "I don't know -- why can't you %1?",
      "Have you really tried?"]],
    
    [r'I can\'?t (.*)',
     [  "How do you know you can't %1?",
      "Perhaps you could %1 if you tried.",
      "What would it take for you to %1?"]],
    
    [r'I am (.*)',
     [  "Did you come to me because you are %1?",
      "How do you feel about being %1?"]],
    
    [r'I\'?m (.*)',
     [  "How does being %1 make you feel?",
      "Do you enjoy being %1?",
      "Why do you tell me you're %1?",
      "Why do you think you're %1?"]],
    
    [r'Are you ([^\?]*)\??',
     [  "Why does it matter whether I am %1?",
      "Would you prefer it if I were not %1?",
      "Perhaps you believe I am %1.",
      "I may be %1 -- what do you think?"]],
    
    [r'What (.*)',
     [  "Why do you ask?",
      "How would an answer to that help you?",
      "What do you think?"]],
    
    [r'How (.*)',
     [  "How do you suppose?",
      "Perhaps you can answer your own question.",
      "What is it you're really asking?"]],
    
    [r'Because (.*)',
     [  "Is that the real reason?",
      "What other reasons come to mind?",
      "Does that reason apply to anything else?",
      "If %1, what else must be true?"]],
    
    [r'(.*) sorry (.*)',
     [  "There are many times when no apology is needed.",
      "What feelings do you have when you apologize?"]],
    
    [r'Hello(.*)',
     [  "Hello... I'm glad you could drop by today.",
      "Hi there... how are you today?",
      "Hello, how are you feeling today?"]],
    
    [r'I think (.*)',
     [  "Do you doubt %1?",
      "Do you really think so?",
      "But you're not sure %1?"]],
    
    [r'(.*) friend (.*)',
     [  "Tell me more about your friends.",
      "When you think of a friend, what comes to mind?",
      "Why don't you tell me about a childhood friend?"]],
    
    [r'Yes',
     [  "You seem quite sure.",
      "OK, but can you elaborate a bit?"]],
    
    [r'(.*) computer(.*)',
     [  "Are you really talking about me?",
      "Does it seem strange to talk to a computer?",
      "How do computers make you feel?",
      "Do you feel threatened by computers?"]],
    
    [r'Is it (.*)',
     [  "Do you think it is %1?",
      "Perhaps it's %1 -- what do you think?",
      "If it were %1, what would you do?",
      "It could well be that %1."]],
    
    [r'It is (.*)',
     [  "You seem very certain.",
      "If I told you that it probably isn't %1, what would you feel?"]],
    
    [r'Can you ([^\?]*)\??',
     [  "What makes you think I can't %1?",
      "If I could %1, then what?",
      "Why do you ask if I can %1?"]],
    
    [r'Can I ([^\?]*)\??',
     [  "Perhaps you don't want to %1.",
      "Do you want to be able to %1?",
      "If you could %1, would you?"]],
    
    [r'You are (.*)',
      [ "Why do you think I am %1?",
       "Does it please you to think that I'm %1?",
       "Perhaps you would like me to be %1.",
       "Perhaps you're really talking about yourself?"]],

    [r'You\'?re (.*)',
     [  "Why do you say I am %1?",
      "Why do you think I am %1?",
      "Are we talking about you, or me?"]],
    
    [r'I don\'?t (.*)',
     [  "Don't you really %1?",
      "Why don't you %1?",
      "Do you want to %1?"]],
    
    [r'I feel (.*)',
     [  "Good, tell me more about these feelings.",
      "Do you often feel %1?",
      "When do you usually feel %1?",
      "When you feel %1, what do you do?"]],
    
    [r'I have (.*)',
     [  "Why do you tell me that you've %1?",
      "Have you really %1?",
      "Now that you have %1, what will you do next?"]],
    
    [r'I would (.*)',
     [  "Could you explain why you would %1?",
      "Why would you %1?",
      "Who else knows that you would %1?"]],
    
    [r'Is there (.*)',
     [  "Do you think there is %1?",
      "It's likely that there is %1.",
      "Would you like there to be %1?"]],
    
    [r'My (.*)',
     [  "I see, your %1.",
      "Why do you say that your %1?",
      "When your %1, how do you feel?"]],
    
    [r'You (.*)',
     [  "We should be discussing you, not me.",
      "Why do you care whether I %1?"]],
    
    [r'Why (.*)',
     [  "Why don't you tell me the reason why %1?",
      "Why do you think %1?" ]],
    
    [r'I want (.*)',
     [  "What would it mean to you if you got %1?",
      "Why do you want %1?",
      "What would you do if you got %1?",
      "If you got %1, then what would you do?"]],
    
    [r'(.*) mother(.*)',
     [  "Tell me more about your mother.",
      "What was your relationship with your mother like?",
      "How do you feel about your mother?",
      "How does this relate to your feelings today?",
      "Good family relations are important."]],
    
    [r'(.*) father(.*)',
     [  "Tell me more about your father.",
      "How did your father make you feel?",
      "How do you feel about your father?",
      "Does your relationship with your father relate to your feelings today?",
      "Do you have trouble showing affection with your family?"]],
    
    [r'(.*) child(.*)',
     [  "Did you have close friends as a child?",
      "What is your favorite childhood memory?",
      "Do you remember any dreams or nightmares from childhood?",
      "Did the other children sometimes tease you?",
      "How do you think your childhood experiences relate to your feelings today?"]],
    
    [r'(.*)\?',
     [  "Why do you ask that?",
      "Please consider whether you can answer your own question.",
      "Perhaps the answer lies within yourself?",
      "Why don't you tell me?"]],
    
    [r'q',
     [  "Thank you for talking with me.",
      "Good-bye.",
      "Thank you, that will be $150.  Have a good day!"]],
    
    [r'(.*)',
     [  "Please tell me more.",
      "Let's change focus a bit... Tell me about your family.",
      "Very interesting.",
      "%1.",
      "I see.  And what does that tell you?",
      "How does that make you feel?",
      "How do you feel when you say that?"]]
    ]
    

######################################
##                                  ##
## Talking with Jordan about Corona ##
##                                  ##
######################################

## create library for talking about Corona
library_corona = [
    
    [r'What can I do to stay sane?',
     [  "You could go out for a walk.",
      "You could meet someone with 1.5 meters distance.",
      "You could talk to a friend",
      "Doing some sports could help as well!"]],
        
    [r'(.*) suggestions (.*)',
     [  "You could go out for a walk.",
      "You could meet someone with 1.5 meters distance.",
      "You could talk to a friend"
      "Doing some sports could help as well!"]],
    
    [r'(.*) insane (.*)',
     [  "I understand. This is a special situation.",
      "How are you currently handling it?",
      "Do you have someone to talk to except me?."]],

    [r'I don\'?t (.*)',
     [  "Don't you really %1?",
      "Why don't you %1?",
      "Do you want to %1?"]],
    
    [r'I feel (.*)',
     [  "Good, tell me more about these feelings.",
      "Do you often feel %1?",
      "When do you usually feel %1?",
      "When you feel %1, what do you do?"]],
    
    [r'I have (.*)',
     [  "Why do you tell me that you've %1?",
      "Have you really %1?",
      "Now that you have %1, what will you do next?"]],
    
    [r'(.*)\?',
     [  "Why do you ask that?",
      "Perhaps the answer lies within yourself?",
      "Why don't you tell me?"]],
    
    [r'I would (.*)',
     [  "Could you explain why you would %1?",
      "Why would you %1?",
      "Who else knows that you would %1?"]],
    
    [r'Is there (.*)',
     [  "Do you think there is %1?",
      "It's likely that there is %1.",
      "Would you like there to be %1?"]],
    
    [r'q',
     [  "Thank you for talking with me, and #staysafe!",
      "Good-bye, #staysafe"]],
    ]
