# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 14:56:03 2018

@author: noelp
"""

import pandas as pd
import numpy as np
import igraph as ig

#%%

main = pd.read_csv('data/data.txt', delimiter=':')
#%%
user_set = pd.unique(main['user'])
repo_set = pd.unique(main['repo'])

Kx = [main.loc[main['user']==u] for u in user_set]
Ky = [main.loc[main['user']==r] for r in repo_set]

#%%

for i in range(len(user_set)):
    ky = 0
    xi = user_set[i]
    for j in range(len(user_set)):
        xj = user_set[j]
        for l in range(len(repo_set)):
            yl = repo_set[l]
            ail= main.loc[main['repo']==yl].loc[main['user']==xi].shape[0]
            ajl =main.loc[main['repo']==yl].loc[main['user']==xj].shape[0]
            if ail != 0 and ajl != 0:
                ky += 1/Ky[l]
        w[i][j] =ky/Kx[j]