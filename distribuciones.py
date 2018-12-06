
"""
Si hay variables que no están definidas, correrlas desde caract-graph.py
"""

#%%
  
def logdist(lista, N, n=14, w=False):
    
    '''
    lista: elementos de la distribución
    N: normalización
    '''
    
    kmax = max(lista)
    kmin = min(lista)
    
    K = dict()
    
    for i in set(lista):
        K[i]=0
    
    for k in lista:
        K[k]+=1
    
    k = list(K.keys())    
    pk = np.array(list(K.values()))/N
    
    if w:
        Bins = np.logspace(np.log10(kmin),np.log10(kmax+1),n)
    else:
        Bins = np.logspace(0,np.log10(kmax+1),n)
    
    h,bins=np.histogram(lista, Bins)
    centros=[]
    for i in range(len(bins)-1):
        c=(bins[i]+bins[i+1])/2
        centros.append(c)
    
    A=[]
    for i in range(len(h)):
        A.append(h[i]/(bins[i+1]-bins[i]))
    pk_log=A/sum(A)
    
    return k, pk, centros, pk_log, sum(A)

#%%
'''
Distribución logarítmica de grado o peso del grafo
no dirigida
'''

k,pk,centros,pk_log, sumA = logdist(red.degree(), red.vcount(), n=90)

plt.figure(2)
plt.title('Log-Log Scale, Log Binning',loc='left',fontsize=10)
plt.loglog(k,pk,'.',color='0.9')
plt.loglog(centros,pk_log,'.')
applyPlotStyle('k',r'p$_k$') 
#applyPlotStyle('w',r'p$_w$')
plt.show()
