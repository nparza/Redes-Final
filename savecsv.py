
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

vertex_clustering_obj = rdv

f = open('cluster-infomap-repos-directed.csv', 'w')
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