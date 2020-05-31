**Why does Jordan exist?**

We are writing the 6th of May 2020, Berlin, Germany. Humans find themselves in the middle of a pandemic, the corona-virus crisis, that has tremendous consequences for economy, politics, and mental health due to world-wide limitations of social contact. Those limitations forbid for many shops, restaurants, and other venues to open for guests. And more, they forbid for people to meet each other physically in order to avoid spreading the flu-like but slightly more dangerous virus. Current popular hashtags that sum up the phenomenon are #socialdistancing, #stayhome, and #staysafe. 

It seems like the world has moved online. Work meetings, parties, lectures take place in the digital spheres. It is actually more physical than social distancing, when you think about it. 

But what does it do to humans, having to isolate themselves? Studies on self-isolation show that psychopathology follows more quickly than expected, especially for extroverts. Additionally, changes in brain matter occur. So. What can we do to stay sane?
Here is where Jordan comes in. 

**What can Jordan do?**

Jordan could be called a therapist without a license, an advisor, a friend when you feel lonely. Jordan can also be evil Jordan, when you just need some katharsis and blow off some steam. In these positions, Jordan can be a man or a woman or something else you imagine she/him/it to be. It is possible to talk with Jordan about the following things:

*general*
1. hold smalltalk.
2. tell about your deepest worries, your aching heart, your destroyed soul. But yes, Jordan also answers in case you are happy.

*calming down stuff*

3. curse with Jordan - because, let us be honest, this is what we want the chatbots to do really. 
4. meditating with mindful Jordan.

*corona-related*

5. ask for suggestions to stay sane. This will include going outside for a walk, going to meet a friend or doing some sports, and discussing how crazy the media is in times of corona. 


**Implementation Graph**

![Jordan Output Flow](https://user-images.githubusercontent.com/64072862/81957953-92366100-960d-11ea-9d37-abc82e5fd2e9.png)

**My Project**

My goal for this project is to make a *simple* chatbot that can give people comfort in times of corona. What I am cutting, if I am short on time is to not implement all modules (conversation types) that I am planning now. But, what I will do, when I have extra time, is to add more modules and things to discuss, and just make Jordan a bit more advanced. 

Steps Implemented
1. Create a flow chart of Jordan's output. Actually I did this already, and you can see it above.
2. Create an answers library that includes keywords Jordan is supposed to react to. For example, when someone writes 'I need chocolate', 'need', would be such a keyword that Jordan can respond to with 'Why do you think you need chocolate?'? For every topic, there should be one library (cursing, caring, meditating etc.)
3. Create a function, in which the participant can pick a topic to talk about. 
4. Create instruction statements that guide the user.
4. Create statements that end the conversation. Then Jordan asks if you would want to end the conversation or if you want to just change the topic. 

**My Code**

As language, I will use python. For packages, I am going to use pydot to create a flowchart of the Jordan output. I will also use the re package, which I will need to access the right positions in the libraries and furthermore the random package to pick random statements as an answer from Jordan. I will use a couple more functions then, which you can see below.

**References**

Jordan is adapted from the therapy chatbot "Eliza" Wikipedia: https://de.wikipedia.org/wiki/ELIZA Inventor: J. Weizenbaum, ELIZA - A Computer Program For the Study of Natural Language Communication Between Man And Machine Communications of the ACM, Vol 9, No 1, January 1966

The code I am adapting Jordan from Github: Original code written by Joe Strout, with some updates by Jeff Epler. Converted to a module and updated for Python 3 by Jez Higgins.Authors of Code so far: Original code written by Joe Strout, with some updates by Jeff Epler. Converted to a module and updated for Python 3 by Jez Higgins.

Other references:

https://github.com/wadetb/eliza/blob/master/eliza.py

https://data-flair.training/blogs/python-chatbot-project/

https://github.com/codeanticode/eliza/blob/master/examples/ElizaChat/ElizaChat.pde

sofa link: https://images.app.goo.gl/oV8PSzeeGNP129Am6
