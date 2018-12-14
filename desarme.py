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
    cutoff = [0]
    N = red.vcount()
    E = red.ecount()
    copy = red.copy()
    cg = copy.components().giant()

    i = 0
    
    while cg.vcount()/N > tresh and i < len(setwei):
         
        eliminar = [] 
        for idx, e in enumerate(cg.es):
            if e['weight'] <= setwei[i]:
                eliminar.append(idx)

        if len(eliminar) > 0:
            cg.delete_edges(eliminar)
            cg = cg.components().giant()
        
            if cg.vcount()/N > tresh:   
                fe.append(len(eliminar)/E + fe[-1])
                fn.append(cg.vcount()/N)
                cutoff.append(setwei[i])
                print(setwei[i], len(fe))
        i += 1
    
    return fe, fn, cutoff
    
    
#%%

umbrales = np.logspace(np.log10(min(setwei)),np.log10(max(setwei)),500)
fe, fn, cutoff = desarme_peso(redu, umbrales, 0.05)  

#%%

'''
PLOTEAR DESARME POR PESO
'''
    
def applyPlotStyle(xname,yname):
    plt.xlabel(xname,weight='bold',fontsize=12)
    plt.ylabel(yname,weight='bold',fontsize=12)
    plt.gcf().set_size_inches([5, 8])
    plt.tight_layout()
    plt.show(block=False)
     
plt.figure(24)
plt.subplot(2,1,1)
plt.semilogx(cutoff,fn,'.')
applyPlotStyle('weight cutoff','fracción de nodos comp. gigante') 
plt.subplot(2,1,2)
plt.plot(fe,fn,'r.')
applyPlotStyle('fracción de enlaces removidos','fracción de nodos comp. gigante') 

#plt.subplots_adjust(wspace=None, hspace=0.285)
#plt.savefig('desarme-users-peso-mM.png', format='png',dpi=2000)

   
