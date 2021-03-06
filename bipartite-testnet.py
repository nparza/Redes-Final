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
for line in lines[1:]:
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
del metadata


#%%

'''
Tengo matriz esparsa bipartita donde los repos son las filas y los users col.
Quiero sacar algunos watcheos de usuarios que tengan cierto grado en la matriz
bipartita.
'''

'''
Tengo 29 bines, me guardo en un diccionario los usuarios que tienen 
grado perteneciente a cada bin. Los bines van de grado 3 inclusive a 
grado 300 inclusive.
'''

bines = [3,4,5,6,7,8,9] + \
        [int(i) for i in np.logspace(np.log10(10),np.log10(301),23)]
        
kubip = dict()
for i in range(len(bines)-1):
    kubip[i] = []

def eligebin(n,bines):
    j = 0
    while j < len(bines)-1:
        if n >= bines[j] and n < bines[j+1]:
            return j
        j += 1
    
for i in range(bip.shape[1]):
    
    if bip[:,i].getnnz() > 2 and bip[:,i].getnnz() < 301:
        kubip[eligebin(bip[:,i].getnnz(),bines)].append(i)
        
            
#%%    

'''
Me armo una lista con tuplas de (usuario, watcheo removido)
'''

urm = list()
wrm = list()

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

## Shuffleo las listitas de kubip

for key in kubip.keys():
    value = kubip[key]
    np.random.shuffle(value)
    kubip[key] = value
    
## value es la lista de users cuyo grado cae dentro de un bin
for key, v in kubip.items():
    
    i = 0
    ## l[i] es un usuario con grado dentro de un determinado bin
    ## j me va a indicar a cuantos usuarios les elegí un watcho para remover
    j = 0
    
    while i < len(v) and j < len(v) and j < 30:
            
        inicio, final = position(v[i], tncol, start=0)
        w = obtain(inicio, final, tnfila)
        np.random.shuffle(w)
        
        ## Voy a pedir que el repo que le remuevo tenga grado al menos 
        ## 2 en la bipartita y que además no lo haya removido de un watcheo
        ## en alguna iteración anterior
        if key < 22:
            
            m = 0
            ok = False
            
            while not ok and m < len(w) and j < len(v) and j < 30:
                
                repito = w[m]
                ok = bip[repito,:].getnnz() > 1 and (repito not in wrm)
                m += 1
            
            if ok:
                urm.append(v[i])
                wrm.append(repito)
                j += 1 
        
        ## Si el user watchea a más de 100 repos, voy a pedir que el repo que
        ## remuevo, además, esté en la lista 'posibles'
        else:
            
            m = 0
            ok = False
            
            while not ok and m < len(w) and j < len(v) and j < 30:
                
                repito = w[m]
                ok = (repito in posibles) \
                and (bip[repito,:].getnnz() > 1) and (repito not in wrm)
                m += 1  
                    
            if ok:
                urm.append(v[i])
                wrm.append(repito)
                j += 1
        
        i += 1
        print(len(urm),j)


del key,value,inicio,final,w,repito,m,i,ok,v,j
        
#%%
        
'''
Testeo no estar dejando en cero el grado de un repo en la bipartita o no 
haber sacado el watcheo de un mismo repo
'''

wrms = sorted(wrm) 

for r in set(wrm):
    
    inicio, final = position(r,wrms)
    apariciones = final - inicio + 1
    
    if bip[r,:].getnnz() <= apariciones:
        print(r, bip[r,:].getnnz(), apariciones)

del inicio, final, apariciones, r

for i in range(len(wrms)-1):
    if wrms[i] == wrms[i+1]:
        print(True)
        
del wrms, i

'''
Si no printea nada, está todo bien!
'''    
        
#%%        

'''
Remuevo los ínidies de tncol y tnfila correspondientes 
a los watcheos elegidos.
tncol debe estar sorteada (usuarios) y tnfila (repos) sorteada según tncol
'''

indextorm = list()

def widxtorm(w,inicio,final,repos):
    
    j = inicio
    while j < final + 1:
        if repos[j] == w:
            return j
        j += 1
    
for i in range(len(urm)):
    
    inicio, final = position(urm[i],tncol)
    indextorm.append(widxtorm(wrm[i],inicio,final,tnfila))


for i in sorted(indextorm, reverse=True):
    del tncol[i]
    del tnfila[i]
    
del i, inicio, final


#%%

'''
Chequeo que removí bien
'''

l_bfila = list(bfila)
l_tnfila = list(tnfila)

for i in range(len(wrm)):
    
    if l_bfila.count(wrm[i]) - l_tnfila.count(wrm[i]) != 1:
        print('Fail')
    
del l_bfila, l_tnfila, i    

'''
Si no printea nada, cool
'''
        
#%%   
 
'''
Guardar tnfila correspondiente a repos y tncol correspondiente a users
en un csv!
'''

