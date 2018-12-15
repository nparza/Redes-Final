
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

<<<<<<< HEAD
uwij = csr_matrix((peso, (fila, col)), shape=(max(fila)+1, max(col)+1))
=======
rwij = csr_matrix((rpeso, (rfila, rcol)), shape=(max(rfila)+1, max(rcol)+1))
>>>>>>> 0f85ba9e9ccdc07bee60773c2a7a5533f01f194e
        
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

<<<<<<< HEAD
ig.write(g,'forks-directed.gml')  
ig.write(g2, 'users-undirected.gml')
=======
#ig.write(g,'users-directed.gml')  
ig.write(rcg, 'repos-CG-undirected.gml')
>>>>>>> 223870946b8243d9fcad6eb1e1904594f77d1ea7

