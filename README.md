# Redes-TPFinal

## Archivos

### Base

- _info.ipynb_ jupyter notebook con información útil, cosas que queremos correr una sola vez y tener a mano.

- _loadcsv.py_, _savecsv.py_ lo que su nombre indica.

- _mapeo.py_ tiene las funciones para mapear los ID de repos y usuarios a los índices matriciales con los que los vamos a trabajar y viceversa. También crea la matriz bipartita en formato esparza partiendo de _data.txt_.

### Matriz de pesos

- _bipartite-projection.py_ teniendo las dos listas de la matriz bipartita esparza, crea la matriz de pesos de un tipo de nodos. También genera un modelo de prueba.

### Grafos

- _create-graph.py_ crea el grafo de usuarios y repos.

- _test-graph.py_ crea el grafo de prueba generado en  _bipartite-projection.py_.

- _subfromgraph.py_ crea un subgrafo a partir del principal.

- _caract-graph.py_ caracterización general de los grafos.

- _func-old.py_ funciones de otros TPs.
- _func-igraph.py_ funciones para aplicar a grafos de igraph.

#### networkx

- _create-graph-nx.py_ crea grafo en networkx.

- _plot-nx.py_ plotea un grafo en networkx.


## Info

Los grafos `.gml` y archivos `.csv` están en el drive.

