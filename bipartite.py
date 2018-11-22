
'''
MATRIX DE ADYACENCIA RED BIPARTITA
Correr mapeo.py
A continuación creo las listas para la matriz esparsa de la red bipartita
Asumimos que la lista data es [1,1,..,1]

'''

# índices de los usuarios
fila = list()

# índices de los repositorios
col = list()

t0 = dt.now()
for i in range(main.iloc[-1].name + 1):
    
    usrindex = usr2index(main.iloc[i].user)
    repoindex = repo2index(main.iloc[i].repo)
    
    fila.append(usrindex); col.append(repoindex);
t1 = dt.now() - t0    



