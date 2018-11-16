# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 01:58:23 2018

@author: noelp
"""

import igraph as ig

vertices = []
for n in range(red.ecount()):
    if red.es[n]['weight'] > 50:
        vertices.append(red.es[n].tuple[0])
        vertices.append(red.es[n].tuple[1])
        

userSubG = red.subgraph(vertices, implementation="auto")
ig.write(userSubG,'userSubG.gml')
#%%

userSGig = ig.read('userSubG.gml')
weights =[userSGig.es[n]['weight'] for n in range(userSGig.ecount())]
#%%

kmax=max(weights)
N=userSGnx.number_of_edges()

K=dict()

for i in set(listk):
    K[i]=0

for k in listk:
    K[k]+=1

k=list(K.keys())    
pk=np.array(list(K.values()))/N

n=14
bins=np.logspace(0,np.log10(kmax+1),n)
h,bins=np.histogram(listk,bins)

centros=[]
for i in range(len(bins)-1):
    c=(bins[i]+bins[i+1])/2
    centros.append(c)

A=[]
for i in range(len(h)):
    A.append(h[i]/(bins[i+1]-bins[i]))
pk_log=A/sum(A)

plt.plot(k,pk,'.')
#plt.plot(centros,pk_log,'.')
applyPlotStyle('k','pk')
plt.show()