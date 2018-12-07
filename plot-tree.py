# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 08:11:32 2018

@author: noelp
"""

import igraph as ig

#%%
## Cargar datos con load.csv
    
g = ig.read('forks-directed.gml')

#%%
def plot(graph, filename="net.svg"):
    from igraph import plot
    layout = graph.layout("circular")
    visual_style = dict()
    visual_style["vertex_size"] = 20
    visual_style["vertex_color"] = "red"
    visual_style["edge_width"] = 2
    visual_style["layout"] = layout
    visual_style["bbox"] = (1200, 1000)
    visual_style["margin"] = 100
    plot(graph, filename, **visual_style) 
    
plot(g, filename='tree.svg')

#%%

def plot_network(g, out_fig_name, vertex_label_field, layout="fr"):
    """ Plot network.

    Args:
        @param g
        @type g: iGraph.Graph object
        @param out_fig_name: if None, image won't be saved to file
        @type out_fig_name: string or None
        @param vertex_label_field: vertex attribute field used for labels
        @type vertex_label_field: string
        @param layout: layout to use for plotting; default = "fr", aka
            Fruchterman Reingold; some other options include "kk" for
            Kamada Kawai, "circle" for circular, and "bipartite"
        @type layout: string

    Returns:
        None

    """
    margin = 80

    # Check if vertex_label_field was provided
    if vertex_label_field is None:
        labels = None
    else:
        labels = g.vs[vertex_label_field]

    # # Check if vertex_color_field was provided
    # if vertex_color_field is None:
    #     colors = None
    # else:
    #     colors = g.vs[vertex_color_field]

    # Do it
    ig.plot(g, out_fig_name,
            layout=layout,
            vertex_size=10,
            vertex_label=labels,
            vertex_label_dist=2,
            edge_arrow_size=0.3,
            edge_curved=False,
            margin=(margin, margin, margin, margin))

    if out_fig_name is not None:
        logger.info("Network saved to {}".format(out_fig_name)) 
        
plot_network(g, 'tree.svg', vertex_label_field=None, layout="kk")
