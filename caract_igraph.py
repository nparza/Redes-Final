# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 15:07:54 2018

@author: noelp
"""

from func import *
from matplotlib import pyplot as plt
import numpy as np
import igraph as ig



'''
Descomentá el subgrafo que queres caracterizar y tamo

-Distribución de grado o de peso, según prefieras
-Características estructurales (N,L,<k>,densidad, <C>, etc.)
'''


#%% 
'''
Grafo principal
'''

#userG = ig.read('C:/Users/noelp/Documents/Git/Redes-TPFinal-Grafos/userG.gml')
#red = userG
#%%
'''
Nodos que watchean +70 repos en simultáneo
'''

#userSG= ig.read('userSubG.gml')
#red = userSG

#%%%
'''
Algunas chanchadas que quizá necesites
'''

deg = red.degree()
weights=[red.es[n]['weight'] for n in range(red.ecount())]
densidad = red.ecount()/(red.vcount()*(red.vcount()-1)/2)
clustg = red.transitivity_avglocal_undirected(weights=weights)

#%%
'''
Distribución logarítmica de grado o peso del grafo
'''

distribucion = red.degree()
#distribución = weights

k,pk,centros,pk_log = logdist(red.degree(), red.vcount())


plt.loglog(k,pk,'.')
plt.loglog(centros,pk_log,'.')
applyPlotStyle('degree','densidad')
plt.show()


#%%
'''
Caracerísticas estructurales
'''
    
print('Caracerísticas estructurales')
print('Nodos:', red.vcount(),'Edges:', red.ecount())
print('k medio:', np.mean(deg), 'kmax:', max(deg), 'kmin:', min(deg))
print('Densidad:', densidad)
print('Average weight:',np.average(weights))
print('Transitividad:', clustg)

 
