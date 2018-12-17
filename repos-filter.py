# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 15:04:51 2018

@author: noelp
"""

runfile('mapeo.py')

import pandas as pd
from datetime import datetime as dt
import numpy as np
import igraph as ig

#%%.
langs = pd.read_csv('contest/lang.txt', sep=':')
reposCG = ig.read('repos-CG-undirected.gml')
#%% 


def strseparator(string, sep1=',',sep2=';'):
    elements = dict()
    lines = string.split(sep1)
    for m in lines:
        elements[m.split(sep2)[0]] = m.split(sep2)[1]
    return elements

def timer(i,count = 100):
    if i ==1:
        print('Primera iteración', dt.now()-t0)                        
    if i ==int(count*0.1):
        print('10%', dt.now()-t0)
    if i == int(count*0.25):
        print('25%', dt.now()-t0)
    if i == int(count*0.5):
        print('50%', dt.now()-t0)
    if i == int(count*0.75):
        print('75%', dt.now()-t0)
    if i == int(count*0.99):
        print('99%', dt.now()-t0)
        

#%%
t0 = dt.now()
d = 0
vid = list()
for v in reposCG.vs:  
    idx = index2repo(v['id'])
    l = langs.loc[langs['repo'] == idx]
    if l.empty != True:
        v['lang'] = strseparator(l.iloc[0].lan)
    else:
        vid.append(v['id'])
        d += 1
    print('i: ',idx,'to delete:',d)
    timer(v.index, count= reposCG.vcount())
        

#%%
idx = [ reposCG.vs.find(id = k).index for k in vid]
reposCG.delete_vertices(idx)

#%%

reposCG.write_pickle('repos.pickle')

#%%
N = reposCG.ecount()
eid = list()
tresh = 0.002
t0 = dt.now()
for idx, e in enumerate(reposCG.es):
    if e['weight'] <= tresh:
        eid.append(idx)
    timer(idx,count=N)
    
#%%

reposCG.delete_edges(eid)
repos_giant = reposCG.components().giant()
repos_giant.write_pickle('reposCG.pickle')


