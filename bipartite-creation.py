
'''
CALCULO MATRIZ DE ADYACENCIA RED BIPARTITA
A continuación creo las listas para la matriz esparsa de la red bipartita
Asumimos que la lista data es [1,1,..,1]
Correr mapeo.py
'''

'''
Estas dos listas ya están guardadas en bipartite.csv
Para cargarlas usar loadcsv.py
'''

# índices de los usuarios
fila = list()

# índices de los repositorios
col = list()

# me tardó en correr 50 min aprox
for i in range(main.iloc[-1].name + 1):
    
    usrindex = usr2index(main.iloc[i].user)
    repoindex = repo2index(main.iloc[i].repo)
    
    fila.append(usrindex); col.append(repoindex);

#%%
    
from scipy.sparse import csr_matrix

'''
CELDA PARA CREAR MATRIZ BIPARTITA DE USUARIOS Y REPOS
cargar las listas fila y col con loadcsv.py
crear la matriz esparza bipartita
'''

'''
Ahora: filas repos, columnas usuarios
'''

bdata = [1]*len(bfila)

bip = csr_matrix((bdata, (bfila, bcol)), shape=(max(bfila)+1, max(bcol)+1))

del bdata
del bfila
del bcol

#%%
    
'''
Armar lista con grado de la red bipartita
'''


ku = list()
kr = list()

for i in range(bip.shape[0]):
    kr.append(bip[i,:].getnnz())

for i in range(bip.shape[1]):
    ku.append(bip[:,i].getnnz())

del i


