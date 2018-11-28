
import igraph as ig
from scipy.sparse import csr_matrix

'''
nececisto la matriz de adyacencia pesada wij
correr la celda 'PRUEBA' de bipartite-projection.py
'''

#%%

'''
DIRIGIDO
filas: targets, columnas: sources, por cómo calculamos la matriz pesos
'''

targets, sources = wij.nonzero()
edgelist = list(zip(sources.tolist(), targets.tolist()))

node_names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']

tg = ig.Graph(edgelist, directed=True, 
             edge_attrs={'weight': wij.data.tolist()},
             vertex_attrs={'label': node_names})

#%%

'''
NO DIRIGIDO - PESO PROMEDIO
'''

tg2 = tg.copy()
tg2.to_undirected(mode='collapse', combine_edges='mean')
rmloops(tg2)


#%%

def plot(graph, filename='test.png', layout='circular'):
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
    visual_style['edge_width'] = [10*float(w) \
                for w in graph.es['weight']]
    ig.plot(graph, filename, **visual_style) 

plot(tg)

#%% EDGES

print('NO DIRIGIDO')
for idx, e in enumerate(tg2.es):
    print(idx, e.tuple, e['weight'])   

print('DIRIGIDO')    
for idx, e in enumerate(tg.es):
    print(idx, e.tuple, e['weight'])      
    

#%% VERTEX

print('NO DIRIGIDO')
for idx, v in enumerate(tg2.vs):
    print(idx, v.index, v['label'])   

print('DIRIGIDO')    
for idx, v in enumerate(tg.vs):
    print(idx, v.index, v['label'])      

#%%

ig.write(g2,'test.gml')      



        
     
    