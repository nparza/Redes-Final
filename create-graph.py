
import igraph as ig
from scipy.sparse import csr_matrix
from datetime import datetime as dt

'''
nececisto la matriz de adyacencia pesada wij
'''

#%%

'''
CREO MATRIZ PESOS
cargar upeso, ufila, ucol con loadcsv.py
'''

rwij = csr_matrix((rpeso, (rfila, rcol)), shape=(max(rfila)+1, max(rcol)+1))
        
del rpeso
del rfila
del rcol

#%%

'''
DIRIGIDO
filas: targets, columnas: sources, por cómo calculamos la matriz pesos
'''

t0 = dt.now()

targets, sources = uwij.nonzero()
edgelist = list(zip(sources.tolist(), targets.tolist()))

timear(t0, 'arranca')

g = ig.Graph(edgelist, directed=True)

timear(t0, 'rmloops()')
rmloops(g)
timear(t0, 'fin')

#%%

'''
NO DIRIGIDO - PESO PROMEDIO
'''

g2 = g.copy()   
g2.to_undirected(mode='collapse', combine_edges='mean')


#%% 

## EDGES

idxi = 0
idxf = 7

print('NO DIRIGIDO')
for idx, e in enumerate(g2.es[idxi:idxf]):
    print(idx, e.tuple, e['weight'])   

print('DIRIGIDO')    
for idx, e in enumerate(g.es[idxi:idxf]):
    print(idx, e.tuple, e['weight'])    

#%%

'''
GUARDAR
'''  

ig.write(g,'forks-directed.gml')  
ig.write(g2, 'users-undirected.gml')

