
## PARA IGRAPH

def rmloops(g):
    
    '''
    asume que todos los nodos tienen self-loop
    '''
    
    loops = list()
    for i in range(g.vcount()):
        loops.append((i,i))  
        g.delete_edges(loops)





