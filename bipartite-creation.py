
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
        
   

