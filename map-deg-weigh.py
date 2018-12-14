# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 10:59:53 2018

@author: noelp
"""

import igraph as ig
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib as mpl
#%%

udg = ig.read('users-CG-undirected.gml')

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
devwe = np.zeros(max(deg)+1)

for i in range(len(deg)):
    norm[deg[i]] += 1
    aweg[deg[i]] += weights[i]
    
awnorm = [aweg[i]/norm[i] for i in range(max(deg)+1)]
#
#for i in range(len(deg)):
#    devwe[deg[i]] += weights[i]-awnorm[deg[i]]
#
#devwe = [devwe[i]/(norm[i]-1) for i in range(max(deg)+1)]

for a in awnorm:
    if a == 0.0:
        awnorm.remove(a)
#        
#for d in devwe:
#    if a == 0.0:
#        devwe.remove(d)        
        
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
hist, xedges, yedges = np.histogram2d(deg, weights, bins=30, range=[[min(deg), max(deg)], [min(weights), max(weights)]])
xcenters = (xedges[1:]+xedges[:-1])/2
ycenters = (yedges[1:]+yedges[:-1])/2

#%%
fig = plt.figure(30)
ax = fig.add_subplot(111, projection='3d')

# Construct arrays for the anchor positions 
xpos, ypos = np.meshgrid(xedges[:-1], yedges[:-1], indexing="ij")
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
zpos = 0

# Construct arrays with the dimensions .
dx =  300 * np.ones_like(zpos)
dy = 0.01 * np.ones_like(zpos)
dz = hist.ravel()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average', shade=True)


#plt.gcf()
#plt.savefig('user-wdeg-hist.pdf', format='pdf',dpi=2000)
#plt.gcf().get_size_inches()


#%%
'''
Distribution log-log
'''

def applyPlotStyle(xname,yname):
    plt.xlabel(xname,weight='bold',fontsize=12)
    plt.ylabel(yname,weight='bold',fontsize=12)
    plt.gcf().set_size_inches([5, 4])
    plt.tight_layout()
    plt.show(block=False)
     
plt.figure(2)
lin1 = {'linestyle': 'None'} #No sé cómo funciona esto pero me saca la linea que une todos los errores
plt.rc('lines', **lin1) 
plt.title('Mode: IN',loc='right',fontsize=10)
plt.title('Users deg-weight relation',loc='left',fontsize=10)
plt.loglog(degidx,awnorm,'.')
#plt.errorbar(degidx, awnorm, devwe, xerr=None,  fmt='', capsize=3, ecolor ='seagreen' )
applyPlotStyle('Degree','Weights') 
plt.errorbar()
plt.gcf()
plt.savefig('user-wdeg-map.pdf', format='pdf',dpi=2000)
plt.gcf().get_size_inches()
#%%
'''

Heat plot ---> no funca aún

Correr primera celda de 3D Histogram

'''

# Make the plot
fig2 = plt.figure()
ax2 = fig2.gca(projection='3d')

# Make data.
Xcenters, Ycenters = np.meshgrid(xcenters, ycenters)

# Plot the surface.
#n = mpl.colors.Normalize(0,18000)

cmap = cm.coolwarm
cmap.set_under(color='b', alpha=0.0)
surf = ax2.plot_surface(Xcenters, Ycenters, hist, cmap=cmap,
                       linewidth=1000, antialiased=False)


# Add a color bar which maps values to colors.
fig2.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
