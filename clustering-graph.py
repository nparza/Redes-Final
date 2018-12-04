# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 15:14:51 2018

@author: noelp
"""

import igraph as ig

#%%
'''
(1) Corré esto 

'''



'''
CARGO GRAFO PRINCIPAL USERS
rdg: repos directed graph
rdw: repos directed weights
'''
rdg = ig.read(r'C:\Users\noelp\Documents\Git\Redes-TPFinal-Grafos\Grafos\directed-users-002.gml')
rdw = [udg.es[n]['weight'] for n in range(rdg.ecount())]

#%%

'''
CARGO GRAFO PRINCIPAL USERS
udg: users directed graph
udw: users directed weights
'''
udg = ig.read(r'C:\Users\noelp\Documents\Git\Redes-TPFinal-Grafos\Grafos\directed-users-002.gml')
udw = [udg.es[n]['weight'] for n in range(udg.ecount())]

#%%
'''
Corré esto
'''
''' 
Clusterizo
udv creo que es una lista de listas donde cada lista es una comunidad 
'''

#udv = udg.community_infomap(edge_weights=udw, vertex_weights=None, trials=10)
rdv = rdg.community_infomap(edge_weights=rdw, vertex_weights=None, trials=10)
#%%

'''
Después me fijo cómo guardarlo
'''