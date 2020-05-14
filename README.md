# Who is Jordan?

*Jordan is a chatbot that helps you not get crazy in times of corona but if you do, then it is he/she/it that is here for you.*

**Why does Jordan exist?**

We are writing the 6th of May 2020, Berlin, Germany. Humans find themselves in the middle of a pandemic, the corona-virus crisis, that has tremendous consequences for economy, politics, and mental health due to world-wide limitations of social contact. Those limitations forbid for many shops, restaurants, and other venues to open for guests. And more, they forbid for people to meet each other physically in order to avoid spreading the flu-like but slightly more dangerous virus. Current popular hashtags that sum up the phenomenon are #socialdistancing, #stayhome, and #staysafe. 

It seems like the world has moved online. Work meetings, parties, lectures take place in the digital spheres. It is actually more physical than social distancing, when you think about it. 

But what does it do to humans, having to isolate themselves? Studies on self-isolation show that psychopathology follows more quickly than expected, especially for extroverts. Additionally, changes in brain matter occur. So. What can we do to stay sane?
Here is where Jordan comes in. 

**What can Jordan do?**

Jordan could be called a therapist without a license, an advisor, a friend when you feel lonely. In this position, Jordan can be a man or a woman or something else you imagine she/him/it to be. It is possible to talk with Jordan about the following things:

*general*
1. hold smalltalk.
2. complain about your day.
3. tell about your deepest worries, your aching heart, your destroyed soul.
4. tell about how wonderful you feel today.
5. tell about your new crush.

*calming down stuff*

6. curse with Jordan - because, let us be honest, this is what we want the chatbots to do really. 
7. meditating with Jordan.

*corona-related*

6. ask for suggestions to stay sane. This will include going outside for a walk, going to meet a friend or doing some sports. 
Jordan can also remind you of these things.
7. discuss how crazy the media is in times of corona. 
8. discuss how hard it is to be in self-isoltation.

**Flow Chart**

![Jordan Output Flow](https://user-images.githubusercontent.com/64072862/81957953-92366100-960d-11ea-9d37-abc82e5fd2e9.png)

**My Project**

My goal for this project is to make a chatbot that can give people comfort in times of corona. What I am cutting, if I am short on time is to not implement all modules (conversation types) that I am planning now. But, what I will do, when I have extra time, is to add more modules and things to discuss, and just make Jordan a bit more advanced. 

Implementation Steps
1. Create a flow chart of Jordan's output. Actually I did this already, and you can see it above.
2. Create a function that decodes a sentence grammatically such that it will use an appropriate response. For this step, there might be several smaller functions to be created, for instance, one that converts the grammar aspects like changing from first-person to second-person perspective.
3. Create an answers library that includes keywords Jordan is supposed to react to. For example, when someone writes 'I need chocolate', 'need', would be such a keyword that Jordan can respond to with 'Why do you think you need chocolate?'?
4. Create a function that initiates an introduction conversation. This introduction conversation is going to consist of a series of questions that come from a library in which introduction sentences are stored, such as "What is your name?" or "How are you today?"
5. Create a function, in which the participant can pick a topic to talk about. 
6. Create an open-question library within the example topic classes. There will be one for cursing with Jordan, one for small talk with Jordan, etc. 
7. Create a function that ends the conversation that activates once a button is pressed: Quit conversation. Then Jordan asks if you would want to end the conversation or if you want to just change the topic. 
3. Create a command interface that can be accessed over the browser. I do not know how that works yet, but I guess I will find out. I hope that in the end, there will be a link, on which will lead you to a window in your browser that looks like a chatroom. Maybe a bit more beautiful. Maybe there can be an image of two really comfortable sofas facing each other, while the sun is shining through the window. Warm colors would be nice to make the participant feel more comfortable.

**My Code**

As language, I will use python. For packages, I am going to use pydot to create a flowchart of the Jordan output. I will try to code the chatbot functions myself, which is why I will not use any chatbot-related packages. However, I might use psychopy and the string package. I will probably even use more packages than that, which I do not even know about yet!

eliza.py --> this is a code package on github that I will use as reference. 
