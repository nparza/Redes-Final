
def list2csvrow(l):
    row = [str(n) for n in l]
    row = ','.join(row)
    return row
    

f = open('weights-repo.csv', 'w')
print('peso,' + '%s' % list2csvrow(peso), file=f)
print('fila,' + '%s' % list2csvrow(ufila), file=f)
print('col,' + '%s' % list2csvrow(ucol), file=f)
f.close()

del f
