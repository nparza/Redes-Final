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
Lista posibles repos para remover de los watcheos de un user
'''

cg = ig.read('nets/repos-CG-undirected.gml')
posibles = list()

for v in cg.vs():
    if v['id'] in metadata:
        posibles.append(v['id'])      
del v

#%%

'''
Tengo matriz esparsa bipartita donde los repos son las filas.
Quiero sacar algunos watcheos. 
'''


















