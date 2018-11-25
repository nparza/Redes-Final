# Redes-TPFinal

## Archivos

### Base

- _info.ipynb_ jupyter notebook con información útil, cosas que queremos correr una sola vez y tener a mano.
- _loadcsv.py_, _savecsv.py_ lo que su nombre indica.
- _mapeo.py_ tiene las funciones para mapear los ID de repos y usuarios a los índices matriciales con los que los vamos a referenciar y viceversa. También crea la matriz bipartita en formato esparza.


### Matriz de pesos

- _bipartite-projection.py_ teniendo las dos listas de la matriz bipartita esparza, crea la matriz de pesos de un tipo de nodos. También genera un modelo de prueba.




- _createGraphnx.py_ crea el grafo principal en networkx
- _subfromgraph.py_ crea un subgrafo a partir del principal
- _caract-igraph.py_ caracteriza cualquier grafo en igraph (Estas cosas son más rápidas en igraph)
- _plot-nx.py_ plotea un grafo en networkx (NO APTO PARA REDES GRANDES)
- _func.py_ tiene (casi) todo lo que quieren las wachas


## __Importante__

No guardes los grafos en el github. 
Fijate donde los guardas cuando creás uno nuevo (o sea hacete una carpetita aparte de la de git)
Yo los estoy subiendo al drive, junto con los ploteos de todo

## Porfis

Revisá la distribución de grado y peso.


