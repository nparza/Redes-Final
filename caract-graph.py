
from matplotlib import pyplot as plt
import numpy as np
import igraph as ig

#%% 

'''
CARGO GRAFO PRINCIPAL USERS
ugd: users directed graph
ug: users graph
'''

ug = ig.read('users-undirected.gml')
udg = ig.read('users-directed.gml')

#%%

'''
CARGO GRAFO PRINCIPAL REPOS
ugd: users directed graph
ug: users graph
'''

rg = ig.read('repos-undirected.gml')
rdg = ig.read('repos-directed.gml')

#%%

#red = rg
#dred = rdg
#red = rg.components().giant()

#red = ug
dred = udg
red = ug.components().giant()

#%%%
'''
CARACTERIZACIÓN
no dirigida
'''

def caract(red):
    
    deg = red.degree()
    wei = [red.es[n]['weight'] for n in range(red.ecount())]
    densidad = red.ecount()/(red.vcount()*(red.vcount()-1)/2)
    
    print('Caracerísticas estructurales ')
    print('Nodos:', red.vcount(),'Edges:', red.ecount())
    print('k medio:', np.mean(deg), 'kmax:', max(deg), 'kmin:', min(deg))
    print('Densidad:', densidad)
    print('Average weight:',np.average(wei))
    print('Cant. componentes:', red.components().__len__())
    print('Nodos comp. gigante:', red.components().giant().vcount())
    print('Porción que representa la CG:', 
          red.components().giant().vcount()/red.vcount())
    

#clustg = red.transitivity_avglocal_undirected(weights=weights)

#%% 
'''
CARACTERIZACIÓN
dirigida
'''

deg = dred.degree(); indeg = dred.indegree(); outdeg = dred.outdegree(); 
wei = [dred.es[n]['weight'] for n in range(dred.ecount())]
densidad = dred.ecount()/(dred.vcount()*(dred.vcount()-1)/2)
#clustg = dred.transitivity_avglocal_undirected(weights=weights)

#%%
'''
CARACTERIZACIÓN
no dirigida
'''
    
print('Caracerísticas estructurales ')
print('Nodos:', red.vcount(),'Edges:', red.ecount())
print('k medio:', np.mean(deg), 'kmax:', max(deg), 'kmin:', min(deg))
print('Densidad:', densidad)
print('Average weight:',np.average(wei))
print('Cant. componentes:', red.components().__len__())
#print('Transitividad:', clustg)

#%%
'''
Caracerísticas estructurales
dirigida
'''
    
print('Caracerísticas estructurales ')
print('Nodos:', dred.vcount(),'Edges:', dred.ecount())
print('k medio:', np.mean(deg), 'kmax:', max(deg), 'kmin:', min(deg))
print('k medio in:', np.mean(indeg), 'k medio out:', np.mean(outdeg))
print('Densidad:', densidad)
print('Average weight:',np.average(wei))
#print('Transitividad:', clustg)


#%%
'''
ENLACES
Imprime los enlaces con ID de idxi a idxf
'''

idxi = 100
idxf = 107

print('NO DIRIGIDO')
for idx, e in enumerate(red.es[idxi:idxf]):
    print(idx+idxi, e.tuple, e['weight'])   

print('DIRIGIDO')    
for idx, e in enumerate(dred.es[idxi:idxf]):
    print(idx+idxi, e.tuple, e['weight'])   


#%%

'''
VERTICES
'''

idxi = 0
idxf = copy.vcount()

print('NO DIRIGIDO')
for v in copy.vs[idxi:idxf]:
    if v['id'] == 8:
        print(v['id'])   
    





