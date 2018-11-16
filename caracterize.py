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

userG = ig.read('Grafos/userG.gml')

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


plt.loglog(k,pk,'.',color='0.9')
plt.loglog(centros,pk_log,'.')
applyPlotStyle()
plt.show()

#%% Calculo valores de la tabla


nodes=[]; edges=[]; kmedio=[]; kmax=[]; kmin=[]; densidad=[]
#clustl=[]; clustg=[]; ; diam=[];



nodes.append(red.vcount())
edges.append(red.ecount())
k=red.degree()
kmedio.append(np.mean(k))
kmax.append(max(k))
kmin.append(min(k))
#densidad.append(edges/(nodes*(nodes-1)/2))
#compgigante=max(nx.connected_component_subgraphs(red),key=len)
#diam.append(nx.diameter(compgigante))
#clustl.append(nx.average_clustering(red))
#clustg.append(nx.transitivity(red))
    

    
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
