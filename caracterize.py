# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 15:07:54 2018

@author: noelp
"""
import pandas as pd
from func import *
from matplotlib import pyplot as plt
import numpy as np
import igraph as ig
#%%

userG = ig.read('C:/Users/noelp/Documents/Git/Redes-TPFinal-Grafos/userG.gml')

red = userG
#%%
'''
Distribución de grado del grafo
'''

listk=red.degree()
kmax=max(listk)
N=red.vcount()


K=dict()

for i in set(listk):
    K[i]=0

for k in listk:
    K[k]+=1

k=list(K.keys())    
pk=np.array(list(K.values()))/N


n=14
#bins=np.logspace(0,np.log10(kmax+1),n)
h,bins=np.histogram(listk, bins=n)
centros=[]
for i in range(len(bins)-1):
    c=(bins[i]+bins[i+1])/2
    centros.append(c)

A=[]
for i in range(len(h)):
    A.append(h[i]/(bins[i+1]-bins[i]))
pk_log=A/sum(A)


plt.loglog(k,pk,'.')
#plt.loglog(centros,pk_log,'.')
applyPlotStyle('degree','densidad')
plt.show()

#%% Calculo valores de la tabla


nodes=[]; edges=[]; kmedio=[]; kmax=[]; kmin=[]; densidad=[]
clustg=[]; weight = []

weights=[red.es[n]['weight'] for n in range(red.ecount())]

nodes.append(red.vcount())
edges.append(red.ecount())
k=red.degree()
kmedio.append(np.mean(k))
kmax.append(max(k))
kmin.append(min(k))
densidad.append(red.ecount()/(red.vcount()*(red.vcount()-1)/2))
#clustg.append(red.transitivity_avglocal_undirected(weights=weights))
weight.append(np.average(weights))
    

    
#%% Grafico tabla

caract = pd.DataFrame({ 'red':['usersG'], 
                        'N':nodes,
                        'L':edges,
                        'k_medio':kmedio,
                        'k_max':kmax,
                        'k_min':kmin,

                      })

caract = caract[['red','N','L','k_medio',
                 'k_max','k_min']]

#Uso cols para copiar y pegar y hacer más rapido la redefinición de lugares
cols=list(caract.columns.values)

print(caract)
