
def list2csvrow(l):
    row = [str(n) for n in l]
    row = ','.join(row)
    return row

#%%    

f = open('weights-repo.csv', 'w')
print('peso,' + '%s' % list2csvrow(peso), file=f)
print('fila,' + '%s' % list2csvrow(ufila), file=f)
print('col,' + '%s' % list2csvrow(ucol), file=f)
f.close()

del f

#%%

'''
CLUSTERS
Guardo el membership que es una lista donde cada posición representa el 
idx de un nodo y el elemento en esa posición es el idx del clúster al
que pertenece
'''

vertex_clustering_obj = udvc

f = open('cluster-infomap-users-directed.csv', 'w')
print(list2csvrow(vertex_clustering_obj.membership), file=f)
f.close()

del f, vertex_clustering_obj

#%%

'''
Family tree
'''

f = open('family-tree.csv', 'w')
print('fila,' + '%s' % list2csvrow(fila), file=f)
print('col,' + '%s' % list2csvrow(col), file=f)
f.close()

del f

#%% 

'''
DESARME
'''

f = open('desarme-peso-mM.csv', 'w')
print('desarme por peso de los enlaces, removiéndolos de menor peso a mayor peso',
      file=f)
print('fn: fracción de nodos de la comp. gigante, \
      fe: fracción de enlaces removidos respecto de la cantidad de enlaces inicial \
      de la CG, cutoff: los nodos removidos tienen peso menor o igual al cutoff',
      file=f)
print('fe,' + '%s' % list2csvrow(fe), file=f)
print('fn,' + '%s' % list2csvrow(fn), file=f)
print('cutoff,' + '%s' % list2csvrow(cutoff), file=f)
f.close()







