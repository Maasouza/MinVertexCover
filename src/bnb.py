import util
from queue import Priority
import time
import random
from util import *
from heuristic import *

def branch_and_bound(g):
    start = time.time()
    cover = []
    my_pq = Priority()
    start_solution = convert(heuristic_cover(g))
    start_lower = len(start_solution)/2
    my_pq.push(
        (
            None,#cover
            tuple(g.nodes()),#vertices que podem ser utilizados
            tuple(g.nodes()),#vertices que estao no grafo
            start_lower #limite inicial
        ),
            g.number_of_edges()#prioridade
        )

    best = (len(start_solution),start_solution)
    print("Start solution: %d - Time: %.2f"%(best[0],time.time()-start))
    itt = 0
    while not my_pq.isEmpty():
        itt += 1
        sub_problem = None
        sub_p_cover = None
        left_vertex = None
        left_graph = None
        this_lower_bound = None

        #pega a maior prioridade (menor numeor de vertices restante)
        sub_problem = my_pq.pop()

        if(sub_problem[0]==None):
            sub_p_cover = []
        else:
            sub_p_cover = list(sub_problem[0])

        left_vertex = list(sub_problem[1])
        left_graph  = g.subgraph(list(sub_problem[2]))
        this_lower_bound = sub_problem[3]

        best_choice = max_degree_vertex(left_graph,left_vertex)
        new_cover_with_v = list(sub_p_cover)
        new_cover_with_v.append(best_choice)



    return cover

def modify_graph(g,vertices):
    """retorna uma lista com todos os vertices do
    grafo que nao sao os vertices de entradas nem
    vizinhos de todos eles"""
    return [i for i in g.node() if(i not in vertices)]


def lower_bound(g):
    return len(heuristic_cover(g))/2

def upper_bound(g):
    return len(heuristic_cover(g))
