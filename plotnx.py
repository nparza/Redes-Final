# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 10:32:34 2018

@author: noelp
"""

import networkx as nx
from matplotlib import pyplot as plt
from func import *
import numpy as np
#%%

userSGnx = nx.read_gml('userSubG.gml')

#%%

pos=nx.spring_layout(userSGnx) 
nx.draw_networkx_nodes(userSGnx,pos,node_color='green',node_size=50)
 
all_weights = []
#4 a. Iterate through the graph nodes to gather all the weights
for (node1,node2,data) in userSGnx.edges(data=True):
    all_weights.append(data['weight']) #we'll use this when determining edge thickness
 
#4 b. Get unique weights
unique_weights = list(set(all_weights))
 
#4 c. Plot the edges - one by one!
for weight in unique_weights:
    #4 d. Form a filtered list with just the weight you want to draw
    weighted_edges = [(node1,node2) for (node1,node2,edge_attr) in userSGnx.edges(data=True) if edge_attr['weight']==weight]
    #4 e. I think multiplying by [num_nodes/sum(all_weights)] makes the graphs edges look cleaner
    width = weight*userSGnx.number_of_nodes()*3.0/sum(all_weights)
    nx.draw_networkx_edges(userSGnx,pos,edgelist=weighted_edges,width=width)
 
#Plot the graph
plt.axis('off')
plt.title('Usuarios que watchean +70 repos en simultaneo')

plt.show() 
 
#%%


