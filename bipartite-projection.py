
## LIBRERIAS

from datetime import datetime as dt
from scipy.sparse import csr_matrix

 
#%% 

''' 
BIPARTITE NETWORK PROJETION 
funciones que tuve que definir para correr weightmatrix() y armar la 
matriz de la proyección sobre un tipo de nodos
'''

def position(elem, type1, start=0):
    
    '''
    asumo que type1 está ordenada de menor a mayor
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


def obtain(inicio, final, type2):
    
    '''
    devuelve lista con elemenentos de type2 con índicies entre 
    inicio y final incluidos
    '''
    
    return type2[inicio:final+1]


def coincidence(l1, l2):
    
    comun = list()
    for elem in l1:
        if elem in l2:
            comun.append(elem)
            
    return comun


def degreetype(ty):
    
    '''
    devuelve diccionario con elemento (key) y su respectivo grado (value)
    en la red bipartita
    '''
    
    tydegree = dict()
    sort = sorted(ty)
    final = 0

    for elem in set(ty):
        inicio, final = position(elem,sort,start=final)
        tydegree[elem] = final - inicio + 1
    
    return tydegree


#%% 

'''
FUNCIÓN PRINCIPAL PARA CALCULAR LA MATRIZ DE PESOS DE LA PROYECCIÓN
'''


def weightmatrix(type1, type2, ty2degree):
    
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
        wi = obtain(ii, fi, type2)
        
        fj = 0
        for j in set(type1):
           
            ij, fj = position(j, type1, start=fj)
            wj = obtain(ij, fj, type2)
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
    
'''
PRUEBA
todo arranca con 't' de test
'''

##  listas para bipartita

tfila = [0,1,2,3,4,5,5,5,5,5,6,6]
tcol = [0,1,2,3,4,0,1,2,3,4,3,4]
tdata = [1]*len(tfila)

tbip = csr_matrix((tdata, (tfila, tcol)), shape=(max(tfila)+1, max(tcol)+1))


## Armo diccionario con repo y su respectivo grado
    
ty2degree = degreetype(tcol)

## ARMO MATRIZ DE PESOS PARA USUARIOS

tpeso, tufila, tucol = weightmatrix(tfila, tcol, ty2degree)

wij = csr_matrix((tpeso, (tufila, tucol)), shape=(max(tufila)+1, max(tucol)+1))


print('MATRIZ BIPARTITA') 
print(tbip.toarray())

print('MATRIZ DE PESOS CON PROYECCIÓN EN LOS ELEM. DE LA FILA')
print(wij.toarray())


#%%

'''
CELDA PARA CREAR MATRIZ BIPARTITA DE USUARIOS Y REPOS
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
CALCULO MATRIZ PESOS 

ENTRE USUARIOS: tardó 5 horas en correr aprox
fila corresponde a los índices de los usuarios y 
col a los ínidices de los repos

ENTRE REPOS: ya corrió en 12 horas je
fila corresponde a los índices de los repos y 
col a los ínidices de los usuarios

OBS: la celda de sorteo de fila debe estar corrida!
'''

## Armo diccionario con repo y su respectivo grado
    
ty2degree = degreetype(col)

## ARMO MATRIZ DE PESOS PARA USUARIOS

peso, ufila, ucol = weightmatrix(fila, col, ty2degree)


#%%

'''
CARGO MATRIZ PESOS
cargar pesos, ufila, ucol con loadcsv.py
'''

wij = csr_matrix((peso, (ufila, ucol)), shape=(max(ufila)+1, max(ucol)+1))
        
del peso
del ufila
del ucol


     
        
        