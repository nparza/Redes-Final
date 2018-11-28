
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

uwij = csr_matrix((upeso, (ufila, ucol)), shape=(max(ufila)+1, max(ucol)+1))
        
del upeso
del ufila
del ucol

#%%

'''
DIRIGIDO
filas: targets, columnas: sources, por cómo calculamos la matriz pesos
'''

t0 = dt.now()

targets, sources = uwij.nonzero()
edgelist = list(zip(sources.tolist(), targets.tolist()))

timear(t0, 'arranca')
g = ig.Graph(edgelist, directed=True, 
             edge_attrs={'weight': uwij.data.tolist()})

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

ig.write(g,'users-directed.gml')  
ig.write(g2, 'users-undirected.gml')

