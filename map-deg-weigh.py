# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 10:59:53 2018

@author: noelp
"""

import igraph as ig
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
import numpy as np
#%%

udg = ig.read('users-CG-undirected.gml')


#%%
#def dweight(graph, MODE = 3):
#    '''
#    graph: igraph graph
#    MODE: OUT = 1 ; IN = 2 ; ALL = 3
#    '''
#    weights = list()
#    for n in graph.vs:        
#        v = graph.neighbors(n, mode=MODE)
#        for i in v:
#            if MODE == 1:
#                weights.append(graph[n,i])    
#            if MODE == 2:
#                weights.append(graph[i,n])
#            if MODE == 3:
#                weights.append(graph[n,i])
#                weights.append(graph[i,n])
#    print('Mode %s' %MODE)
#    return weights
#%%
    
def dweight_node(graph,n, MODE = 3):
    '''
    graph: igraph graph
    MODE: OUT = 1 ; IN = 2 ; ALL = 3
    '''
    weights = list()        
    v = graph.neighbors(n, mode=MODE)
    for i in v:
        if MODE == 1:
            weights.append(graph[n,i])    
        if MODE == 2:
            weights.append(graph[i,n])
        if MODE == 3:
            weights.append(graph[n,i])
            weights.append(graph[i,n])

    return weights

def ave_weight(graph, MODE = 3):
    W = list()
    for n in graph.vs:
        W.append(np.average(dweight_node(graph,n, MODE = 3)))
    return W


#%%
deg = udg.indegree()
weights = ave_weight(udg, MODE = 2)

#%%

aweg = np.zeros(max(deg)+1)
norm = np.zeros(max(deg)+1)

for i in range(len(deg)):
    norm[deg[i]] += 1
    aweg[deg[i]] += weights[i]
    
awnorm = [aweg[i]/norm[i] for i in range(max(deg))]

for a in awnorm:
    if a == 0.0:
        awnorm.remove(a)
        
degidx = np.zeros(max(deg)+1)
for d in deg:
    if degidx[d] == 0.0:   
        degidx[d] = d

#%%
'''
3D Histogram
'''

# Fixing random state for reproducibility and construct hist
np.random.seed(19680801)
hist, xedges, yedges = np.histogram2d(deg, weights, bins=50, range=[[min(deg), max(deg)], [min(weights), max(weights)]])

#%%
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Construct arrays for the anchor positions of the 16 bars.
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Construct arrays with the dimensions for the 16 bars.
dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')

plt.show()

#%%
'''
Distribution log-log
'''
#plt.plot(degidx[1:],awnorm,'g.')
#

def applyPlotStyle(xname,yname):
    plt.xlabel(xname,weight='bold',fontsize=12)
    plt.ylabel(yname,weight='bold',fontsize=12)
    plt.gcf().set_size_inches([5, 4])
    plt.tight_layout()
    plt.show(block=False)
     
plt.figure(2)
plt.title('Mode: IN',loc='right',fontsize=10)
plt.title('Users deg-weight relation',loc='left',fontsize=10)
plt.loglog(degidx[1:],awnorm,'.')
applyPlotStyle('Degree','Weights') 

plt.gcf()
plt.savefig('user-wdeg-map.pdf', format='pdf',dpi=2000)
plt.gcf().get_size_inches()
#%%
'''

Heat plot ---> no funca aún

Correr primera celda de 3D Histogram

'''

# Make the plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(xedges, yedges, hist, cmap=plt.cm.viridis, linewidth=0.2)
plt.show()
 

# to Add a color bar which maps values to colors.
surf=ax.plot_trisurf(xedges, yedges, hist, cmap=plt.cm.viridis, linewidth=0.2)
fig.colorbar( surf, shrink=0.5, aspect=5)
plt.show()
