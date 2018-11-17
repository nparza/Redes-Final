# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:12:31 2018

@author: noelp
"""

import igraph as igraph
from matplotlib import pyplot as plt
import networkx as nx

def clusterize(nx_Graph, method="infomap"):
    """
    Calcula el agrupamiento en comunidades de un grafo.
    
    In:
        nx_Graph: grafo de networkx
        method: metodo de clustering, puede ser: "infomap", "fastgreedy", "eigenvector", "louvain", "edge_betweenness","label_prop", "walktrap", ""
        
    Out:
        labels_dict: diccionario de nodo : a label al cluster al que pertenece.
    """
    if method == "edge_betweenness":
        nx_Graph = max(nx.connected_component_subgraphs(nx_Graph), key=len)#se queda con la componente más grande.
        print("AVISO: restringiendo a la componente connexa más grade. De otro modo falla el algoritmo de detección de comunidades edge_betweenness.")
    
    isdirected = nx.is_directed(nx_Graph)
    np_adj_list = nx.to_numpy_matrix(nx_Graph)
    g = igraph.Graph.Weighted_Adjacency(np_adj_list.tolist(),mode=igraph.ADJ_UPPER)
   
    if method=="infomap":
        labels = g.community_infomap(edge_weights="weight").membership
    if method=="label_prop":
        labels = g.community_label_propagation(weights="weight").membership
    if method=="fastgreedy":
        labels = g.community_fastgreedy(weights="weight").as_clustering().membership
    if method=="eigenvector":
        labels = g.community_leading_eigenvector(weights="weight").membership
    if method=="louvain":
        labels = g.community_multilevel(weights="weight").membership
    if method=="edge_betweenness":
        labels = g.community_edge_betweenness(weights="weight", directed=isdirected).as_clustering().membership
    if method=="walktrap":
        labels = g.community_walktrap(weights="weight").as_clustering().membership
    
    label_dict = {node:label for node,label in zip(nx_Graph.nodes(), labels)}
    return label_dict


def ldata(archive):
    f = open(archive)
    data = []
    for line in f:
        line = line.strip()
        col = line.split()
        data.append(col)	
    return data

def degrees(grafo, node = 'All'):
    if node == 'All':
        lista=list(dict(grafo.degree).values())
    else:
        lista= grafo.degree(node)
    return lista

def applyPlotStyle(xname,yname):
    plt.xlabel(xname,weight='bold',fontsize=11)
    plt.ylabel(yname,weight='bold',fontsize=11)
    plt.grid(linestyle=':')
    
    
def logdist(lista, N):
    ''''
    lista: elementos de la distribución
    N: Normalización
    ''''
    kmax=max(lista)
    
    
    K=dict()
    
    for i in set(lista):
        K[i]=0
    
    for k in lista:
        K[k]+=1
    
    k=list(K.keys())    
    pk=np.array(list(K.values()))/N
    
    
    n=14
    bins=np.logspace(0,np.log10(kmax+1),n)
    h,bins=np.histogram(lista, bins=n)
    centros=[]
    for i in range(len(bins)-1):
        c=(bins[i]+bins[i+1])/2
        centros.append(c)
    
    A=[]
    for i in range(len(h)):
        A.append(h[i]/(bins[i+1]-bins[i]))
    pk_log=A/sum(A)
    
    return k, pk, centros, pk_log