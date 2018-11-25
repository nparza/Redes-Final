
import igraph as ig
from scipy.sparse import csr_matrix

'''
nececisto la matriz de adyacencia pesada wij
'''

#%%

'''
CREO MATRIZ PESOS
cargar pesos, ufila, ucol con loadcsv.py
'''

wij = csr_matrix((peso, (ufila, ucol)), shape=(max(ufila)+1, max(ucol)+1))
        
del peso
del ufila
del ucol

#%%

