# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:02:57 2020

@author: User
"""
import pydot

graph = pydot.Dot(graph_type='digraph')

## creating nodes for bot ouput

node_a = pydot.Node("Initiate Introduction \n\
                    Output 'What is your name?'", style="filled", fillcolor="purple", shape = 'box')
# example: what is your name? how are you?
node_b = pydot.Node("Let participant pick a topic \n\
                    'Output 'Please pick a topic below.'", style="filled", fillcolor="blue", shape = 'box')
# example: curse with jordan, hold small-talk with jordan
node_c = pydot.Node("Initiate Example Topic \n\
                    Output 'Small-talk with Jordan'", style="filled", fillcolor="green", shape = 'box')
node_c1 = pydot.Node("Initiate Example Topic \n\
                     Output 'Cursing with Jordan'", style="filled", fillcolor="green", shape = 'box')
node_c2 = pydot.Node("Initiate Example Topic \n\
                     Output 'Complain about quarantine'", style="filled", fillcolor="green", shape = 'box')
# example: Ok, you chose Example Topic. Why dont you start by telling me why you chose this topic?
node_d = pydot.Node("Maintain Conversation \n\
                    Output 'Tell me more.'", style="filled", fillcolor="orange", shape = 'box')
node_d1 = pydot.Node("Maintain Conversation \n\
                    Output 'Tell me more.'", style="filled", fillcolor="orange", shape = 'box')
node_d2 = pydot.Node("Maintain Conversation \n\
                    Output 'Tell me more.'", style="filled", fillcolor="orange", shape = 'box')
# example: Open questions and fillers in that class of that specific example topic - Tell me more! How did that happen? I understand. 
node_e = pydot.Node("End Conversation \n\
                    Output 'Thank you for trusting me. Do you want to pick another topic or do you want to say goodbye?'", style="filled", fillcolor="yellow", shape = 'box')
node_e1 = pydot.Node("End Conversation \n\
                    Output 'Thank you for trusting me. Do you want to pick another topic or do you want to say goodbye?'", style="filled", fillcolor="yellow", shape = 'box')
node_e2 = pydot.Node("End Conversation \n\
                    Output 'Thank you for trusting me. Do you want to pick another topic or do you want to say goodbye?'", style="filled", fillcolor="yellow", shape = 'box')
# example: Ok, you wanted to end this conversation. Do you want to choose another topic?


# creating nodes for participants response

# add nodes
graph.add_node(node_a)
graph.add_node(node_b)
graph.add_node(node_c)
graph.add_node(node_c1)
graph.add_node(node_c2)
graph.add_node(node_d)
graph.add_node(node_d1)
graph.add_node(node_d2)
graph.add_node(node_e)
graph.add_node(node_e1)
graph.add_node(node_e2)



# create edges
graph.add_edge(pydot.Edge(node_a, node_b))
graph.add_edge(pydot.Edge(node_b, node_c))
graph.add_edge(pydot.Edge(node_b, node_c1))
graph.add_edge(pydot.Edge(node_b, node_c2))

graph.add_edge(pydot.Edge(node_c, node_d))
graph.add_edge(pydot.Edge(node_c, node_e))
graph.add_edge(pydot.Edge(node_c1, node_d1))
graph.add_edge(pydot.Edge(node_c1, node_e1))
graph.add_edge(pydot.Edge(node_c2, node_d2))
graph.add_edge(pydot.Edge(node_c2, node_e2))
graph.add_edge(pydot.Edge(node_e, node_b, label="alternatively go back to picking a topic", labelfontcolor="#009933", fontsize="10.0", color="blue"))

graph.write_png('C:/Users/User/Documents/file2.png')