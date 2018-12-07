#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Tener cargado el grafo 'red' que sea la componente gigante de los grafos
users o repos
'''

from matplotlib import pyplot as plt

#%%

wei = [red.es[n]['weight'] for n in range(red.ecount())]
setwei = sorted(list(set(wei)))

#%%

#def desarme_peso(red, setwei):
#    
#    eliminar = []
#    for idx, e in enumerate(red.es):
#        if e['weight'] <= setwei[0]:
#            eliminar.append(idx)
#    
#    red.delete_edges(eliminar)
#    cg = red.components().giant()
#    
#    #if cg.vcount()/red.vcount() <= 0.1:
#    if len(setwei) == 10000:
#         return []
#    
#    return [(len(eliminar), cg.vcount())] + desarme_peso(cg, setwei[1:])


#        idx = []
#        wei = []
#        for x, e in enumerate(cg.es):
#            idx.append(x)
#            wei.append(e['weight'])
#        idxsort, weisort = zip(*sorted(zip(idx, wei)))
#        idx = list(idxsort); del idxsort
#        wei = list(weisort); del weisort
#        
#        eliminar = []
#        i = 0
#        while wei[i] <= setwei[i]:
#            eliminar.append(idx[i])
#            i += 1


def desarme_peso(red, setwei):
    
    fe = [0]
    fn = [1]
    N = red.vcount()
    E = red.ecount()
    
    cg = red.copy()  
    i = 0
    
    while cg.vcount()/N > 0.2:
        
        eliminar = []
        for idx, e in enumerate(cg.es):
            if e['weight'] <= setwei[i]:
                eliminar.append(idx)
            
        cg.delete_edges(eliminar)
        cg = cg.components().giant()
        
        if cg.vcount()/N > 0.2:
            
            fe.append(len(eliminar)/E + fe[-1])
            fn.append(cg.vcount()/N)
            print(setwei[i])
            i += 1
    
    return fe, fn
    
    
#%%

fe, fn = desarme_peso(red.copy(), setwei)  


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

   
