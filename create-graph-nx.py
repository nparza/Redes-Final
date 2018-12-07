# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:37:02 2018

@author: noelp
"""


import pandas as pd
import networkx as nx
from scipy.sparse import csr_matrix
from datetime import datetime as dt
import numpy as np
#%%
main = pd.read_csv('data/data.txt', delimiter=':')

#%%
'''
Nodos: users
Enlaces: repositorio watcheado por el par de nodos
Peso: cantidad de repositorios watcheados por el par de nodos
'''

for r in pd.unique(main['repo']):
    matches = main['user'].loc[main['repo']==r]
    userG.add_nodes_from(matches)
    for i in matches:
        for j in matches:
            if j<i:
                if userG.has_edge(i,j) == False:
                    userG.add_edge(i,j,weight=1)
                else:
                    userG[i][j]['weight'] +=1
            
nx.write_gml(userG, 'userG.gml.gz', stringizer=None)

#%%
'''DIRIGIDO'''

'''
CREO MATRIZ PESOS
cargar peso, fila, col con loadcsv.py
'''

wij = csr_matrix((np.ones(len(fila)), (fila, col)), shape=(max(fila)+1, max(col)+1))
        
del fila
del col

#%%

t0 = dt.now()
targets, sources =wij.nonzero()
edgelist = list(zip(sources.tolist(), targets.tolist()))

G = nx.DiGraph()
timear(t0, 'arranca')
G.add_edges_from(edgelist)
timear(t0, 'fin')



