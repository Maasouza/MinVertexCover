import itertools as it
from util import *
import time

def brute_force(g):
    """
        Forca bruta
        gera combinacoes de tamanho N, onde N = 1..V
        util para poucos vertices ou grafos muito esparcos
    """
    start = time.time()
    vertices = list(range(len(g.nodes())))
    itt=0
    for r in range(1,len(vertices)):
        for i in it.combinations(vertices,r):
            cover = list(i)
            itt+=1
            print(itt)
            if(itt==10000000):
                return []
            if(isCover(g,cover)):
                print(time.time()-start)
                return [ 1 if i in cover else 0 for i in range(len(g.nodes()))]
