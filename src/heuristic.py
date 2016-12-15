import networkx as nx
from util import *

def heuristic_cover(graph , preprocess = False):
    """
        heuristica
        se preprocess entao
            realiza o preprocessamento para remover vertices com apenas um vizinho
            retornando os vertices ja visitados

        enquanto existir vertices no grafo
            v = vertice de maior grau de G
            marcado[v]=1
            adiciona v a cobertura
            para cada u vizinho de v
                marcado[u] = 1
                remove u do grafo
            remove g do grafo

        retorna cobertura
    """
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
    print("--- Heuristica")
    print("\tExec time: "+str((end-start))+" sec")
    return cover
