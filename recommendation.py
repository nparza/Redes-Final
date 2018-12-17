#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from scipy.sparse import csr_matrix

#%%

'''
CARGO MATRIZ PESOS TESTNET
cargar peso, rfila, rcol con loadcsv.py
'''

wij = csr_matrix((peso, (rfila, rcol)), shape=(max(rfila)+1, max(rcol)+1))
        
del peso
del rfila
del rcol

#%%

'''
CARGO MATRIZ BIPARTITA TESTNET
fila, col con loadcsv.py donde fila es repo, columna usuario
'''

data = [1]*len(fila)

bip = csr_matrix((data, (fila, col)), shape=(max(fila)+1, max(col)+1))

#%%

'''
CARGO WATCHEOS REMOVIDOS con loadcsv.py
Tengo que tener dos listas: urm, wrm
'''

#%%

def chequeo(bip, urm, wrm):
    
    for i in range(len(urm)):  
       
        if bip[wrm[i],urm[i]] == 1:
           return 'Falla'
    
    return 'Todo ok'
    

def scores(user, bip, wij):
    
    '''
    Calcula el score de cada repo para recomendarle al user y los ordena de 
    mayor a menor.
    Requiere:
        - 'user' es el id del usuario al que quiero recomendarle repos.
        - 'wij' es la matriz esparza de pesos que sale de la proyección 
        de la matriz bipartita al espacio de los repositorios.
    Devuelve: 
        - lista con scores sorteada de mayor a menor.
        - lista con repos correspondientes a cada score.
    '''
    
    uvect = bip[:,user].toarray()
    res = list(wij @ uvect)
    
    for i in range(len(res)):
        res[i] = float(res[i])
    
    repos = list(np.arange(0,len(res)))
    yawatcheados = list()
    
    for i in range(len(uvect)):
        if uvect[i] == 1:
            yawatcheados.append(i)
    
    for i in sorted(yawatcheados, reverse=True):
        del repos[i]
        del res[i]
    
    ## Sorteo de mayor a menor la lista res
    ## repos se sortea según res
    
    resort, reposort = zip(*sorted(zip(res, repos), reverse=True))
    res = list(resort); del resort
    repos = list(reposort); del reposort
    
    return repos, res


def rank_position(rank, scores, repo):
    
    '''
    Devuelve la posición en el ranking del repo y su score. 
    Si no está en el ranking devuelve nan value.
    '''
    
    for i in range(len(rank)):
        
        if rank[i] == repo:
            return i+1, scores[i]
    
    return np.nan, np.nan

#%%
    
posicion = []
grado = []
puntaje = []

for i in range(len(urm)):

    u = urm[i]
    w = wrm[i]
    
    rank, s = scores(u, bip, wij)
    pos, score = rank_position(rank, s, w)
    
    grado.append(bip[:,u].getnnz())
    posicion.append(pos)
    if max(s) != 0:
        puntaje.append((score/max(s))*10)
    else:
        puntaje.append(0)
    

#print('El repo ', w, ' está en la posición ', pos, ' con score ', 
#      (score/max(s))*10, ' para ser recomendado al user ', u)
        
del i, u, w, rank, s, pos, score

#%%

def sort(l1, l2, r=False):
    
    l1s, l2s = zip(*sorted(zip(l1, l2), reverse=r))
    l1 = list(l1s)
    l2 = list(l2s)
    
    return l1, l2
    
sgrado, sposicion = sort(grado, posicion)
sgrado, spuntaje = sort(grado, puntaje)

#%%


def applyPlotStyle(xname,yname):
    plt.xlabel(xname,weight='bold',fontsize=12)
    plt.ylabel(yname,weight='bold',fontsize=12)
    plt.gcf().set_size_inches([5, 4])
    plt.tight_layout()
    plt.show(block=False)

plt.figure(23)
#plt.title('DISTRIBUCIÓN DE GRADO',loc='left',fontsize=10)
plt.plot(grado,posicion,'.')
plt.grid(color='0.9')
applyPlotStyle('cant. de watcheos','posición de recomendación')    

#%%

i = 660

plt.figure(50)
#plt.title('DISTRIBUCIÓN DE GRADO',loc='left',fontsize=10)
plt.plot(sgrado[i:],sposicion[i:],'.')
plt.grid(color='0.9')
plt.ylim([-100,2000])
applyPlotStyle('cant. de watcheos','posición de recomendación')  


#%%
'''
Distribución logarítmica de RECOMENDACION
'''

i = 660
k, pk, centros, pk_log= logdist(sposicion[i:], len(sposicion[i:]), n=25)

#%%%

plt.figure(3)
plt.title('Log Binning',loc='right',fontsize=10)
plt.title('DIST. DE POSICIONES EN RANKING',loc='left',fontsize=10)
#plt.loglog(k,pk,'.',color='0.9')
plt.plot(centros,pk_log,'.')
applyPlotStyle('posición de recomendación','probabilidad posicion de rec.')
plt.grid(color='0.9')
plt.xlim([-100,500])
plt.show()

#plt.savefig('grado-bip-repos.png', format='png',dpi=2000)

