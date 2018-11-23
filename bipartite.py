
'''
MATRIX DE ADYACENCIA RED BIPARTITA
Correr mapeo.py si quiero correr esta celda
A continuación creo las listas para la matriz esparsa de la red bipartita
Asumimos que la lista data es [1,1,..,1]

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
    
'''
Estas dos listas ya están guardadas en bipartite.csv
Para cargarlas usar loadcsv.py
'''

#%%

## LIBRERIAS

from datetime import datetime as dt
from scipy.sparse import csr_matrix

 
#%% 

## FUNCIONES

def position(elem, type1, start=0):
    
    '''
    asumo que fila está ordenada de menor a mayor
    '''
    
    # encuentro la posición del primer elemento
    i = start 
    while type1[i] != elem:
        i += 1
    inicio = i
    
    # encuentro la posición del último elemento
    while i < len(type1)-1 and type1[i] == type1[i+1]:
        i += 1
    final = i
    
    return inicio, final


def obtainrepo(inicio, final, type2):
    
    '''
    devuelve lista de repos con índicies entre inicio y final incluidos
    '''
    
    return type2[inicio:final+1]


def coincidence(l1, l2):
    
    comun = list()
    for elem in l1:
        if elem in l2:
            comun.append(elem)
            
    return comun


#%% 

def degreetype2(type2):
    
    ty2degree = dict()
    sort = sorted(type2)
    final = 0

    for rep in set(type2):
        inicio, final = position(rep,sort,start=final)
        ty2degree[rep] = final - inicio + 1
    
    return ty2degree


def weightmatrix(type1, type2):
    
    '''
    los elementos de type1 son del espacio a donde quiero hacer la 
    proyección de pesos
    type2 son los nodos de los que me quiero independizar
    type1 debe estar ordenada de menor a mayor
    type2 está ordenada según type1
    '''
    t0 = dt.now()
    peso = list()
    ufila = list()
    ucol = list()
    
    fi = 0
    for i in set(type1):
        
        print('i: ', i); print(dt.now()-t0)
        ii, fi = position(i, type1, start=fi)
        wi = obtainrepo(ii, fi, type2)
        
        fj = 0
        for j in set(type1):
           
            ij, fj = position(j, type1, start=fj)
            wj = obtainrepo(ij, fj, type2)
            comun = coincidence(wi, wj)
            
            if len(comun) != 0:
                suma = 0
                for l in comun:
                    suma += 1/ty2degree[l]
                peso.append(suma/len(wj))
                ufila.append(i)
                ucol.append(j)
    
    return peso, ufila, ucol
            
    
#%% 
    
'''PRUEBA'''

##  listas para bipartita

tfila = [0,1,2,3,4,5,5,5,5,5,6,6]
tcol = [0,1,2,3,4,0,1,2,3,4,3,4]
tdata = [1]*len(tfila)

tbip = csr_matrix((tdata, (tfila, tcol)), shape=(max(tfila)+1, max(tcol)+1))


## Armo diccionario con repo y su respectivo grado
    
ty2degree = degreetype2(tcol)

## ARMO MATRIZ DE PESOS PARA USUARIOS

peso, ufila, ucol = weightmatrix(tfila, tcol)

wij = csr_matrix((peso, (ufila, ucol)), shape=(max(ufila)+1, max(ucol)+1))


#%%

'''
MATRIZ BIPARTITA
cargar las listas fila y col con loadcsv.py
crear la matriz esparza bipartita
'''

data = [1]*len(fila)

bip = csr_matrix((data, (fila, col)), shape=(max(fila)+1, max(col)+1))


#%%

## Sorteo de menor a mayor la lista fila
## Col se sortea según fila

fsort, csort = zip(*sorted(zip(fila, col)))

fila = list(fsort); del fsort
col = list(csort); del csort


#%%        

'''
CALCULO MATRIZ PESOS ENTRE USUARIOS
tardó 9 horas en correr aprox
'''

## Armo diccionario con repo y su respectivo grado
    
ty2degree = degreetype2(col)

## ARMO MATRIZ DE PESOS PARA USUARIOS

peso, ufila, ucol = weightmatrix(fila, col)


#%%

'''
CARGO MATRIZ PESOS
cargar pesos, ufila, ucol con loadcsv.py
'''

wij = csr_matrix((peso, (ufila, ucol)), shape=(max(ufila)+1, max(ucol)+1))
        
        
        
        
    
    
    
