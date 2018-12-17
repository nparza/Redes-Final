# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 19:32:09 2018

@author: noelp
"""

import pandas as pd
from datetime import datetime as dt
import numpy as np

#%%


main = pd.read_csv('contest/repos.txt', sep=':|,')
langs = pd.read_csv('contest/lang.txt', sep=':')

#### Hay 93k repos que fueron forkeados de algún lugar.

#%% Veamos los baches

#bache = list()
#t0 = dt.datetime.now()
#for i in range(1, main['repo'].shape[0]-1):
#    if main['repo'][i-1] != main['repo'][i]-1:
#        bache.append((i,main['repo'][i]))
#    if i == int(main['repo'].shape[0]*0.25):
#        print('25%', dt.datetime.now()-t0)
#    if i == int(main['repo'].shape[0]*0.5):
#        print('50%', dt.datetime.now()-t0)
#    if i == int(main['repo'].shape[0]*0.75):
#        print('75%', dt.datetime.now()-t0)
#
#print('Baches',len(bache))

#%% Mi matriz va a tener las mismas filas y columnas

repo = list(set(main['repo']))
r = range(len(repo))

def repo2index(a):
        return r[repo.index(a)]



def strseparator(string, sep1=',',sep2=';'):
    elements = dict()
    lines = string.split(sep1)
    for m in lines:
        elements[m.split(sep2)[0]] = m.split(sep2)[1]
    return elements

def timer(i,count = main['repo'].shape[0]):
    if i ==1:
        print('Primera iteración', dt.now()-t0)                        
    if i ==int(count*0.1):
        print('10%', dt.now()-t0)
    if i == int(count*0.25):
        print('25%', dt.now()-t0)
    if i == int(count*0.5):
        print('50%', dt.now()-t0)
    if i == int(count*0.75):
        print('75%', dt.now()-t0)
    if i == int(count*0.99):
        print('99%', dt.now()-t0)



#%%

## Creo los elementos de mi matriz esparza


col = list() ##Repos hijos
fila = list() ##Repos padres


t0 = dt.now()
for i in range(main.iloc[-1].name + 1):
    a = main.iloc[i]
    l = langs.loc[langs['repo'] == a.repo]
    if np.isnan(a.forked) != True and l.empty != True:
        fila.append(repo2index(a.repo))
        col.append(repo2index(a.forked))
        metadata = strseparator(l.iloc[0].lan)
        name.append(a.repo)

data = np.ones(len(col))

#%%
uwij = csr_matrix((data, (fila, col)), shape=(max(fila)+1, max(col)+1))

targets, sources = uwij.nonzero()
edgelist = list(zip(sources.tolist(), targets.tolist()))
g = ig.Graph(edgelist, directed=True)
ig.write(g,'forks-directed.gml')  

#%%
##%%
#'''
#Load graph, ya está creado con el script create-graph.py
#Para correr create-graph.py corré func-igraph.py
#'''
#
#gtree = ig.read('forks-directed.gml')
#
##%%
#
### voy a ver qué onda las componentes del wacho
#
#gcomps = gtree.components(mode=1)
#sizes = gcomps.sizes()
#hist = list(gcomps.size_histogram(bin_width=1).bins())
#binedges = [hist[n][0] for n in range(len(hist))]
#freq = [hist[n][2] for n in range(len(hist))]
#
#plt.plot(binedges,freq,'.')
#



#%%

bound = 10

houses = dict()
for c in range(len(gcomps)):
    count = 0
    if sizes[c] >= bound:
        houses[str(count)] = gtree.subgraph(gcomps[c], implementation="auto") 
        count += 1
        











