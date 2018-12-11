#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Tener cargado el grafo 'red' que sea la componente gigante de los grafos
users o repos
'''

from matplotlib import pyplot as plt

#%%

wei = [redu.es[n]['weight'] for n in range(redu.ecount())]
setwei = sorted(list(set(wei)))
del wei

#%%

def desarme_peso(red, setwei, tresh):
    
    fe = [0]
    fn = [1]
    N = red.vcount()
    E = red.ecount()
    copy = red.copy()
    
    idx = []
    wei = []
    for x, e in enumerate(copy.es):
        idx.append(x)
        wei.append(e['weight'])
    weisort, idxsort = zip(*sorted(zip(wei, idx)))
    idx = list(idxsort); del idxsort
    wei = list(weisort); del weisort
    
    maxcomp = N
    i = 1
    j = 1
    
    while maxcomp/N > tresh:
         
        eliminar = [] 
        while wei[j] <= setwei[i]:
            eliminar.append(idx[j])
            j += 1
        
        if len(eliminar) > 0:
            copy.delete_edges(eliminar)
            maxcomp = max(copy.components().sizes())
        
            if maxcomp/N > tresh:   
                fe.append(len(eliminar)/E + fe[-1])
                fn.append(maxcomp/N)
                print(setwei[i], len(fe), len(fn))
        i += 1
    
    return fe, fn
    
    
#%%

umbrales = np.logspace(np.log10(min(setwei)),np.log10(max(setwei)+1),1000)
fe, fn = desarme_peso(redu, umbrales, 0.2)  

#%%
    
def applyPlotStyle(xname,yname):
    plt.xlabel(xname,weight='bold',fontsize=12)
    plt.ylabel(yname,weight='bold',fontsize=12)
    plt.gcf().set_size_inches([5, 4])
    plt.tight_layout()
    plt.show(block=False)
     
plt.figure(2)
#plt.title('Log Binning',loc='right',fontsize=10)
#plt.title('DISTRIBUCIÓN DE GRADO',loc='left',fontsize=10)
#plt.loglog(k,pk,'.',color='0.9')
plt.plot(fe,fn,'.')
applyPlotStyle('fracción de enlaces removidos','fracción de nodos comp. gigante') 

   
