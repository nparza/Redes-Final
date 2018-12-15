
import igraph as ig
import numpy as np

#%% 

'''
CARGO GRAFO USERS
'''

redu = ig.read('users-CG-undirected.gml')

#%%

'''
CARGO GRAFO PRINCIPAL REPOS
'''

redr = ig.read('repos-CG-undirected.gml')

#%%

'''
Remover enlaces con peso menor a un cierto umbral
'''

def filter_graph(red, umbral):
    '''
    Devulve un nuevo grafo con los enlaces removidos y un lista con
    los id de los enlaces eliminados
    '''
    red_filt = red.copy()
    eliminar = []
    for idx, e in enumerate(red_filt.es):
        if e['weight'] < umbral:
            eliminar.append(idx)

    red_filt.delete_edges(eliminar)
    
    return red_filt, eliminar
    

red_filt, eliminados = filter_graph(red, 0.001)


#%%