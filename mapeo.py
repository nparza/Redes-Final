## LIBRERIAS

import pandas as pd

## CARGO EL MAIN TXT

main = pd.read_csv('data/data.txt', delimiter=':')


## MAPEO INDICE-ID Y VICEVERSA

# list with ID   
user = list(set(main['user']))
repo = list(set(main['repo']))

# list with index
ui = range(len(user))
ri = range(len(repo))

def usr2index(a):   
    return ui[user.index(a)]

def index2usr(a):
    return user[ui.index(a)]

def repo2index(a):
    return ri[repo.index(a)]

def index2repo(a):
    return repo[ri.index(a)]
    
    
#%%

'''
CALCULO MATRIZ DE ADYACENCIA RED BIPARTITA
A continuación creo las listas para la matriz esparsa de la red bipartita
Asumimos que la lista data es [1,1,..,1]
'''

'''
Estas dos listas ya están guardadas en bipartite.csv
Para cargarlas usar loadcsv.py
'''

# índices de los usuarios
fila = list()

# índices de los repositorios
col = list()

# me tardó en correr 50 min aprox
for i in range(main.iloc[-1].name + 1):
    
    usrindex = usr2index(main.iloc[i].user)
    repoindex = repo2index(main.iloc[i].repo)
    
    fila.append(usrindex); col.append(repoindex);
        
   