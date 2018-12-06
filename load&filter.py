
import igraph as ig
import numpy as np

#%% 

'''
CARGO GRAFO USERS
'''

red = ig.read('users-CG-undirected.gml')

#%%

'''
CARGO GRAFO PRINCIPAL REPOS
'''

red = ig.read('repos-CG-undirected.gml')

#%%

'''
Remover enlaces con peso menor a un cierto umbral
'''

def filter_graph(red, umbral):
    
    red_filt = red.copy()
    eliminar = []
    for idx, e in enumerate(red_filt.es):
        if e['weight'] < umbral:
            eliminar.append(idx)

    red_filt.delete_edges(eliminar)
    
    return red_filt, eliminar
    
red_filt, eliminados = filter_graph(red, 0.001)

#%%