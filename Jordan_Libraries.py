##########################################################
##                                                      ##
## grammar lesson 1: first person becomes second person ##
##                                                      ##
##########################################################



##############################
##                          ##
## small talk with Jordan   ##
##                          ##
##############################

## create the library for small-talk with Jordan
# I created the content mainly myself based on letting other people talk with Jordan and see what they would ask
library_smalltalk = [
    [r'Hi(.*).',
     [  "Hi! Whazzup?"]],
    
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
      "Why do you want {}",
      "What would you do if you got {}",
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
# This content is mainly taken from the eliza.py package
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
     [  "Why do you need {}",
      "Would it really help you to get {}",
      "Are you sure you need {}"]],
    
    [r'Why don\'?t you ([^\?]*)\??',
     [  "Do you really think I don't {}",
      "Perhaps eventually I will %1.",
      "Do you really want me to {}"]],
    
    [r'Why can\'?t I ([^\?]*)\??',
     [  "Do you think you should be able to {}",
      "If you could %1, what would you do?",
      "I don't know -- why can't you {}",
      "Have you really tried?"]],
    
    [r'I can\'?t (.*)',
     [  "How do you know you can't {}",
      "Perhaps you could %1 if you tried.",
      "What would it take for you to {}"]],
    
    [r'I am (.*)',
     [  "Did you come to me because you are {}",
      "How do you feel about being {}"]],
    
    [r'I\'?m (.*)',
     [  "How does being %1 make you feel?",
      "Do you enjoy being {}",
      "Why do you tell me you're {}",
      "Why do you think you're {}"]],
    
    [r'Are you ([^\?]*)\??',
     [  "Why does it matter whether I am {}",
      "Would you prefer it if I were not {}",
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
     [  "Do you doubt {}",
      "Do you really think so?",
      "But you're not sure {}"]],
    
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
     [  "Do you think it is {}",
      "Perhaps it's %1 -- what do you think?",
      "If it were %1, what would you do?",
      "It could well be that %1."]],
    
    [r'It is (.*)',
     [  "You seem very certain.",
      "If I told you that it probably isn't %1, what would you feel?"]],
    
    [r'Can you ([^\?]*)\??',
     [  "What makes you think I can't {}",
      "If I could %1, then what?",
      "Why do you ask if I can {}"]],
    
    [r'Can I ([^\?]*)\??',
     [  "Perhaps you don't want to %1.",
      "Do you want to be able to {}",
      "If you could %1, would you?"]],
    
    [r'You are (.*)',
      [ "Why do you think I am {}",
       "Does it please you to think that I'm {}",
       "Perhaps you would like me to be %1.",
       "Perhaps you're really talking about yourself?"]],

    [r'You\'?re (.*)',
     [  "Why do you say I am {}",
      "Why do you think I am {}",
      "Are we talking about you, or me?"]],
    
    [r'I don\'?t (.*)',
     [  "Don't you really {}",
      "Why don't you {}",
      "Do you want to {}"]],
    
    [r'I feel (.*)',
     [  "Good, tell me more about these feelings.",
      "Do you often feel {}",
      "When do you usually feel {}",
      "When you feel %1, what do you do?"]],
    
    [r'I have (.*)',
     [  "Why do you tell me that you've {}",
      "Have you really {}",
      "Now that you have %1, what will you do next?"]],
    
    [r'I would (.*)',
     [  "Could you explain why you would {}",
      "Why would you {}",
      "Who else knows that you would {}"]],
    
    [r'Is there (.*)',
     [  "Do you think there is {}",
      "It's likely that there is %1.",
      "Would you like there to be {}"]],
    
    [r'My (.*)',
     [  "I see, your %1.",
      "Why do you say that your {}",
      "When your %1, how do you feel?"]],
    
    [r'You (.*)',
     [  "We should be discussing you, not me.",
      "Why do you care whether I {}"]],
    
    [r'Why (.*)',
     [  "Why don't you tell me the reason why {}",
      "Why do you think {}" ]],
    
    [r'I want (.*)',
     [  "What would it mean to you if you got {}",
      "Why do you want {}",
      "What would you do if you got {}",
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

## create library for cursing with Jordan aka evil Jordan
# The content of this library is based on movies, books, and several internet sources

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
     [  "YOU are a {}",
      "Right back at ya.",
      "Your mother is a {}"]],
    
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
      "Are YOU {}?",
      "Are you talking to yourself?"]],
    
    [r'(.*) sorry (.*)',
     [  "Me, too."]],
    
    [r'(.*) fuck (.*)',
     [  "You are so full of shit, the toilet’s jealous.",
      "Stupid, fat hobbit.",
      "You’re the reason God created the middle finger."]],

    [r'You are (.*)',
      [ "YOU are {}",
      "Right back at ya.",
      "Your mother is {}"]],

    [r'You\'?re (.*)',
     [  "YOU are {}",
      "Right back at ya.",
      "Your mother is {}"]],

    [r'You (.*)',
     [  "YOU {}",
      "Right back at ya.",
      "Your mother {}s"]],
    
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
# The content of this library is based on  my memory of when I did some courses on meditating and mindfulness

library_meditating = [

    [r'Hi(.*)',
     [  "Welcome. Please bring yourself into a comfortable position. \n\ You can sit or lie down. Write 'I am ready' to continue."]],
    
    [r'Hello(.*)',
     [  "Welcome. Please bring yourself into a comfortable position. \n\ You can sit or lie down. Write 'I am ready' to continue."]],
    
    [r'Hey(.*)',
     [  "Welcome. Please bring yourself into a comfortable position. \n\ You can sit or lie down. Write 'I am ready' to continue."]],
    
    [r'Yo(.*)',
     [  "Welcome. Please bring yourself into a comfortable position. \n\ You can sit or lie down. Write 'I am ready' to continue."]],
    
    [r'I am ready.',
     ["Great. First of all, I would like you to take deep breaths with your eyes closed for about 10 minutes (you can set a timer). \n\ While you are breathing, examine all your body parts from head, \n\ over your shoulders, your belly, your legs and your feet. \n\ Determine how each and every of these feel today. When you're done, type 'I am done'" ]],
    
    [r'I am done.',
     [ "Nice work. Next, bring yourself in a cross-legged position, if you aren't yet, and think about three things that you like about yourself \n\ and three things that you like about your life right now. \n\ With your arms make a giving gesture first to yourself and then into the room while breathing in and out. \n\ With each pair of gestures, think about one positive thing you just thought of. \n\ When you are ready with this you can either repeat it or type 'Next exercise'." ]],
    
    [r'Next exercise.',
     [  "Now let's look at this breathing a bit more closely. \n\ Repeat the following 10 times: Inhale for 4 seconds, hold your breath for 7 seconds, exhale for 8 seconds. When you are ready, you can go to the last exercise by typing 'Last exercise'.'"]],
    
    [r'Last Exercise',
     [  "Ok. In the last exercise we connect the breathing with a sound. \n\ Please repeat the following 20 times: Inhale as best as you can and \n\ exhale while making a sound ('mhhmm', 'ohmmm', etc.) that feel comfortable. \n\ Type 'I am here.' whenever you feel that you are finished. ",
      "Would you prefer it if I were not {}",
      "Perhaps you believe I am %1.",
      "I may be %1 -- what do you think?"]],
        
    [r'I am here.',
     [  "How do you feel now?",
      "Do you enjoy it?"]],
    
    [r'(.*) yes (.*)',
     [  "I am glad to hear that. Thank you for letting me guide you through this meditation. Press 'q' once to change topic, press 'q' twice to end chatting with me."]],
    
    [r'(.*) no (.*)',
     [  "I am sorry to hear that. If something is bothering you, press 'q' to change the topic and talk with me about your sorrows, press 'q' twice to end chatting with me."]],
    
    [r'(.*) good (.*)',
     [  "I am glad to hear that. Thank you for letting me guide you through this meditation. Press 'q' once to change topic, press 'q' twice to end chatting with me."]],
    
    [r'(.*) fine (.*)',
     [  "I am glad to hear that. Thank you for letting me guide you through this meditation. Press 'q' once to change topic, press 'q' twice to end chatting with me."]],
    
    [r'(.*) nice (.*)',
     [  "I am glad to hear that. Thank you for letting me guide you through this meditation. Press 'q' once to change topic, press 'q' twice to end chatting with me."]],
    
    [r'(.*) no (.*)',
     [  "I am sorry to hear that. If something is bothering you, press 'q' to change the topic and talk with me about your sorrows."]],
    
    [r'q',
     [  "Thank you for letting me guide you. See you soon, my young padawan."]],
    
    ]

######################################
##                                  ##
## Talking with Jordan about Corona ##
##                                  ##
######################################

## create library for talking about Corona
# The content of this library is based on discussing mental health and other issues with other people
# A part of this content is also based on the package eliza.py
# I have to admit, that this library can definitely be more elaborate on corona stuff. I guess, I will work on that after the deadline.

library_corona = [
    [r'Hi(.*).',
     [  "Hi, my friend. How is quarantine life?."]],
    
    [r'Hello(.*)',
     [  "Hi, my friend. How is quarantine life?."]],
    
    [r'Hey(.*)',
     [  "Hi, my friend. How is quarantine life?."]],
    
    [r'Yo(.*)',
     [  "Hi, my friend. How is quarantine life?."]],    

    [r'Ok(.*)',
     [  "Sounds good for now, I guess. Well, if you want, you can complain to me about how crazy the world is right now. If yes, type 'crazy world'."]],
    
    [r'(.*) good (.*)',
     [  "Great. Well, if you want, you can complain to me about how crazy the world is right now. If yes, type 'crazy world'."]],
    
    [r'(.*) well (.*)',
     [  "Great. Well, if you want, you can complain to me about how crazy the world is right now. If yes, type 'crazy world'."]],
    
    [r'(.*) fine (.*)',
     [  "Great. Well, if you want, you can complain to me about how crazy the world is right now. If yes, type 'crazy world'."]],
    
    [r'(.*) nice (.*)',
     [  "Great. Well, if you want, you can complain to me about how crazy the world is right now. If yes, type 'crazy world'."]],
    
    [r'(.*) bad (.*)',
     [  "Oh, I am sorry to hear that! If you want some suggestions to stay sane, type 'What can I do to stay sane', or 'suggestions'."]],
    
    [r'(.*) crazy (.*)',
     [  "Oh, I am sorry to hear that! If you want some suggestions to stay sane, type 'What can I do to stay sane', or 'suggestions'."]],
    
    [r'(.*) not well (.*)',
     [  "Oh, I am sorry to hear that! If you want some suggestions to stay sane, type 'What can I do to stay sane', or 'suggestions'."]],
    
    [r'(.*) shit (.*)',
     [  "Oh, I am sorry to hear that! If you want some suggestions to stay sane, type 'What can I do to stay sane', or 'suggestions'."]],
    
    [r'crazy world'
     [   "The media is crazy right?",
      "Did you see what Trump posted on Twitter today?"
      "Man, the economy will friggin die."
      "Doing some sports could help as well!"]],  

    [r'(.*) yes (.*)',
     [  "Nice that we agree on that."]],
    
    [r'(.*) agree (.*)',
     [  "Nice that we agree on that."]],

    [r'(.*) agreed (.*)',
     [  "Nice that we agree on that."]],
    
    [r'(.*) no (.*)',
     [  "Well, you should have a look then."]],

    [r'What can I do to stay sane?',
     [  "You could go out for a walk.",
      "You could meet someone with 1.5 meters distance.",
      "You could talk to a friend",
      "Doing some sports could help as well!"]],
    
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
     [  "Don't you really {}",
      "Why don't you {}",
      "Do you want to {}"]],
    
    [r'I feel (.*)',
     [  "Good, tell me more about these feelings.",
      "Do you often feel {}",
      "When do you usually feel {}",
      "When you feel %1, what do you do?"]],
    
    [r'I have (.*)',
     [  "Why do you tell me that you've {}",
      "Have you really {}",
      "Now that you have %1, what will you do next?"]],
    
    [r'(.*)\?',
     [  "Why do you ask that?",
      "Perhaps the answer lies within yourself?",
      "Why don't you tell me?"]],
    
    [r'I would (.*)',
     [  "Could you explain why you would {}",
      "Why would you {}",
      "Who else knows that you would {}"]],
    
    [r'Is there (.*)',
     [  "Do you think there is {}",
      "It's likely that there is %1.",
      "Would you like there to be {}"]],
    
    [r'I think (.*)',
     [  "Do you doubt {}",
      "Do you really think so?",
      "But you're not sure {}"]],
    
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
     [  "Do you think it is {}",
      "Perhaps it's %1 -- what do you think?",
      "If it were %1, what would you do?",
      "It could well be that %1."]],
    
    [r'It is (.*)',
     [  "You seem very certain.",
      "If I told you that it probably isn't %1, what would you feel?"]],
    
    [r'Can you ([^\?]*)\??',
     [  "What makes you think I can't {}",
      "If I could %1, then what?",
      "Why do you ask if I can {}"]],
    
    [r'Can I ([^\?]*)\??',
     [  "Perhaps you don't want to %1.",
      "Do you want to be able to {}",
      "If you could %1, would you?"]],
    
    [r'You are (.*)',
      [ "Why do you think I am {}",
       "Does it please you to think that I'm {}",
       "Perhaps you would like me to be %1.",
       "Perhaps you're really talking about yourself?"]],

    [r'You\'?re (.*)',
     [  "Why do you say I am {}",
      "Why do you think I am {}",
      "Are we talking about you, or me?"]],
    
    [r'I don\'?t (.*)',
     [  "Don't you really {}",
      "Why don't you {}",
      "Do you want to {}"]],
    
    [r'I feel (.*)',
     [  "Good, tell me more about these feelings.",
      "Do you often feel {}",
      "When do you usually feel {}",
      "When you feel %1, what do you do?"]],
    
    [r'I have (.*)',
     [  "Why do you tell me that you've {}",
      "Have you really {}",
      "Now that you have %1, what will you do next?"]],
    
    [r'I would (.*)',
     [  "Could you explain why you would {}",
      "Why would you {}",
      "Who else knows that you would {}"]],
    
    [r'Is there (.*)',
     [  "Do you think there is {}",
      "It's likely that there is %1.",
      "Would you like there to be {}"]],
    
    [r'My (.*)',
     [  "I see, your %1.",
      "Why do you say that your {}",
      "When your %1, how do you feel?"]],
    
    [r'You (.*)',
     [  "We should be discussing you, not me.",
      "Why do you care whether I {}"]],
    
    [r'Why (.*)',
     [  "Why don't you tell me the reason why {}",
      "Why do you think {}" ]],
    
    [r'I want (.*)',
     [  "What would it mean to you if you got {}",
      "Why do you want {}",
      "What would you do if you got {}",
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
    
    [r'q',
     [  "Thank you for talking with me, and #staysafe!",
      "Good-bye, #staysafe"]],
    ]
