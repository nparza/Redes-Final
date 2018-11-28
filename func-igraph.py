
## PARA IGRAPH

def timear(t0, texto):
    
    print(texto + ' ', dt.now()-t0)


def rmloops(g):
    
    index = list()
    for idx, e in enumerate(g.es):
        if g.is_loop(e) == True:
            index.append(idx)
    g.delete_edges(index)
    
    





