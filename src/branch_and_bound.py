import util
import Queue as q
import time
import random
from util import *
from heuristic import *
import math

def branch_and_bound(g):
    """
        Branch and bound
        cria um fila de prioridades, onde os primeiros a serem executados sao os branchs com menos vertices a serem verificados
        executa a heuristica feita para receber uma solucao inial
        melhor_solucao = solucao_inicial
        define o lower_bound como a metade da melhor solucao
        adciona ((cobertura,vertices que podem ser escolhidos,vertices no grafo,lower_bound),prioridade)
        enquanto a fila nao estiver vazia
            sub_problema = fila.pop()
            se sub_problema_cobertura forma uma cobertura
                se sub_problema_cobertura melhor que melhor solucao
                    melhor solucao = sub_problema_cobertura
            senao
                v = seleciona_melhor_vertice
                sub_problema_cobertura U v
                se solucao_atual + solucao_resto_do_grafo/2 < lower_bound
                    adiciona sub_problema_alterado a fila
                remove v do sub_problema_cobertura
                remove v dos vertices que ainda podem ser utilizados
                se vertices que ainda podem ser utilizados formam uma cobertura
                    adciona sub_problema_alterado a fila
        retorna melhor_solucao
    """
    start = time.time()
    my_pq = q.PriorityQueue() #lista de prioridade
    start_solution = convert(heuristic_cover(g))
    start_lower = math.floor(len(start_solution)/2)

    my_pq.put(#adicionar o novo elemento
        (
            None,#cover
            tuple(g.nodes()),#vertices que podem ser utilizados
            tuple(g.nodes()),#vertices que estao no grafo
            start_lower #limite inicial
        ),
            nx.number_of_nodes(g)#prioridade
        )

    best = (len(start_solution),start_solution)

    print(str(best[1])+" - Start solution: %d - Time: %.2f"%(best[0],time.time()-start))

    itt = 0

    sub_problem = None
    sub_p_cover = None
    left_vertex = None
    left_graph = None
    this_lower_bound = None

    while not my_pq.empty():
        itt += 1
        #pega a maior prioridade (menor numeor de vertices restante)
        sub_problem = my_pq.get()

        if(sub_problem[0]==None):
            sub_p_cover = []
        else:
            sub_p_cover = list(sub_problem[0])
        left_vertex = list(sub_problem[1])
        left_graph  = g.subgraph(list(sub_problem[2]))
        this_lower_bound = sub_problem[3]

        random.seed()
        best_pick = random.choice(left_vertex)
        new_cover_with_v = list(sub_p_cover)
        new_cover_with_v.append(best_pick)
        new_left_possibles = modify_graph(left_graph,best_pick)
        new_total_possibles = set(left_vertex).intersection(new_left_possibles)
        new_left_graph = g.subgraph(new_left_possibles)

        #Se nao tiver mais nos a serem pesquisados
        if nx.number_of_nodes(new_left_graph) == 0:
            #se a achada foi melhor que a atual
            if len(new_cover_with_v) < best[0]:
                best = (len(new_cover_with_v),new_cover_with_v)
                print(str(best[1])+" - New solution: %d - Time: %.2f"%(best[0],time.time()-start))
        else:
            #se ainda houver elementos a serem testados
            if len(new_left_possibles) > 0 :

                cost = len(new_cover_with_v) + math.floor(heuristic(new_left_graph))
                if cost < best[0]:
                    my_pq.put(
                        (
                            tuple(new_cover_with_v),
                            tuple(new_total_possibles),
                            tuple(new_left_possibles),
                            cost
                        ),
                            nx.number_of_nodes(new_left_graph)
                        )

        cover_without_v = list(sub_p_cover)
        new_left_possibles_without_v = list(left_vertex)
        new_left_possibles_without_v.remove(best_pick)

        #Verifica se ainda e viavel
        if len(new_left_possibles_without_v) > 0 and still_coverable(left_graph,best_pick,new_left_possibles_without_v):
            if this_lower_bound < best[0]:
                my_pq.put(
                        (
                            tuple(cover_without_v),
                            tuple(new_left_possibles_without_v),
                            tuple(sub_problem[2]),
                            this_lower_bound
                        ),
                            nx.number_of_nodes(left_graph)
                        )



    print(str(best[1])+" - BEST solution: %d - Time: %.2f"%(best[0],time.time()-start))
    return best

def modify_graph(g, vertices):
        """retorna todos os vertices de g que nao
        pertencem a vertices e nem sao vizinhos de todos os vertices"""
        if not isinstance(vertices, list):
            vertices = [vertices]

        return [ v for v in g.nodes() if (v not in vertices and not set(g.neighbors(v)) < set(vertices)) ]

def still_coverable(g,removed_vertex,left_vertices):
    """verifica se o grafo ainda e pode ter corbertura se remover um vertice"""
    neigh = set(g.neighbors(removed_vertex))

    if len(neigh) > 0:
        if not neigh <= set(left_vertices):
            return False
    if len(neigh)== 0:
        return False

    return True

def heuristic(graph):
    cover = set()
    covered_edges = set()
    #para cada aresta do grafo
    for u, v in graph.edges_iter():
        #se u e v nao estiverem na cobertura nem estiverem cobertas
        if (u, v) not in covered_edges and (v, u) not in covered_edges:
            cover.add(u)
            cover.add(v)
            covered_edges = covered_edges | set(graph.edges([u, v]))

    return len(cover)/2
