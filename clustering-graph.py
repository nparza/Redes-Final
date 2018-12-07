# -*- coding: utf-8 -*-

import igraph as ig

#%%
'''
CARGO GRAFO PRINCIPAL REPOS DIRECTED
rdg: repos directed graph
rdw: repos directed weights
'''
rdg = ig.read('repos-directed.gml')
rdw = [rdg.es[n]['weight'] for n in range(rdg.ecount())]

#%%
'''
CARGO GRAFO PRINCIPAL USERS DIRECTED
udg: users directed graph
udw: users directed weights
'''
udg = ig.read('users-directed.gml')
udw = [udg.es[n]['weight'] for n in range(udg.ecount())]

#%%
'''
CARGO GRAFO PRINCIPAL REPOS UNDIRECTED
rdg: repos directed graph
rdw: repos directed weights
'''
rg = ig.read('repos-undirected.gml')
rw = [rg.es[n]['weight'] for n in range(rg.ecount())]
rcg = rg.components().giant()

#%%

''' 
CALCULO CLUSTERS CON INFOMAP
udv/rdv creo que es una lista de listas donde cada lista es una comunidad 
'''

udvc = udg.community_infomap(edge_weights=udw, vertex_weights=None, trials=10)
#rdvc = rdg.community_infomap(edge_weights=rdw, vertex_weights=None, trials=10)

'''
Ir a savecsv.py y guardar!
Los clusters con infomap se hicieron al grafo TOTAL dirigido 
'''

#%%




#%%

'''
CREO OBJETO VERTEX CLUSTERING (que es lo que me devuelve la función community)
A partir de:
    - lista membership
    - grafo
'''

#udvc2 = ig.VertexClustering(udg, membership = membership)
rdvc = ig.VertexClustering(rdg, membership = membership)

#%%

#sizesu = sorted(list(udvc.sizes()))
sizesr = sorted(list(rdvc.sizes()))
