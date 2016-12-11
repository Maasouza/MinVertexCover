import networkx as nx
from util import *

def heuristic_cover(graph , preprocess = False):

    start = time.time()
    g = nx.Graph()
    g.add_edges_from(graph.edges())
    if(preprocess):
        cover,marked,visited = pre_process(g)
    else:
        cover = [False for x in range(len(g.nodes()))]
        marked = [False for x in range(len(g.nodes()))]
        visited = 0

    while(visited!=len(graph.nodes())):
        v = max_degree_vertex(g)
        cover[v]=True
        visited+=1
        for u in g.neighbors(v):
            visited+=1
            g.remove_node(u)
        g.remove_node(v)

    end = time.time()
    print("--- Heuristica ---")
    print("--- Exec time: "+str((end-start)*1000)+" sec ---")
    return cover

g = nx.Graph()
load_graph(g,"../data/grafo.dat")

c = heuristic_cover(g)

draw_results(g,c)



