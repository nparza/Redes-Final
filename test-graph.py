
import igraph as ig
from scipy.sparse import csr_matrix

'''
nececisto la matriz de adyacencia pesada wij
correr la celda 'PRUEBA' de bipartite-projection.py
'''

#%%

'''
DIRIGIDO
'''

sources, targets = wij.nonzero()
edgelist = list(zip(sources.tolist(), targets.tolist()))

node_names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']

g = ig.Graph(edgelist, directed=True, 
             edge_attrs={'weight': wij.data.tolist()},
             vertex_attrs={'label': node_names})

#%%

'''
NO DIRIGIDO - PESO PROMEDIO
'''

g2 = g.copy()
g2.to_undirected(mode='collapse', combine_edges='mean')


#%%

def plot(graph, filename='prueba.png', layout='circular'):
    layout = graph.layout(layout)
    visual_style = dict()
    visual_style['vertex_size'] = 20
    visual_style['vertex_label_size'] = 30
    visual_style['vertex_label_dist'] = 2
    visual_style['vertex_color'] = "white"
    visual_style['vertex_label_color'] = "blue"
    visual_style['vertex_label'] = graph.vs['label']
    visual_style['edge_width'] = 2
    visual_style['layout'] = layout
    visual_style['bbox'] = (1200, 1000)
    visual_style['margin'] = 100
    ig.plot(graph, filename, **visual_style) 

plot(g2)

#%%

print('NO DIRIGIDO')
for idx, e in enumerate(g2.es):
    print(idx, e.tuple, e['weight'])   

print('DIRIGIDO')    
for idx, e in enumerate(g.es):
    print(idx, e.tuple, e['weight'])      
    

#%%

ig.write(g2,'test.gml')      



        
     
    