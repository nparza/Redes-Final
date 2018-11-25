
'''
Ploteo en networkx de un grafo pesado. 
No usar para la red grande porque networkx es re pichi
'''

import networkx as nx
from matplotlib import pyplot as plt
from func import *
import numpy as np

#%%

userSGnx = nx.read_gml('userSubG.gml')
red = userSGnx

#%%

pos=nx.spring_layout(red) 
nx.draw_networkx_nodes(red,pos,node_color='green',node_size=50)
 
all_weights = []
#4 a. Iterate through the graph nodes to gather all the weights
for (node1,node2,data) in red.edges(data=True):
    all_weights.append(data['weight']) #we'll use this when determining edge thickness
 
#4 b. Get unique weights
unique_weights = list(set(all_weights))
 
#4 c. Plot the edges - one by one!
for weight in unique_weights:
    #4 d. Form a filtered list with just the weight you want to draw
    weighted_edges = [(node1,node2) for (node1,node2,edge_attr) in red.edges(data=True) if edge_attr['weight']==weight]
    #4 e. I think multiplying by [num_nodes/sum(all_weights)] makes the graphs edges look cleaner
    width = weight*red.number_of_nodes()*3.0/sum(all_weights)
    nx.draw_networkx_edges(red,pos,edgelist=weighted_edges,width=width)
 
#Plot the graph
plt.axis('off')
plt.title('Usuarios que watchean +70 repos en simultaneo')

plt.show() 
 
#%%


