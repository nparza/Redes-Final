# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:37:02 2018

@author: noelp
"""

import networkx as nx
import pandas as pd

#%%
'''
Nodos: users
Enlaces: repositorio watcheado por el par de nodos
Peso: cantidad de repositorios watcheados por el par de nodos
'''

main = pd.read_csv('data/data.txt', delimiter=':')

userG = nx.Graph()

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



