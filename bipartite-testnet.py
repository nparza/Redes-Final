import igraph as ig
from scipy.sparse import csr_matrix
import numpy as np
import pandas as pd

runfile('mapeo.py')

#%%

'''
CREO MATRIZ ESPARSA BIPARTITA
cargar peso, fila, col con loadcsv.py
bfila: repos, bcol: users
'''

bdata = [1]*len(bfila)
bip = csr_matrix((bdata, (bfila, bcol)), shape=(max(bfila)+1, max(bcol)+1))
        
del bdata
del bfila
del bcol

#%%

'''
Guardo en la lista 'metadata' los repos que tienen metadata
'''

entrada = open('contest/lang.txt')
lines = list()

for line in entrada:
    lines.append(line.split(':'))

noidxmeta = list()    
for line in lines:
    noidxmeta.append(int(line[0]))

noidxmeta.remove(59337)
noidxmeta.remove(95472)
noidxmeta.remove(80221)
noidxmeta.remove(73599)
noidxmeta.remove(24616)
metadata = list()
for i in range(len(noidxmeta)):
    metadata.append(repo2index(noidxmeta[i]))
    
del noidxmeta
del line
del lines
del entrada
del i

#%%

'''
Lista posibles repos para remover de los watcheos de un user, cumplen:
    - Están en la CG del grafo original de repos
    - Tienen metadata
'''

cg = ig.read('nets/repos-CG-undirected.gml')
posibles = list()

for v in cg.vs():
    if v['id'] in metadata:
        posibles.append(v['id'])      
del v


#%%


'''
Tengo matriz esparsa bipartita donde los repos son las filas y los users col.
Quiero sacar algunos watcheos de repos que tengan cierto grado en la matriz
bipartita.
'''

cgu = ig.read('nets/users-CG-undirected.gml')

def degreekbip()

def elige30(rango):
    '''
    Elige 30 users al azar cuyo grado en la bipartita esté en el rango 
    '''
    tochoose = list()
    
    for k in rango:
        vsk = cg.vs.select(_degree=k)
        for v in vsk:
            tochoose.append(v['id'])
    
    np.random.shuffle(tochoose)
    return tochoose[:30]
    

bines = [int(i) for i in np.logspace(np.log10(5),np.log10(300),20)]
torm = dict() 

for i in range(len(bines)-1):
   
    rango = np.arange(bines[i],bines[i+1])
    torm[i] = elige30(rango)
            
#%%    

'''
Me armo una lista con tuplas de (usuario, watcheo removido)
'''

removidos = list()

## En las filas están los indices de los repos, en las columnas los users
    
tnfila, tncol = bip.nonzero()

'''
Voy a usar algunas funciones de bipartite-projection.py
'''

## Sorteo de menor a mayor la lista tncol
## Col se sortea según fila

csort, fsort = zip(*sorted(zip(tncol, tnfila)))
tncol = list(csort); del csort
tnfila = list(fsort); del fsort

for l in list(torm.values()):
    for u in l:
        inicio, final = position(u, tncol, start=0)
        w = obtain(inicio, final, tnfila)
        np.random.shuffle(w)
        removidos.append((u,w[0]))
        print(bip[w[0],u])
        

#%%
        
        
        
        
        
