# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 01:58:23 2018

@author: noelp
"""
'''
------------SUBGRAFO DEL GRAFO PRINCIPAL----------------

Es necesario tener cargado el grafo principal 'red', para que el nuevo grafo
sea subgrafo de éste


Nodos: users que watchean +70 repos en simultáneo
Enlaces: repo watcheado en simultáneo
Peso: Cantidad de repos watcheados
'''


import igraph as ig
#%%

userGig = ig.read('C:/Users/noelp/Documents/Git/Redes-TPFinal-Grafos/userG.gml')
red = userGig
#%%

vertices = []
for n in range(red.ecount()):
    if red.es[n]['weight'] > 50:
        vertices.append(red.es[n].tuple[0])
        vertices.append(red.es[n].tuple[1])

userSubG = red.subgraph(vertices, implementation="auto")    
    
'''
Hay tres implementaciones:
    googlealas porque no las recuerdo, una crea el subgrafo de la nada, otra extrae 
    los vértices que no le das, y la automática elige una de las anteriores
'''

ig.write(userSubG,'userSubG.gml')

