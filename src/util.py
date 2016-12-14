import networkx as nx
import matplotlib.pyplot as plt
import operator
import time
import random



def load_graph(graph,file_name):
    """Carrega as arestas do grafo"""
    f = open(file_name,"r")
    f.readline()#jump number of vertices
    edges=[]
    for line in f:
        edge = list(map(int,line.split(" ")))
        edges.append(edge)
    graph.add_edges_from(edges)

def pre_process(graph):
    """Remove os vertices folhas adicionando o vizinho dele a cobertura"""

    g = nx.Graph()
    g.add_edges_from(graph.edges())
    marked = [False for i in range(len(graph.nodes()))]
    cover = [False for i in range(len(graph.nodes()))]
    visited = 0
    changed = True
    times = 0
    removed = 0

    start = time.time()
    while(changed and visited != len(graph.nodes())):
        """Enquanto houver folhas"""
        changed = False
        for v in g.nodes():
            times += 1
            if(marked[v]):
                continue
            neigh = g.neighbors(v)
            if(len(neigh) <= 1):
                removed+=1
                changed=True
                if(len(neigh)==1):
                    cover[neigh[0]]=True
                    for u in g.neighbors(neigh[0]):
                        removed+=1
                        marked[u]=True
                        g.remove_node(u)
                        visited+=1
                    marked[neigh[0]]=True
                    g.remove_node(neigh[0])
                else:
                    cover[v]=True
                    marked[v]=True
                visited+=1
    end = time.time()
    print("--- Pre processamento")
    print("\t"+str(removed)+" vertices removidos em "+str(times)+" iteracoes")
    print("\tExec time: "+str((end-start))+" sec ")
    return cover,marked,visited

def draw_results(graph,cover=None,mode = 0):
    if(mode == 0):
        cover_list = []
        for i in range(len(cover)):
            if(cover[i]):
                cover_list.append(i)
    else:
        cover_list = cover[:]

    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph,pos,node_color='black')
    nx.draw_networkx_nodes(graph,pos,nodelist = cover_list,node_color='r')
    nx.draw_networkx_edges(graph,pos,edge_color='black')
    nx.draw_networkx_labels(graph,pos,font_color='white')
    plt.show()

def isCover(g,cover):
    marked = [0 for i in range(len(g.nodes()))]
    for i in cover:
        marked[i] = 1
        for j in g.neighbors(i):
            marked[j] = 1

    if(sum(marked) == len(marked)):
        return True
    else:
        return False

def max_degree_vertex(graph,vertices = None):
        if(vertices!=None):
            vertex_degree_dict = nx.degree(graph,vertices)
        else:
            vertex_degree_dict = nx.degree(graph)
        random.seed()
        vertex = sorted(vertex_degree_dict.iteritems(), key = lambda x : x[1], reverse = True)
        out = []
        degree = vertex[0][1]
        for i in vertex:
            if(i[1]!=degree):
                break
            out.append(i[0])
        return random.choice(out)
    #return max(vertex_degree_dict.iteritems(), key = operator.itemgetter(1))[0]

def convert(data):
    """funcao que adciona A a C se data[A]==1"""
    c = []
    for i in range(len(data)):
        if data[i] == 1:
            c.append(i)
    return c