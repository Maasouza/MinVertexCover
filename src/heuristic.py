import networkx as nx
from util import *


def heuristic_cover(graph , preprocess = False):
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
        for i in g.neighbors(v):




    return cover




g = nx.Graph()
load_graph(g,"../data/test.dat")

heuristic_cover(g)



