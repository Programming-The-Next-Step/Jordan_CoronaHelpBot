# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:02:57 2020

@author: User
"""
import pydot

graph = pydot.Dot(graph_type='digraph')

## creating nodes for bot ouput

node_1 = pydot.Node("Initiate Introduction \n\
                    Output 'What is your name?'", style="filled", fillcolor="purple", shape = 'box')
# example: what is your name? how are you?
node_2 = pydot.Node("Let participant pick a topic \n\
                    'Output 'Please pick a topic below.'", style="filled", fillcolor="blue", shape = 'box')
# example: curse with jordan, hold small-talk with jordan
node_3 = pydot.Node("Initiate Example Topic \n\
                    Output 'Small-talk with Jordan'", style="filled", fillcolor="green", shape = 'box')
node_4 = pydot.Node("Initiate Example Topic \n\
                     Output 'Cursing with Jordan'", style="filled", fillcolor="green", shape = 'box')
node_5 = pydot.Node("Initiate Example Topic \n\
                     Output 'Complain about quarantine'", style="filled", fillcolor="green", shape = 'box')
# example: Ok, you chose Example Topic. Why dont you start by telling me why you chose this topic?
node_6 = pydot.Node("Maintain Conversation \n\
                    Output 'Tell me more.'", style="filled", fillcolor="orange", shape = 'box')
node_7 = pydot.Node("Maintain Conversation \n\
                    Output 'Tell me more.'", style="filled", fillcolor="orange", shape = 'box')
node_8 = pydot.Node("Maintain Conversation \n\
                    Output 'Tell me more.'", style="filled", fillcolor="orange", shape = 'box')
# example: Open questions and fillers in that class of that specific example topic - Tell me more! How did that happen? I understand. 
node_9 = pydot.Node("End Conversation \n\
                    Output 'Thank you for trusting me. Do you want to pick another topic or do you want to say goodbye?'", style="filled", fillcolor="yellow", shape = 'box')
node_10 = pydot.Node("End Conversation \n\
                    Output 'Thank you for trusting me. Do you want to pick another topic or do you want to say goodbye?'", style="filled", fillcolor="yellow", shape = 'box')
node_11 = pydot.Node("End Conversation \n\
                    Output 'Thank you for trusting me. Do you want to pick another topic or do you want to say goodbye?'", style="filled", fillcolor="yellow", shape = 'box')
# example: Ok, you wanted to end this conversation. Do you want to choose another topic?


# creating nodes for participants response

# add nodes


graph.add_node(node_1)
graph.add_node(node_2)
graph.add_node(node_3)
graph.add_node(node_4)
graph.add_node(node_5)
graph.add_node(node_6)
graph.add_node(node_7)
graph.add_node(node_8)
graph.add_node(node_9)
graph.add_node(node_10)
graph.add_node(node_11)


# for i in range(1,12):
    # x = graph.add_node("node_" + str(i))
    # print(x)




# create edges
graph.add_edge(pydot.Edge(node_1, node_2))
graph.add_edge(pydot.Edge(node_2, node_3))
graph.add_edge(pydot.Edge(node_2, node_4))
graph.add_edge(pydot.Edge(node_2, node_5))

graph.add_edge(pydot.Edge(node_3, node_6))
graph.add_edge(pydot.Edge(node_3, node_9))
graph.add_edge(pydot.Edge(node_4, node_7))
graph.add_edge(pydot.Edge(node_4, node_10))
graph.add_edge(pydot.Edge(node_5, node_8))
graph.add_edge(pydot.Edge(node_5, node_11))
graph.add_edge(pydot.Edge(node_9, node_2, label="alternatively go back to picking a topic", labelfontcolor="#009933", fontsize="10.0", color="blue"))

graph.write_png('C:/Users/User/Documents/file2.png')