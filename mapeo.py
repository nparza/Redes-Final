## LIBRERIAS

import pandas as pd
from datetime import datetime as dt

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
    
    
    
   