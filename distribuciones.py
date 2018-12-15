
"""
Si hay variables que no están definidas, correrlas desde caract-graph.py
"""
from matplotlib import pyplot as plt
import numpy as np

#%%
  
def logdist(lista, N, n=14, w=False):

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
    
    return k, pk, centros, pk_log

#%%

def applyPlotStyle(xname,yname):
    plt.xlabel(xname,weight='bold',fontsize=12)
    plt.ylabel(yname,weight='bold',fontsize=12)
    plt.gcf().set_size_inches([5, 4])
    plt.tight_layout()
    plt.show(block=False)

#%%
'''
Distribución logarítmica de grado
no dirigida
'''

k, pk, centros, pk_log= logdist(red_filt.degree(), 
                                red_filt.vcount(), n=75)

#%%
    
plt.figure(2)
plt.title('Log Binning',loc='right',fontsize=10)
plt.title('DISTRIBUCIÓN DE GRADO',loc='left',fontsize=10)
plt.loglog(k,pk,'.',color='0.9')
plt.loglog(centros,pk_log,'.')
applyPlotStyle('k',r'p$_k$')    

#plt.gcf()
#plt.savefig('grado-cg-users.png', format='png',dpi=2000)
#plt.gcf().get_size_inches()

#%%
'''
Distribución logarítmica de pesos de enlaces
no dirigida
'''

k, pk, centros, pk_log= logdist(wei, red.ecount(), n=100, w=True)

#%%%

plt.figure(3)
plt.title('Log Binning',loc='right',fontsize=10)
plt.title('DISTRIBUCIÓN DE PESOS',loc='left',fontsize=10)
#plt.loglog(k,pk,'.',color='0.9')
plt.loglog(centros,pk_log,'.')
applyPlotStyle('w',r'p$_w$')
plt.show()

#plt.savefig('pesos-cg-users.png', format='png',dpi=2000)

#%%
'''
Distribución logarítmica de grado BIPARTITA USERS
'''

k, pk, centros, pk_log= logdist(ku, len(ku), n=17)

#%%%

plt.figure(3)
plt.title('Log Binning',loc='right',fontsize=10)
plt.title('DIST. GRADO RED BIPIPARTITA',loc='left',fontsize=10)
plt.loglog(k,pk,'.',color='0.9')
plt.loglog(centros,pk_log,'.')
applyPlotStyle('k',r'p$_k$')
plt.show()

#plt.savefig('pesos-bip-users.png', format='png',dpi=2000)

#%%
'''
Distribución logarítmica de grado BIPARTITA REPOS
'''

k, pk, centros, pk_log= logdist(kr, len(kr), n=17)

#%%%

plt.figure(3)
plt.title('Log Binning',loc='right',fontsize=10)
plt.title('DIST. GRADO RED BIPIPARTITA',loc='left',fontsize=10)
plt.loglog(k,pk,'.',color='0.9')
plt.loglog(centros,pk_log,'.')
applyPlotStyle('k',r'p$_k$')
plt.show()

plt.savefig('grado-bip-repos.png', format='png',dpi=2000)

