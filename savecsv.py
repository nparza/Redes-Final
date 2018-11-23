
def list2csvrow(l):
    row = [str(n) for n in l]
    row = ','.join(row)
    return row
    

f = open('bipartite.csv', 'w')
print('filas,' + '%s' % list2csvrow(fila), file=f)
print('cols,' + '%s' % list2csvrow(col), file=f)
f.close()

del f
