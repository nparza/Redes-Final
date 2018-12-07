# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 19:32:09 2018

@author: noelp
"""

import pandas as pd
import datetime as dt
import numpy as np

#%%


main = pd.read_csv('data/repos.txt', sep=':|,')

#%% Veamos los baches

bache = list()
t0 = dt.datetime.now()
for i in range(1, main['repo'].shape[0]-1):
    if main['repo'][i-1] != main['repo'][i]-1:
        bache.append((i,main['repo'][i]))
    if i == int(main['repo'].shape[0]*0.25):
        print('25%', dt.datetime.now()-t0)
    if i == int(main['repo'].shape[0]*0.5):
        print('50%', dt.datetime.now()-t0)
    if i == int(main['repo'].shape[0]*0.75):
        print('75%', dt.datetime.now()-t0)

print('Baches',len(bache))

#%% Mi matriz va a tener las mismas filas y columnas

repo = list(set(main['repo']))
r = range(len(repo))

def repo2index(a):
        return r[repo.index(a)]

#%%

## Creo los elementos de mi matriz esparza


col = list() ##Repos hijos
fila = list() ##Repos padres

t0 = dt.datetime.now()
for i in range(main.iloc[-1].name + 1):
    a = main.iloc[i]
    if np.isnan(a.forked) != True:
        fila.append(repo2index(a.repo))
        col.append(repo2index(a.forked))
    if i ==int(main['repo'].shape[0]*0.1):
        print('10%', dt.datetime.now()-t0)
    if i == int(main['repo'].shape[0]*0.25):
        print('25%', dt.datetime.now()-t0)
    if i == int(main['repo'].shape[0]*0.5):
        print('50%', dt.datetime.now()-t0)
    if i == int(main['repo'].shape[0]*0.75):
        print('75%', dt.datetime.now()-t0)
    if i == int(main['repo'].shape[0]):
        print('100%', dt.datetime.now()-t0)

data = np.ones(len(col))
#%%