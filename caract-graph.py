
'''
Descomentá el subgrafo que queres caracterizar y tamo

-Distribución de grado o de peso, según prefieras
-Características estructurales (N,L,<k>,densidad, <C>, etc.)
'''


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

red = rg
dred = rdg

#%%

## EDGES

idxi = 100
idxf = 107

print('NO DIRIGIDO')
for idx, e in enumerate(red.es[idxi:idxf]):
    print(idx+idxi, e.tuple, e['weight'])   

print('DIRIGIDO')    
for idx, e in enumerate(dred.es[idxi:idxf]):
    print(idx+idxi, e.tuple, e['weight'])   

#%%%
'''
COEFICIENTES Y GRADO
no dirigida
'''

deg = red.degree()
weights = [red.es[n]['weight'] for n in range(red.ecount())]
densidad = red.ecount()/(red.vcount()*(red.vcount()-1)/2)
clustg = red.transitivity_avglocal_undirected(weights=weights)

#%%
'''
Distribución logarítmica de grado o peso del grafo
no dirigida
'''

k,pk,centros,pk_log, sumA = logdist(red.degree(), red.vcount(), n=90)

plt.figure(2)
plt.title('Log-Log Scale, Log Binning',loc='left',fontsize=10)
plt.loglog(k,pk,'.',color='0.9')
plt.loglog(centros,pk_log,'.')
applyPlotStyle('k',r'p$_k$') 
#applyPlotStyle('w',r'p$_w$')
plt.show()


#%%
'''
Caracerísticas estructurales
'''
    
print('Caracerísticas estructurales')
print('Nodos:', red.vcount(),'Edges:', red.ecount())
print('k medio:', np.mean(deg), 'kmax:', max(deg), 'kmin:', min(deg))
print('Densidad:', densidad)
print('Average weight:',np.average(weights))
print('Transitividad:', clustg)

 
