# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import igraph as ig 
from datetime import datetime as dt
from scipy.sparse import coo_matrix

#%%

def list2csvrow(l):
    row = [str(n) for n in l]
    row = ','.join(row)
    return row
    
#%% 

main = pd.read_csv('data/data.txt', delimiter=':')

#%%

user_set = pd.unique(main['user'])
repo_set = pd.unique(main['repo'])

# list with each user dataframe
Kx = [main.loc[main['user'] == u] for u in user_set]

# list with each repo dataframe
Ky = [main.loc[main['repo'] == r] for r in repo_set]

#%%

t0 = dt.now()

q = int(len(user_set)/10)

for p in range(10):
    
    print('inicio p = ', p)
    print(dt.now()-t0)
    
    data = list()
    filas = list()
    cols = list()
    
    inicio = q*p
    fin = q*(p+1)
    if p == 4:
        fin = len(user_set)
    
    for i in range(inicio,fin):
        xi = user_set[i]
        for j in range(len(user_set)):
            s = 0 
            xj = user_set[j]
            for l in range(len(repo_set)):
                if xi in Ky[l]['user'] and xj in Ky[l]['user']:
                    s += 1/Ky[l].shape[0]
            data.append(s/Kx[j].shape[0])
            filas.append(i)
            cols.append(j)    
        print('i: ', i)
        print(dt.now()-t0)

    print('final p = ', p)
    print(dt.now()-t0)
    
    f = open('part' + p + '.csv', 'w')
    print('data,' + '%s' % list2csvrow(data), file=f)
    print('filas,' + '%s' % list2csvrow(filas), file=f)
    print('cols,' + '%s' % list2csvrow(cols), file=f)
    f.close()
    
    del data
    del filas
    del cols
    
        
#%%
    
#coo = coo_matrix((data, (row, col)), shape=(4, 4))


#        w[i].append(s/Kx[j].shape[0])  
#        w[i][j] = s/Kx[j].shape[0]
#            ail = Ky[l].loc[main['user']==xi].shape[0]
#            ajl = Ky[l].loc[main['user']==xj].shape[0]
#            ail = main.loc[main['repo']==yl].loc[main['user']==xi].shape[0]
#            ajl = main.loc[main['repo']==yl].loc[main['user']==xj].shape[0]
#            if ail != 0 and ajl != 0:
#                s += 1/Ky[l].shape[0]
        
        
        
        
        
        